# Firmware Hacking

The Black Magic Debug firmware is under the GPLv3 open-source license, all contributions to the project should be either GPLv3 or compatible.

Any contributed hardware designs found in the [hardware repository](https://github.com/blackmagic-debug/blackmagic-hardware/) is under the CC-BY-SA license.

## Getting the project source

The project resides in a [GitHub git repository](https://github.com/blackmagic-debug/blackmagic)

Clone this repository (or fork and clone) using your desired method. Typically:

```bash
git clone --recursive https://github.com/blackmagic-debug/blackmagic.git
```

The project uses [libopencm3](http://www.libopencm3.org/), which is included as a git submodule. If you don't provide the `--recursive` parameter above you will have to initialize and check out locm3 as a submodule:

```bash
cd /path/to/blackmagic
git submodule init
git submodule update
```

## Compiling for the native hardware

To build the firmware for the standard hardware platform run `make` in the
top-level directory.  You will require a GCC cross compiler for ARM Cortex-M3
targets. A good option is [gcc-arm-embedded](https://developer.arm.com/downloads/-/gnu-rm).
The default makefile assumes the target prefix is `arm-none-eabi-`. Then only

```bash
make
```

is needded. If your compilers uses some other prefix,  you can override this
on the command line like e.g.:

```bash
make CROSS_COMPILE=arm-cortexm3-eabi-
```

This will result in the following binary files:

* `blackmagic.elf` - ELF binary of the Black Magic debug probe.
* `blackmagic.bin` - Flat binary of the Black Magic debug probe, load at `0x8002000`.
* `blackmagic_dfu.elf` - ELF binary of the Black Magic DFU bootloader.
* `blackmagic_dfu.bin` - Flat binary of the DFU bootloader, load at `0x8000000`.

## Alternative Hardware

A number of users have contributed alternative hardware designs that are compatible with the native firmware.
Some of these designs are in the [hardware repo](https://github.com/blackmagic-debug/blackmagic-hardware/tree/master/contrib). Check the `README.md` files for details. For instance, to compile a BMP for an ST-Link v2 to run as alternative to the ST firmware, compile:

```bash
make PROBE_HOST=stlink ST_BOOTLOADER=1
```

## Building on Windows

Sid Price wrote a detailed step by step guide describing [how to set up CygWin and compile the Black Magic Probe firmware](http://www.sidprice.com/2018/05/23/cortex-m-debugging-probe/).

### Compiling as a desktop program

The Black Magic Debug project can also be compiled as a desktop program named Black Magic Debug App.

Compile the application with the command:

```bash
make PROBE_HOST=hosted
```

## Enabling DEBUG() messages

Easiest way is to compile a PC-hosted BMP. Run blackmagic -v 1 so that all infos are printed on the controlling terminal. Argument to -v is a bitmask, with -v 31 very verbose. If you do not succeed in compiling PC-hosted, use following steps as a last resort to compile in the debug messages when building the firmware:

```bash
make ENABLE_DEBUG=1
```

Then enable debug messages in gdb with the new command

```gdb
monitor debug_bmp enable
```

The debug messages appear on the debug UART. On a BMP the USB UART device is used.

```bash
screen /dev/ttyACM2 115200
```

Exit the screen session by type crt-a + ctl-\\.

## Updating firmware

Follow instructions in [Firmware Upgrade Section](/firmware-upgrade.md).
