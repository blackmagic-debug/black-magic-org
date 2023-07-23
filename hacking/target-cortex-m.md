# Cortex-M Targets

Developing a new target driver for the Black Magic Probe is straight forward on many ARM platforms.
This page collects some notes taken while developing drivers.
As a convention, source files are referenced from the top level directory of the repository with a dot (.)
so the directory for target files is `./src/target`.

## Hooking your target support into the system

Your driver will typically be written in a single source file which should be in the `./src/target` directory
and named after the family you wish to add support for.
For example, support for the ST Micro STM32F1 series are in the file `src/target/stm32f1.c`

This file will define exactly one globally visible function named `<target>_probe` with the C prototype of
`bool <target>_probe(target *t);`. Any other functions or data you declare in this file should be declared
`static` to avoid name collisions with other target implementations.

You will modify four files to make your target part of the BMP build, the first is the make file, `./src/Makefile`
which should have your source added to the `SRC =` definition.The second is `./src/target/cortexm.c` where you will
add a line of the form `PROBE(<target>_probe);` in the sequence of other calls to probe functions.
The third file will be `./src/target/target_probe.h` where you will add a prototype for your probe function.
Finally `./src/target/target_probe.c` where you will use the `TARGET_PROBE_WEAK_NOP` macro to add a weak linked
stub for your probe function.

A typical target driver will be updates to these four files and your new `./src/target/<target>.c` file.

## Setting up a Development Environment

You will need three things for a functioning development environment: GNU Make, bmputil, and a compiler.
If you wish to interface with the target serial port having built the firmware with debugging enabled,
then you will also need to install a serial program such as minicom or screen.

We advise using the official ARM toolchain even over any distribution toolchain you might be able to install
from a package manager. You can acquire the official toolchain in one of two flavours - the older
[GNU Arm Embedded Toolchain](https://developer.arm.com/downloads/-/gnu-rm) flavour,
and the newer [Arm GNU Toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads) flavour.
Both should work, however the project authors currently test with and use the older toolchain flavour.

The Black Magic Firmware supports two kinds of debugging, however, using them may require disabling some target
support to free up enough Flash space for the extra code and data needed. The first kind of debugging uses
debug statements littered through the code and the secondary serial connection. You can enable this by passing
`ENABLE_DEBUG` to the build, as in `make ENABLE_DEBUG=1`. The second kind of debugging is for Black Magic Inception
and involves switching to debug optimisations and enabling debug information generation in the build. This can be
achieved by passing `OPT_FLAGS` to the build, as in `make OPT_FLAGS="-Og -g"` -- these approaches are not mutually
exclusive of each other and can both be enabled at the same time by combining the make arguments:
`make ENABLE_DEBUG=1 OPT_FLAGS="-Og -g"`.

If instead of trying to do debug builds to fit in Flash you need a more general approach and **do not** need to debug
the JTAG or SWD bitbanging routines, you can alternatively use BMDA (Black Magic Debug App) which carries none
of the restrictions of the firmware. To do this, simply build with the following options to Make:
`make PROBE_HOST=hosted ENABLE_DEBUG=1 ASAN=1 OPT_FLAGS="-Og -g"`.
Even though `ASAN=1` is optional, it is *strongly* advised you enable this when doing development on BMP.

With the firmware variant, once you have a debug-enabled build you can connect to the BMP's non-GDB serial port
to get the additional debug messages. The extra messages are only enabled if you issue `monitor debug_bmp enable`
(or a shortening such as `mon debug en`) from in GDB after connecting in to your BMP as normal. Alternatively, you
can set up Black Magic Inception, detailed in the following section.

## Black Magic Inception

There are a couple of generations of this. The older generation (v2.0 hardware and older) uses the auxiliary
serial connector on BMP which happens to be directly attached to the SWD pins of the processor on BMP, and
the newer generation (v2.1 hardware and newer) has a dedicated pinheader connector for the purpose.

### Debugging the older generation

With the older generation (v2.0 hardware and older), you can debug a new BMP target with a second BMP as
the first BMP's debugger. When debugging with another BMP device the debug messages who up in the second
BMP devices gdb session as it uses semi-hosting to direct them out.

To set up one BMP debugging a second BMP is not particularly difficult but it can be unwieldy. Start with the
BMP that is going to run the new target code, connect its SWD, SCLK, tPWR/vRef, and GND pins on the PicoBlade
connector on the rear side of the board, to the second BMP unit. If you have the mini-10 to JTAG adapter board
and a PicoBlade serial port cable, you can push the connectors on the serial port cable on to the pins on the
10-pin debug target connector.

The connection sequence from the PicoBlade
(with the [1BitSquared cable](https://1bitsquared.com/products/black-magic-01in-pin-header-serial-cable))
to the 10-pin debug target connector is:

* PicoBlade Pin 1 (red) => 10-pin connector pin 1
* PicoBlade Pin 2 (green) => 10-pin connector pin 4
* PicoBlade Pin 3 (purple) => 10-pin connector pin 2
* PicoBlade Pin 4 (black) => 10-pin connector pin 3 or 5

For more information on what connections are being made here, see the [pinout glossary](../knowledge/pinouts.md).

If you are using an older generation BMP that uses the 20-pin ARM debug connector, you will instead want to connect
the green wire to pin 9 of the JTAG connector, purple to pin 7, and black to any even pin on the JTAG connector
other than pin 2.

If you set one BMP to debug another, then you can load firmware using GDB into the BMP. If you are simply building
the firmware and evaluating its function by reading the output from `DEBUG_*` statements then you will need to use
`bmputil` or `dfu-util` to update the firmware. (see [Updating the Firmware](../upgrade.md)).

### Debugging newer generations

With newer generation (v2.1 hardware and newer) BMPs, there is a dedicated set of 0.05" (1.27mm) pin headers
provided to allow connecting one BMP to another using a
[1BitSquared JTAG SWD adaptor](https://1bitsquared.com/collections/accessories/products/jtag-swd-adapter)
or the 5-pin variant of this which includes the ~RST signal too.

To use this, simply plug the adaptor in as labeled on the BMP you want to debug, connect a 10-pin IDC cable between it
and the second BMP you are using as the first's debugger, and proceed as you would on the older generation boards.

## Implementing the Driver

The first step in implementing the driver is to implement the `<target>_probe` function. This function has three very important things to do:

  1. it has to identify whether or not you are talking to a target you recognize
  2. it has to create a memory map describing that target's resources
  3. it has to initialize the function pointers in the target structure to point to routines that can erase and program the target's on board flash memory.

The functions `target_mem_read32` and `target_mem_write32` will read and write long words in the target's address space. Generally the debug unit has access to all of the address space unless the chip has been put into a protected mode. It is useful for your target driver to provide a target specific command for removing protected mode (see **Custom Commands** below). The register that the probe code will read on Cortex-M processors is called the chip ID register or CHIPID. Where it is in the address space will be documented in the data sheet or reference manual for the chip.

That section will also typically document what memory configurations are available based on information contained in the CHIPID register. Your probe function will use this information to confirm that the target is something you recognize, and then decode the parameters in register according to the datasheet to identify FLASH address location and size, and RAM address location and size.

### Adding RAM

For each discontinuous region of RAM your code will call `target_add_ram` with the pointer to the target structure, the address of the RAM chunk, and its size in bytes. Each time you call this function, an additional chunk of RAM is added to the gdb memory map for the target.

### Adding Flash

As you did with RAM, you will need to tell gdb about the size(s) and addresses of programmable read-only memory (Flash) on the device. Because every device tends to have a slightly different way of programming things, adding a segment of Flash memory means adding the address and size of Flash, and then adding pointers to functions that can erase and write the Flash (reading is handled by just reading memory).

Some Flash memories can only be erased all at once, some can be erased in variable sized sectors, and others can be erased in pages of fixed size. A *region* is Flash at a given address, and of a given length, that has the same erase and programming requirements.

You describe these in your target driver by populating a `target_flash` structure. This structure has members for the start, length, and blocksize of the Flash you are describing. The blocksize is the smallest individual unit of Flash that can be **erased**. So if your Flash says that it must be erased in 8K byte segments, then your blocksize is 8192. If your Flash can be erased a page at a time and a page is 256 bytes, then your blocksize is 256. You finish that off by adding a function call to a local, statically defined, function that can erase Flash. It will be passed an address and a length which is compatible with your stated blocksize when your Flash needs to be erased.

The next section of this structure is for writing. It is simplest to set the write function call to the internal BMP function called `target_flash_write_buffered`. For the done function you set it to the internal function `target_flash_done_buffered`. Now you set the value `bufsize` to be the "writable unit" of Flash (so one sector or one page depending on the Flash) and the field `erased` to the state Flash is in when it is erased (typically 0xff).
Finally you will add a local, statically defined, function call which can write one buffer's worth of data to the Flash. That function will be passed an address on a buffer boundary, and a buffer's worth of data to write.

Then you will add the Flash segment by calling `target_add_flash` with the target pointer and a pointer to your `target_flash` structure.

### Custom Commands

You have the option to add some additional commands to the target. These will become part of the acceptable commands to the 'mon' command in gdb. So if you added a new command `erase-protection`, typing `mon erase-protection` would invoke it.

Commands are added using a `command_s` structure of three pointers, the first is the string for the command, the second pointer is a pointer to the local function that implements that command, and the third is a help string that is printed when someone types `mon help <your-command>`.

When invoked, your command function will be passed an argument count and an argument vector (just like `main` in a C program) that you can take arguments from and use in your command. If you don't recognize the arguments you can use `tc_printf` to return a usage string to the user.

If the command fails you should return `false` and if it succeeds you should return `true`.

## Special Handling

If you have recognized the target, filled out the `target_s` structure for it, populated the memory map and potentially added a new command or two, the final steps are to set the name of your driver in the `driver` string pointer of the target structure and decide if you need any special reset handling. Special reset handling comes in two forms, avoiding system reset and extra care after reset.

Some targets can lose debugger state and detach if you assert system reset. This is not supposed to happen according to the ARM documents but it has been known to be an issue. You can tell the generic Cortex M driver not to use sRST by setting an option `CORTEXM_TOPT_INHIBIT_SRST` in the `target_options` field of the target structure. Normally when the BMP is trying to reset the target it will call `platform_srst_set_val` with a `true` state followed by a `false` state to assert reset. If you find this causes your target to detach or get lost, use the `CORTEXM_TOPT_INHIBIT_SRST` option to tell the generic driver not to do that. You need only set the option in your `target_options` during the probe function.

Another situation that can arise is that asserting reset causes other things to happen on the chip that will prevent it from continuing. The Atmel SAM series tends to have this sort of problem. If your platform needs some extra help to get completely out of reset you can define a function that will do that work and put a pointer to it in the field `extended_reset`. If this field is non-NULL, the Cortex M platform driver will call it after it has issued a SYSRESETREQ and before it starts polling the target to see if it has released from reset.

## Getting from Zero to Sixty

When you start this process you will have a data sheet, a fresh build the BMP firmware, and a lot of questions. Bring up strategy for a new target works well if you proceed in the following way;

  1. **Verify you can identify your target** -- When you run your firmware for the first time attached to your target you should be able to type `mon swdp_scan` and see your driver name come back as the available target. If you added `DEBUG` statements to your poll function they would appear on the debug terminal (either the second serial port or the debugging BMP's gdb session).
  2. **Verify you can Erase and Program Flash** -- This is a bit trickier, one technique is to create a simple C program with some `const unint8_t` arrays that contain recognizable data in them. Loading that file from gdb will tell the BMP to flash it into your target and you can use the gdb memory inspection tools to verify it arrived intact. A useful gdb command here is `compare-sections` which will compare the .elf file with what gdb can see in memory. If they don't match your flash programming is *not working*. You can dump out memory to a file using the gdb command `dump bin memory <filename> addr1 addr2` so the first 8K of memory might be `dump bin mem 8k-mem-dump.bin 0x0 0x2000`.
  3. **Verify you can start and interrupt a running program.** -- At this point it is quite useful to have a minimal "blinker" program that will toggle and LED or GPIO pin that you can monitor on an oscilloscope ready to run. Load this program with the working flash functions and tell gdb to run it. It should start and the GPIO should begin toggling, then use ^C to interrupt and verify the program stops and gdb gives you the source line where the code was interrupted.
  4. **Verify you can set a breakpoint and single step.** -- If you have a runnable "Blinky" program then you can set a breakpoint on the `main` function. Run the program and confirm that it stops when it hits the break point. Use the `step` command to single step forward and then the `cont` command to resume execution.

## Summary

Implementation of a new Cortex-M target driver requires that you write code that can positively identify that your target is being talked to, erase and program your target's FLASH memory, manage resets so that the debugger can function across system resets, and any special commands that might be needed for target-specific features. You can debug the development through either `printf` like features of the DEBUG statements or by using another BMP to run gdb on the firmware in the first one. Using a simple "blinky" type program and some recognizable data structures you can verify the basic functions of gdb with respect to your target.

Once you've done that you have a new target driver for the BMP.
