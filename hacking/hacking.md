# Firmware Hacking

The Black Magic Debug firmware is under the GPLv3 open-source license, all contributions to the project
should be either GPLv3, BSD-3-Clause or MIT licenses.

Any contributed hardware designs found in the
[hardware repository](https://github.com/blackmagic-debug/blackmagic-hardware/) is under the CC-BY-SA license.

Building the firmware requires an arm-none-eabi compiler of some sort. Recomended is the official
[ARM GNU Toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads).

## Getting the project source

The project resides in a [GitHub git repository](https://github.com/blackmagic-debug/blackmagic)

Clone this repository (or fork and clone) using your desired method. Typically:

```sh
git clone https://github.com/blackmagic-debug/blackmagic
```

## Compiling for the native hardware

For the native hardware, there are 5 pre-made configurations you can pick from, and the generic configuration
which can then be customised as you wish. The 5 configurations are as follows:

* `native.ini` - Baseline configuration with support for ARM Cortex-M architecture parts. This includes the
  target support for NXP LPC family parts, the nRF series', NXP's Kinetis and i.MXRT parts, RPi Foundation's
  MCUs (ARM parts only), Atmel's ATSAM parts, ST's parts and TI's Stellaris/Tiva-C parts.
* `native-remote.ini` - A special configuration which only includes the remote protocol and acceleration
  components with absolutely no target support enabled. This is designed for use with BMDA exclusively.
* `native-riscv.ini` - A special RISC-V configuration profile which contains only target and architecture
  support for RISC-V devices.
* `native-st-clones.ini` - A special configuration which supports only ST's parts and their clones. This is
  intended for users who are dealing only with ST's parts or their clones. This includes support for parts
  from Artery Tek, GigaDevice, WinChipHead, MindMotion, Puya and HDSC.
* `native-uncommon.ini` - A configuration of all the uncommon parts for all ARM Cortex architectures. This
  includes support for Energy Micro's parts, Renesas parts, Xilinx's Zynq, and Ambiq's Apollo3.

We will use the native.ini configuration in the example build below. We recomend using version 12.2.Rel1 of the
[ARM GNU Toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads) to build the firmware.
To start, we need to create a build directory from a configuration with Meson and then ask Meson to run the build:

```sh
meson setup build --cross-file=cross-file/native.ini
meson compile -C build
```

This will result in the following binary files in the build directory:

* `blackmagic_native_firmware.elf` - ELF binary of the Black Magic debug probe.
* `blackmagic_native_firmware.bin` - Flat binary of the Black Magic debug probe, load at `0x8002000`.

If you need the bootloader as well, then `cd build` and run `ninja boot-bin` which will compile the
bootloader and generate a .bin file for it for use with provisioning tools. This results in two files:

* `blackmagic_native_bootloader.elf` - ELF binary of the Black Magic DFU bootloader.
* `blackmagic_native_bootloader.bin` - Flat binary of the DFU bootloader, load at `0x8000000`.

## Alternative Hardware

A number of users have contributed alternative hardware designs that are compatible with the native firmware.
Some of these designs are in the
[hardware repo](https://github.com/blackmagic-debug/blackmagic-hardware/tree/master/contrib). Check the
`README.md` files for details. For instance, to compile a BMP for an ST-Link v2 to run as alternative to the
ST firmware, compile:

```bash
make PROBE_HOST=stlink ST_BOOTLOADER=1
```

## Building on Windows

Sid Price wrote a detailed step by step guide describing
[how to set up CygWin and compile the Black Magic Probe firmware](http://www.sidprice.com/2018/05/23/cortex-m-debugging-probe/).

### Compiling as a desktop program

The Black Magic Debug project can also be compiled as a desktop program named Black Magic Debug App.

Compile the application with the command:

```bash
make PROBE_HOST=hosted
```

## Enabling DEBUG() messages

Easiest way is to compile a PC-hosted BMP. Run blackmagic -v 1 so that all infos are printed on the controlling
terminal. Argument to -v is a bitmask, with -v 31 very verbose. If you do not succeed in compiling PC-hosted,
use following steps as a last resort to compile in the debug messages when building the firmware:

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

Exit the screen session by type Crtl-A + Ctrl-\\.

## Updating firmware

Follow instructions in [Firmware Upgrade Section](/upgrade.md).
