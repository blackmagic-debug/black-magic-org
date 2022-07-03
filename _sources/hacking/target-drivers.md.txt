# Adding Target Drivers

This is a placeholder of cut-and-pasted text until I have a chance to write up some real documentation for the target API.

## External target API

You can find the public API in [`target.h`](https://github.com/blackmagic-debug/blackmagic/blob/master/src/include/target.h), used by the GDB server. Nothing outside of this header should be accessed from outside of `src/target/*`

## Internal target API

Structure definitions and convenience functions for use in target implementations are defined in [target/target_internal.h](https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/target_internal.h). Specific target implementations fill in the function pointers in these structures for their device specific implementations

## Raw JTAG Devices
Supported JTAG devices are defined in [target/jtag_scan.c](https://github.com/blackmagic-debug/blackmagic/blob/master/src/target/jtag_scan.c#L35)

The `.handler` function is called when a device IDCODE matches `.idcode` with `.idmask` applied.
It is the responsibility of the handler function to instantiate a new target with `target_new` and fill in the access methods.

These functions provide access to the JTAG IR and DR registers:
```c
void jtag_dev_write_ir(jtag_dev_t *dev, uint32_t ir);
void jtag_dev_shift_dr(jtag_dev_t *dev, uint8_t *dout, const uint8_t *din, int ticks);
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
                                target_addr addr, size_t len) {…}
static int skeleton_flash_write(struct target_flash *f,
                                target_addr dest, const void *src, size_t len) {…}


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
