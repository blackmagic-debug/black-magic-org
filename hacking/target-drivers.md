# Adding Target Drivers

This is a placeholder of cut-and-pasted text until I have a chance to write up some real documentation for the target API.

## External target API

You can find the public API in [`target.h`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/include/target.h), used by the GDB server. Nothing defined in `src/target` outside of this header should be accessed from outside of `src/target/*`

## Internal target API

There are several internal API headers:

* [`target/target_internal.h`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/target_internal.h)
  This header contains structure definitions and convinence functions for use in target support implementations.
  Specific target implementations fill in the function pointers in these structures for their device specific
  implementations.
* [`target/target_probe.h`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/target_probe.h)
  This header contains declarations for all the *_probe functions so they're all declared in one central place.
  This header works in tandem with `target/target_probe.c` to allow any target support implementation to be
  switched off as-needed without this breaking the build.

## Raw JTAG Devices

Supported JTAG devices are defined in [target/jtag_devs.c](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/jtag_devs.c)

The `.handler` function is called when a device's ID Code matches the `.idcode` field with `.idmask` applied.
It is the responsibility of the handler function to instantiate a new target with `target_new` and fill in
the access function pointers.

### Raw JTAG access

There is a global structure of function pointers, `jtag_proc` defined in
[`jtagtap.h`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/include/jtagtap.h), which is
automatically initialised to provide access to raw JTAG bus access routines:

```c
typedef struct jtag_proc {
    /* Reset the bus */
    void (*jtagtap_reset)(void);
    /* Step into the next TMS state */
    bool (*jtagtap_next)(const bool tms, const bool tdi);
    /* Step through a sequence of TMS states (up to 32) */
    void (*jtagtap_tms_seq)(uint32_t tms_states, size_t clock_cycles);
    /* Write a number of bits from data_in to TDI, reading the responses back into data_out from TDO */
    void (*jtagtap_tdi_tdo_seq)(uint8_t *data_out, const bool final_tms, const uint8_t *data_in, size_t clock_cycles);
    /* Same as the previous function but without the read-back part */
    void (*jtagtap_tdi_seq)(const bool final_tms, const uint8_t *data_in, size_t clock_cycles);
    /* Runs a series of clock cycles on the bus after establishing an initial TMS + TDI state */
    void (*jtagtap_cycle)(const bool tms, const bool tdi, const size_t clock_cycles);
} jtag_proc_s;
```

There are also some helper macros defined for running certain known sequences onto the bus:

```c
/* Perform a soft reset of the bus */
#define jtagtap_soft_reset() jtag_proc.jtagtap_tms_seq(0x1F, 6)
/* From bus idle, clock into the Shift-IR state */
#define jtagtap_shift_ir() jtag_proc.jtagtap_tms_seq(0x03, 4)
/* From bus idle, clock into the Shift-DR state */
#define jtagtap_shift_dr() jtag_proc.jtagtap_tms_seq(0x01, 3)
/* Return the bus to idle from one of the capture states */
#define jtagtap_return_idle(cycles) jtag_proc.jtagtap_tms_seq(0x01, (cycles) + 1U)
```

### TAP-layer access

There are higher level access functions defined in
[`target/jtag_scan.h`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/jtag_scan.h).

These functions provide higher level access to the JTAG IR and DR registers:

```c
/* Write the dev_index'th device's IR to the value in `ir` */
void jtag_dev_write_ir(uint8_t dev_index, uint32_t ir);
/*
 * Write the dev_index'th device's DR with the data sequence pointed to by data_in,
 * Reading the current DR value back in data_out. Either can be NULL to allow only-readout and only-write operations.
 */
void jtag_dev_shift_dr(uint8_t dev_index, uint8_t *data_out, const uint8_t *data_in, size_t clock_cycles);
```

## ARM implementations (ADIv5)

This table is a list of known Coresight CIDR and PIDR values can be found in [target/adiv5.c](
https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/adiv5.c#L156)

The ROM table is read from the ADIv5 Mem-AP, and the appropriate probe function is called in [target/adiv5.c](https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/adiv5.c#L323).

There is currently support for:

- ARMv6-M/ARMv7-M ([target/cortexm.c](https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/cortexm.c))
- ARMv7-A ([target/cortexa.c](https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/cortexa.c))

The [generic Cortex-M driver](https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/cortexm.c#L257) calls probe functions for each supported vendor device.

These probe functions should probe the target device, add any memories they support with `target_add_ram` and `target_add_flash`, and return `true` for any device they support, or return `false` otherwise.

## Flash programming

The ADIv5 interface does not directly provide a way to write to flash. It's implemented differently for different target devices.  This is done by filling in the function pointers in a `struct target_flash` structure and calling `target_add_flash` on the target in the device specific probe function.

```c
struct target_flash {
    target_addr start;      /* Base address for this block of flash memory */
    size_t length;          /* Length of this block of flash memory */
    size_t blocksize;       /* Erase sector size for this block of flash memory */
    flash_erase_func erase; /* Function pointer to flash erase function.
                               Called with address and length aligned on .blocksize */
    flash_write_func write; /* Function pointer to flash write function.
                               Called with address and length aligned according to .align,
                               and padded with value in .erased. */
    flash_done_func done;   /* Called at the end of flash operations,generic Cortex-M driver

There are a few basic patterns for how this is done in practice:

- **Direct** - writes are passed directly to the target driver which programs the flash directly using MMIO. (eg. [kinetis.c](https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/kinetis.c))
- **Buffered** - the target layer will buffer write packets from GDB until and pass to the driver as writes of whole sectors. The driver will program the target flash directly using MMIO. This works well when whole sectors can be programmed with sequencial writes. (eg. [stm32l0.c](https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/stm32l0.c))
- **Stubbed** - writes are passed directly to the target driver which writes a program stub and the data payload to the target. The stub is then executed to program the device. This works well when flash can't be programmed with sequential writes. (eg. [stm32f1.c](https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/stm32f1.c))
- **LPC** - NXP devices include a built in ROM for programming flash. There is no published MMIO mechanism to program the flash on these devices. (eg. [lpc11xx.c](https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/lpc11xx.c))

### Buffered Flash model
For devices than can only efficiently program flash sectors of a fixed size there is some additional support
in the `target_flash` structure.  To make use of this mechanism, the `.write` and `.done` pointers must be
assigned to `target_flash_write_buffered` and `target_flash_done_buffered` respectively.  The `.align` field should be left set to zero when using the buffered flash model.
```c
struct target_flash {
    ...
    /* For buffered flash */
    size_t buf_size;            /* Size of buffer for buffered operations */
    flash_write_func write_buf; /* Function pointer to buffered flash write function.
                                   Called with address aligned according to .buf_size,
                                   and padded with value in .erased.  The buffer
                                   will always be exactly .buf_size bytes */
};
```

## Skeleton Driver

```c
static int skeleton_flash_erase(struct target_flash *f,
                                target_addr addr, size_t len) {...}
static int skeleton_flash_write(struct target_flash *f,
                                target_addr dest, const void *src, size_t len) {...}

static void skeleton_add_flash(target *t)
{
    struct target_flash *f = calloc(1, sizeof(*f));
    f->start = SKELETON_FLASH_BASE;
    f->length = SKELETON_FLASH_SIZE;
    f->blocksize = SKELETON_BLOCKSIZE;
    f->erase = skeleton_flash_erase;
    f->write = skeleton_flash_write;
    target_add_flash(t, f);
}


bool skeleton_probe(target *t)
{
    if (target_mem_read32(t, SKELETON_DEVID_ADDR) == SKELETON_DEVID) {
        skeleton_add_flash(t);
        return true;
    } else {
        return false;
    }
}
```
