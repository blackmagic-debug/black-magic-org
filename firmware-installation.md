# Firmware Installation

The Black Magic Firmware can be installed on hardware that did not previously contain Black Magic Firmware. We refer to this as a clean install.

If your board already has the Black Magic Firmware installed, please refer to [Firmware Upgrade](./firmware-upgrade.md) to upgrade your Black Magic Probe with the latest firmware.

To perform a clean install, multiple types of hardware can be used in combination with different software utilities. This section lists the options to perform a clean install by hardware, to enable you to select the right software utility for the hardware you have at hand. The options covered are:
- USB to Serial/UART/TTL converter, i.e. FTDI interface, if the targeted hardware has the built-in ST serial UART bootloader
- ST-Link
- Black Magic Probe

## USB to serial/UART/TTL converter, i.e. FTDI interface

```{note}
To use this method, the target hardware must have the ST serial UART bootloader.
```

For instance an USB to serial UART converter with [FTDI FT232RL](https://ftdichip.com/products/ft232rl/) can be used.

Connect the GND, TXD, RXD and 3V3 pins of the converter to the pins of the target hardware. Note that TxD of the converter shall be connected to RxD of the target hardware, and RxD of the converter shall be connected to TxD of the target hardware.

As flashing utility, use either:
- stm32loader
- stm32flash

### stm32loader

Download [stm32loader](https://github.com/jsnyder/stm32loader).

To flash using `stm32loader` run the command:

```bash
python ./stm32loader -p /dev/tty.usbserial -e -w -v src/blackmagic.bin
```

This will pre-erase flash, write `blackmagic.bin` to the flash on the device using the port `/dev/tty.usbserial`, and then perform a verification after writing is finished. Please udate the port to the actual port of your USB to serial converter.

<!-- 
FIXME: validate if this command works
-->

```{note}
This command has not been validated by the author of this section.
```

### stm32flash

Install [stm32flash](https://sourceforge.net/p/stm32flash/wiki/Home/).

To flash using `stm32flash` run the command:

```bash
./stm32flash -w blackmagic.bin -S 0x8000000 -v -g 0x0 /dev/tty.usbserial
```

<!-- 
FIXME: validate if this command works
-->

```{note}
This command has not been validated by the author of this section.
```

## ST-Link

For instance an original [ST-Link/V2](https://www.st.com/en/development-tools/st-link-v2.html) or an [ST-Link clone](https://stm32-base.org/boards/Debugger-STM32F101C8T6-STLINKV2) can be used.

Connect the GND, SWDIO, SWCLK and 3V3 pins of the ST-Link to the same pins of the target hardware which shall be flashed with the Black Magic Firmware.

As flashing utility, use either:
- stlink
- pystlink

### stlink

[stlink](https://github.com/stlink-org/stlink) is an open source version of the STMicroelectronics STLINK Tools.

For a board with flash (rom) of 128 kB, run the command:

```bash
st-flash erase
st-flash --flash=128k write blackmagic.bin 0x8000000
```

Determine the flash size of the target hardware. The flash size is stored in the linker script (.ld) of the [platform](https://github.com/blackmagic-debug/blackmagic/tree/main/src/platforms) of the target hardware. Adapt the flash size in the command accordingly.

### pystlink

[pystlink](https://github.com/pavelrevak/pystlink) is a python utility to interact with an ST-Link.

For 
```bash
pystlink flash:erase:verify:0x8000000:blackmagic.bin
```

<!-- 
FIXME: validate if this command works
-->

```{note}
This command has not been validated by the author of this section.
This utility does not support ST-Link v1.
```

## Black Magic Probe

If you already have a Black Magic Probe, you can turn another device into a Black Magic Probe using SWD (Serial Wire Debug) or JTAG (Joint Test Action Group).

To use SWD, connect the GND, SWDIO, SWCLK and 3V3 pins of the Black Magic Probe to the same pins of target hardware and run the following commands:

```
arm-none-eabi-gdb blackmagic.bin
(gdb) target extended-remote /dev/ttyACM0
(gdb) monitor swdp_scan
(gdb) attach 1
(gdb) load
(gdb) compare-sections
```

Please find further details how to use the Black Magic Probe and operating system specific information on the [Getting started](./getting-started.md) and [GDB commands](./usage/gdb-commands.md) sections.
