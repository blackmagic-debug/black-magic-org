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

There are a number of platforms that have been contributed by the community to the main repository. You can
make use of them by subsituting out `native.ini` in the instructions for native with one of the following:

* `96b_carbon.ini` - Configuration for [96Boards' Carbon](https://www.96boards.org/product/carbon/)
* `blackpill-f401cc.ini` - Configuration for the WeAct Studio
  [Black Pill F401CC](https://github.com/WeActStudio/WeActStudio.MiniSTM32F4x1)
* `blackpill-f401ce.ini` - Configuration for the WeAct Studio
  [Black Pill F401CE](https://github.com/WeActStudio/WeActStudio.MiniSTM32F4x1)
* `blackpill-f411ce.ini` - Configuration for the WeAct Studio
  [Black Pill F411CE](https://github.com/WeActStudio/WeActStudio.MiniSTM32F4x1)
* `bluepill.ini` - Configuration for the WeAct Studio Blue Pill
* `ctxlink.ini` - Configuration for [Sid Price's ctxLink](https://www.crowdsupply.com/sid-price/ctxlink)
* `f072.ini` - Configuration for STM32F072's
* `f3.ini` - Configuration for STM32F3's
* `f4discovery.ini` - Configuration for ST's
  [STM32F4 Discovery](https://www.st.com/en/evaluation-tools/stm32f4discovery.html) board
* `hydrabus.ini` - Configuration for [HydraBus](https://hydrabus.com/)
* `launchpad-icdi.ini` - Configuration for the ICDI on TI's Launchpad boards
* `stlink.ini` - Configuration for ST-Link v2, and ST-Link v2.1 adaptors
* `stlinkv3.ini` - Configuration for ST-Link v3
* `swlink.ini` - Configuration for ST-Link and Blue Pill (read the README.md before using this)

For the ST-Link platform, the default is for the project bootloader to be disabled so it can be used with
ST's own and `stlink-tool`. If you wish to use the project's bootloader and replace ST's, then pass
`-Dbmd_bootloader=true` on the end of the `meson setup` line and follow the bootloader build instructions
as well to generate the files to use to start over on the ST-Link probe.

## Building on Windows

For windows-specific instructions, please use the [Compiling on Windows](/knowledge/compiling-windows.md) guide.

### Compiling as a host computer program

Black Magic Debug App (BMDA) is compiled by default when building the firwmare if the dependencies for it
can be resolved. If you wish to build just BMDA on its own however, you can run the following two Meson
commands:

```sh
meson setup build
meson compile -C build
```

This will generate one file in the build directory - `blackmagic`. This is the BMDA executable.

## Enabling debug messages

All debug messages are compiled into BMDA, always. To enable more of the diagnostic output, use the `-v` flag.
This flag is a bitmask with a maximum value of 63. There are 6 sets of diagnostics that can be enabled:

* 1  - INFO: General informational diagnostics
* 2  - GDB: GDB remote protocol diagnostics
* 4  - TARGET: Target-specific diagnostics
* 8  - PROTO: Target debug protocol diagnostics
* 16 - PROBE: Probe protocol diagnostics
* 32 - WIRE: USB communication with probe ("wire-level") diagnostics

There are two additional always-enabled levels for BMDA - `ERROR` and `WARN`.

For the firmware, pass `-Ddebug_output=true` to the end of the `meson setup` line and build. This will include
some of the levels into the firmware such as ERROR, WARN, and INFO. You can then enable the messages at runtime
with the `monitor` command this adds:

```gdb
monitor debug_bmp enable
```

The debug messages appear on the target debug UART. An example of its usage follows below:

```sh
minicom -D /dev/ttyBmpTarg -8
```

To exit `minicom`, type Ctrl + A then Q and answer "Yes" to the question about leaving without reset by typing
Enter. This will return you to the original console.

## Updating firmware

Follow instructions in [Firmware Upgrade Section](/upgrade.md).
