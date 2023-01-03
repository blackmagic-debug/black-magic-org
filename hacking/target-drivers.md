# Adding Target Drivers

## External target API

You can find the public API in [`target.h`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/include/target.h), used by the GDB server. Nothing defined in `src/target` outside of this header should be accessed from outside of `src/target/*`

## Internal target API

There are several internal API headers:

* [`target/target_internal.h`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/target_internal.h)
  This header contains structure definitions and convenience functions for use in target support implementations.
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

There are a few moving parts to the ADIv5 (ARM Debug Interface v5) implementation. The most important ones are:

* The debug interface logic itself found in
  [`target/adiv5.c`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/adiv5.c).
* The generic logic for Cortex-M parts which is found in
  [`target/cortexm.c`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/cortexm.c).
  Please note, this presently supports the ARMv6-M and ARMv7-M profiles only.
* The generic logic for Cortex-A parts which is found in
  [`target/cortexa.c`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/cortexa.c).
  Please note, this presently supports the ARMv7-M profile only.

### ADIv5 Coresight identification

`adiv5.c` implements not just logic for accessing the Debug Port and Access Port components of an ADIv5 Coresight
interface over either JTAG or SWD, but also implements the generic identification logic for devices using this
specification.

When a device is identified during scan that talks ADIv5, the various Coresight CIDR and PIDR values get read out
automatically and decoded. A list of known component class values can be found at the top of `adiv5.c` and
a list of known JEP-106 manufacturer codes (encoded in the PIDR register for each ROM table chunk that must be read)
can be found in the [`target/adiv5.h`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/adiv5.h)
header.

Once an AP has been identified as belonging to either a Cortex-M or a Cortex-A core, the ADIv5 code dispatches to
`cortexm_probe` or `cortexa_probe` accordingly.

### Corex-M device handling

Special consideration is made for ARM's JEP-106 which represents an ARM Cortex device which has not had its ROM
tables customised by the device manufacturer. When the Cortex-M support encounters a device like this in
`cortexm_probe`, the ARM part ID retrieved from the ROM tables is used to identify which type of Cortex-M core
is being probed, and further part identification is then dispatched on the core type.

In either this case or the normal manufacturer-specific JEP-106 case, we then dispatch to one of a number of `_probe`
routines that are then used to specifically identify the part and, on creating a positive part identification,
configure any device-specific behaviour that needs to occur via the `target_s` structure, and if possible
define any known RAM and Flash memory regions via `target_add_ram` and `target_add_flash` (the latter typically
gets wrapped in a target-specific helper).

Once a probe routine creates a positive identification on a part and configures the target structure and memory
regions, it must return `true` to halt the probing process for the AP. If a probe routine fails to create a positive
identification, it must return `false` as soon as possible.

## Flash programming

None of the generic targets are able to provide a generic way to erase or write Flash, as this is implemented
differently for each target device. Instead, as part of the writing target support, you must supply suitable Flash
erase and write routines. The target layer then interacts with the Flash of your target through these routines,
which may even be specific to specific Flash regions depending on how the Flash/NVM controller in the target
device works.

Configuration of these routines is achieved by constructing `target_flash_s` structures, the layout of which is
provided below with member documentation. Once the structure has been filled in with the necessary information
for the target Flash region, `target_add_flash` must then be called to register the region against the target.

If your target requires additional data not present in the `target_flash_s` structure, it is permitted to
write a structure that wraps `target_flash_s` to add the additional members needed. An example of this for the
RP2040 support follows:

```c
typedef struct rp_flash {
    /* This member is what gets passed to `target_add_flash` to register the region */
    target_flash_s f;
    /*
     * RP2040 being Flashless can have an arbitrary Flash programming page size based on the attached
     * SPI Flash device, this field stores what that discovered size is for use in write operations
     */
    uint32_t page_size;
    /* Likewise the instruction to issue to the SPI Flash to erase a sector is device-specific */
    uint8_t sector_erase_opcode;
} rp_flash_s;

static void rp_add_flash(target *t)
{
    /* Allocate the device-specific structure on the heap (this allocates the target Flash structure too */
    rp_flash_s *flash = calloc(1, sizeof(*flash));
    if (!flash) { /* calloc failed: heap exhaustion */
        DEBUG_WARN("calloc: failed in %s\n", __func__);
        return;
    }

    [...]

    /* Grab a member pointer to the target Flash structure */
    target_flash_s *const f = &flash->f;
    [...]
    /* Register with the target structure */
    target_add_flash(t, f);
    [...]
}

bool rp_probe(target *t)
{
    [...]
    /*
     * We can't know the Flash region layout head of time, so we override the target `attach` behaviour
     * and perform RAM and Flash region registration on attach
     */
    t->attach = rp_attach;
    [...]
    return true;
}

static bool rp_attach(target *t)
{
    /*
     * RP2040 is a Cortex-M device, so we *must* call the normal Cortex-M attach routine and
     * propagate errors. It is an error to not do this step somewhere in the target-specific attach routine.
     */
    if (!cortexm_attach(t) || !rp_read_rom_func_table(t))
        return false;

    /*
     * Because we are in attach, which can be called multiple times for a device, we *must*
     * free any existing map before rebuilding it. Failure to do so will result in unpredictable behaviour.
     */
    target_mem_map_free(t);
    rp_add_flash(t);
    target_add_ram(t, RP_SRAM_BASE, RP_SRAM_SIZE);

    return true;
}
```

The generic target Flash structure is defined as follows:

```c
typedef struct target_flash target_flash_s;

typedef bool (*flash_prepare_func)(target_flash_s *f);
typedef bool (*flash_erase_func)(target_flash_s *f, target_addr_t addr, size_t len);
typedef bool (*flash_write_func)(target_flash_s *f, target_addr_t dest, const void *src, size_t len);
typedef bool (*flash_done_func)(target_flash_s *f);

typedef struct target_flash {
    target *t;                   /* Target this Flash is attached to */
    target_addr_t start;         /* Start address of Flash */
    size_t length;               /* Flash length */
    size_t blocksize;            /* Erase block size */
    size_t writesize;            /* Write operation size, must be <= blocksize/writebufsize */
    size_t writebufsize;         /* Size of write buffer */
    uint8_t erased;              /* Byte erased state */
    bool ready;                  /* True if flash is in flash mode/prepared */
    flash_prepare_func prepare;  /* Prepare for flash operations */
    flash_erase_func erase;      /* Erase a range of flash */
    flash_write_func write;      /* Write to flash */
    flash_done_func done;        /* Finish flash operations */
    void *buf;                   /* Buffer for flash operations */
    target_addr_t buf_addr_base; /* Address of block this buffer is for */
    target_addr_t buf_addr_low;  /* Address of lowest byte written */
    target_addr_t buf_addr_high; /* Address of highest byte written */
    target_flash_s *next;        /* Next Flash in the list */
};
```

## Skeleton Driver

Below is a skeleton for adding support for a new target. Please note that it is preferred to forward declare the Flash
routines and define them after `*_add_flash` and `*_probe`. Functionally it makes no difference, but this improves
the navigability of the resulting target support.

```c
/* Declare the license you wish to use here */

#include "general.h"
#include "target.h"
#include "target_internal.h"
#include "cortexm.h"

static bool skeleton_flash_erase(target_flash_s *f, target_addr_t addr, size_t len);
static bool skeleton_flash_write(target_flash_s *f, target_addr_t dest, const void *src, size_t len);

static void skeleton_add_flash(target *t)
{
    target_flash_s *f = calloc(1, sizeof(*f));
    if (!f) { /* calloc failed: heap exhaustion */
        DEBUG_WARN("calloc: failed in %s\n", __func__);
        return;
    }

    f->start = SKELETON_FLASH_BASE;
    f->length = SKELETON_FLASH_SIZE;
    f->blocksize = SKELETON_BLOCKSIZE;
    f->erase = skeleton_flash_erase;
    f->write = skeleton_flash_write;
    f->erased = 0xffU;
    target_add_flash(t, f);
}

bool skeleton_probe(target *t)
{
    /* Positively identify the target device somehow */
    if (target_mem_read32(t, SKELETON_DEVID_ADDR) != SKELETON_DEVID)
        return false;

    t->driver = "skeleton partno";
    /* Add RAM mappings */
    target_add_ram(t, SKELETON_RAM_BASE, SKELETON_RAM_SIZE);
    /* Add Flash mappings */
    skeleton_add_flash(t);
    return true;
}

static bool skeleton_flash_erase(target_flash_s *f, target_addr_t addr, size_t len)
{
    [...]
}

static bool skeleton_flash_write(target_flash_s *f, target_addr_t dest, const void *src, size_t len)
{
    [...]
}
```

In addition to this, you *must* declare your new probe routine in
[`target/target_probe.h`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/target_probe.h),
and also define a weak linked stub for it in
[`target/target_probe.c`](https://github.com/blackmagic-debug/blackmagic/blob/main/src/target/target_probe.c)

The existing stubs should serve as a decent example for how to do this.

If you wish your new target support to provide functionality like mass erase, there are members in the target structure
such as `t->mass_erase` specifically for this and should be populated in your probe routine.
Similarly, if you wish to add custom commands for your target, you need to build a `command_s` structure array at the top of your target support implementation and register it in the probe routine with `target_add_commands()`.
An example of how to define this custom command block follows:

```c
const struct command_s stm32f1_cmd_list[] = {
    {"option", stm32f1_cmd_option, "Manipulate option bytes"},
    {NULL, NULL, NULL},
};
```

An example registration call has this form: `target_add_commands(t, stm32f1_cmd_list, t->driver);`
