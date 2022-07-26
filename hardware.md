# Supported Hardware

Black Magic Probe firmware can be compiled for many different target platforms. Here is a short list with descriptions of different targets.

## Native Hardware

The following is a list of official hardware supported by the Native target that is the default compilation target of Black Magic Probe firmware.  All revisions of the native hardware work with the same firmware binary.

### Black Magic Probe V2.3 (BMP23)

![](_assets/bmp23-top.jpg)
![](_assets/bmp23-bottom.jpg)

**Status** Active

**Schematic** TODO

New slightly larger form factor than previous versions to accommodate the larger TQFP MCU package, AUX connector and additional flash chip. Following is a list of the main differences to the predecessor relevant to an end user.

* ...
* ...

### Black Magic Probe Mini V2.1 (BMP21)

TODO: Add photos

**Status** Legacy (not in production)

**Source** [Vendors](index.md#getting-hardware)

**Schematic** [bmpm_v2_1c_schematic.pdf](_assets/bmpm_v2_1c_schematic.pdf)  
**Schematic** [bmpm_v2_1e_schematic.pdf](_assets/bmpm_v2_1e_schematic.pdf)

Same form factor as the predecessor BMPM2. Following is a list of main differences to the predecessor relevant to an end user.

* Replaces the TXS0108 bidirectional level shifter with dual supply 74LVC2T45 bus transceivers. This improves the line drive strength and expands the target voltage range to 1.8V-5V (previous design was limited to 1.8V-3.3V)
* Dedicated reset line drive MOSFET circuitry with 10k pull-up ensuring good open-drain RST line drive with monitoring.
* Exposed the BMP side SWD lines on dedicated pads, allowing for easier programming and debugging of the probe firmware. It is much easier now to program and debug the BMP firmware using a second BMP. The pinout is compatible with the [SWD adapter by 1Bitsquared](https://1bitsquared.com/products/jtag-swd-adapter).
* Increased LED distance from each other for better visual separation.
* (V2.1e revision) Added a normally open jumper to allow the connection of the `TRACESWO` signal to `UART1_RX` on pin `PB7`. This pin is also the highest order bit of the hardware version. Because of that all BMPM V2.1e have the hardware version stored as a user `Data0` option byte at address `0x1FFFF804`. The hardware version corresponding to V2.1e is `0x04`. The firmware that implements the use the uart SWO decoding should check the presence of the hardware version in the option bytes first. (this feature is not yet supported in current blackmagic probe firmware)

**3D Printed Cases**
* Michael McAvoy's Black Magic Probe Case - With Fins: [Thingverse](https://www.thingiverse.com/thing:2387688), [Shapeways](https://www.shapeways.com/product/ZCZRTYJJ9/case-black-magic-probe-with-fins) 
* Michael McAvoy's Black Magic Probe Case - Flat: [Thingverse](https://www.thingiverse.com/thing:2401662), [Shapeways](https://www.shapeways.com/product/JG6NTERVG/case-black-magic-probe-flat)

### Black Magic Probe Mini V2.0 (BMPM2)

![](_assets/bmpm2-black-final-top.jpg)
![](_assets/bmpm2-black-final-bottom.jpg)

**Status** Legacy (not in production)

**Source** [Vendors](index.md#getting-hardware)

**Schematic** [bmpm_v2_0f_schematic.pdf](_assets/bmpm_v2_0f_schematic.pdf)

Same form factor as the predecessor BMPM1. Following is a list of main differences to the predecessor.

* Adds TXS0108 level shifter for wider range of targets. This will add support for low voltage targets that run on 1.8V.
* Uses two MOSFET to prevent powering the BMPM in reverse through the MOSFET body diodes.
* Uses USB Micro connector as it is by now more wide spread than USB Mini.

### Black Magic Probe Mini V1.0 (BMPM1)

![](_assets/bmpm1-top.jpg)
![](_assets/bmpm1-bottom.jpg)

**Status** Legacy (not in production)

**Source** [Getting Hardware](index.md#getting-hardware)

**Schematic** [blackmagic_mini.pdf](_assets/blackmagic_mini.pdf)

Small version of the Black Magic Probe also known as BMPM1. The form factor was inspired by the Floss JTAG FTDI based adapter. The board offers an ARM Cortex 0.05" 10Pin connector on the top of the board and a Molex Picoblade 4Pin UART serial connector on the back of the board.

The board has a MOSFET to switch 3.3V power supply to the target in place of the jumper on the original Black Magic Probe.

This board does not buffer the JTAG or serial pins in any way, they are connected directly to the STM32.

### Black Magic Probe

![](_assets/bmp1-top.jpg)

**Status** Legacy (not in production)

**Schematic** [blackmagic-1.0.pdf](_assets/blackmagic-1.0.pdf)

The original first hardware. Offers a legacy ARM JTAG 0.1" 20Pin connector. Some of the pins of the 20Pin connector carry TX and RX of a serial interface. This makes the connector not 100% compatible to a default 20Pin JTAG connector.

The board has a physical jumper to switch 3.3V power supply to the target.

JTAG IO is buffered through a TXS0108 Texas Instruments bidirectional level shifter.  UART signals are connected directy to the STM32.

## FTDI target

It is possible to run the Black Magic Probe firmware on your PC and have it bit bang using a USB attached FTDI MPSSE capable adapter. Programming speed is a little slower, but BMP development may be faster due to no firmware upload needed and the inherent debugging messages on the starting console. 

## ST Link

You can compile the firmware for an ST Link debugger. These are often included on ST Discovery and Nucleo evaluation boards. You can replace [the ST Link firmware on your discovery board](http://esden.net/2014/12/29/black-magic-discovery/) with Black Magic Probe firmware. Usually this leads to more stable operation and easier use than the ST tools. There are several tutorials for how to do it even if you don't have a JTAG adapter yet and no way to bootstrap. :)

For a generic STM32F103 board, look if the swlink platform can handle it. Swlink reuses the SWD pins.
You can also follow [these](https://medium.com/@paramaggarwal/converting-an-stm32f103-board-to-a-black-magic-probe-c013cf2cc38c#.btn6lnwqe) instructions for a solution to not reuse the SWD pins.

## ST Link V2

Restoring StlinkV2 BMP support with recent original ST firmware is a work in progress at the moment, according to the [issue #504](https://github.com/blacksphere/blackmagic/issues/504#issuecomment-525399540).

## F4 Discovery

You can run the Black Magic Probe firmware on the "target" processor of an ST F4 discovery board. This among others useful if you want to bootstrap your F4 Discovery board ST Link programmer without having any other means of programming it.

## SW Link

This target is the programmer integrated on the STM8S Discovery board.

## Bluepill/Blackpill V1 minimal development boards

The swlink platform can also be used for development boards with header accessible SWD pins. Swlink firmware remaps SWD debug pins as bit-bang SWD output. Full JTAG and more infrastructure is accessible on the header rows.

## Launchpad ICDI

This target is the programmer integrated on the TI Launchpad board.
