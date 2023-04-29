# FAQ

## What targets are currently supported?

The Black Magic probe currently supports ARMv6-M and ARMv7-M architecture targets, specifically Cortex-M0, Cortex-M3 and Cortex-M4.
Any device with these cores should work with possibly the exception flash memory programming.

Memory map and flash programming are supported for these specific implementations:
* `efm32.c`: Silicon Labs EFM32, EZR32
* `kinetis.c`: Freescale Kinetis KL25, KL27, KL02
* `lmi.c`: Texas Instruments: LM3S, TM4C
* `lpc11xx.c`: NXP LPC8xx, LPC11xx
* `lpc15xx.c`: NXP LPC15xx
* `lpc17xx.c`:  NXP LPC17xx
* `lpc43xx.c`: NXP LPC43xx
* `lpc546xx.c`: NXP LPC546
* `msp432.c`: MSP432P401
* `nrf51.c`: Nordic nRF51, nRF52
* `nxpke04.c`: Kinetis KE04
* `renesas.c`: Renesas RA, R7FAxxx
* `rp.c`: Raspberry RP20240
* `sam3x.c`: Atmel SAM3N, SAM3X, SAM3S, SAM3U, SAM4S, SAMx7x
* `sam4l.c`: Atmel SAM4L
* `samd.c`: Atmel SAM D20, D21
* `samdx5x.c`:Atmel SAMD5x/E5x
* `samx5x.c`: Atmel SAMx5xqq
* `stm32f1.c`: ST Microelectronics STM32F0, STM32F1, STM32F3
* `stm32f4.c`: ST Microelectronics STM32F2, STM32F4, STM32F7
* `stm32g0.c`: ST Microelectronics G0
* `stm32h7.c`: ST Microelectronics H7
* `stm32l0.c`: ST Microelectronics STM32L0, STM32L1
* `stm32l4.c`: ST Microelectronics STM32L4, STM32G0, STM32G4

Last Updated: Sep 6, 2022 (Partial update)

As additions happen, you to update the firmware to profit from these additions.
There is experimental support for Cortex-A (ARMv7-A architecture).  This is being used with success on Xilinx Zynq-7000 SoC (Dual-core Cortex-A9) and Raspberry Pi 2 (Quad-core Cortex-A7).


## Where can I get the hardware?

The official Black Magic Probe hardware is available from multiple vendors. An up to date list is kept on the [project main page](index.md#getting-hardware).

## Where can I find the BMP schematics?
 * [Black Magic Probe Mini v2.1](https://github.com/blackmagic-debug/blackmagic/wiki/files/bmpm_v2_1c_schematic.pdf)
 * [Black Magic Probe Mini v2.0](https://github.com/blackmagic-debug/blackmagic/wiki/files/bmpm_v2_0f_schematic.pdf)
 * [Black Magic Probe Mini](https://github.com/blackmagic-debug/blackmagic/wiki/files/blackmagic_mini.pdf)
 * [Original Black Magic Probe](https://github.com/blackmagic-debug/blackmagic/wiki/files/blackmagic-1.0.pdf)

## What are those JTAG/SWD connectors and cables?
The JTAG/SWD connector is [FTSH-105-01-F-DV-K from Samtec](https://www.samtec.com/products/ftsh-105-01-f-dv-k) (Buy: [Digi-key](http://www.digikey.com/product-detail/en/FTSH-105-01-F-DV-K/FTSH-105-01-F-DV-K-ND/2649974), [1BitSquared](https://1bitsquared.com/products/jtag-swd-smd-connector)).

The JTAG/SWD connector is a 0.05" (50mil/1.27mm) pitch, 2 row 10pin connector. The Samtec version is the only one that includes a keying shroud and does not occupy a large space on the PCB. There are other manufacturers that make connectors that can be used too. Here are a few options:
* Amphenol FCI 20021121-00010C4LF unshrouded SMD (Buy: [Digi-key](https://www.digikey.com/product-detail/en/amphenol-fci/20021121-00010C4LF/609-3695-1-ND/2209147))
* Amphenol FCI 20021111-00010T4LF unshrouded TH (Buy: [Digi-key](https://www.digikey.com/product-detail/en/amphenol-fci/20021111-00010T4LF/609-3712-ND/2209072))
* Amphenol FCI 20021521-00010T1LF shrouded SMD (Buy: [Digi-key](https://www.digikey.com/product-detail/en/amphenol-fci/20021521-00010T1LF/609-4054-ND/2414951))
* Amphenol FCI 20021211-00010T1LF shrouded TH (Buy: [Digi-key](https://www.digikey.com/product-detail/en/amphenol-fci/20021211-00010T1LF/20021211-00010T1LF-ND/4244146))
* CNC Tech 3220-10-0300-00 shrouded SMD (Buy: [Digi-key](https://www.digikey.com/product-detail/en/cnc-tech/3220-10-0300-00/1175-1629-ND/3883266))
* CNC Tech 3220-10-0100-00 shrouded TH (Buy: [Digi-key](https://www.digikey.com/product-detail/en/cnc-tech/3220-10-0100-00/1175-1627-ND/3883661))
* And many many more ... 😸

The JTAG/SWD cable is [FFSD-05-D-xx.xx-01-N](https://www.samtec.com/products/ffsd-05-d-06.00-01-n) where the `x` stand for the length of the cable. Common length is 6 inches. (Buy: [Digi-key](https://www.digikey.com/product-detail/en/samtec-inc/FFSD-05-D-06.00-01-N/SAM8218-ND/1106577), [1BitSquared](https://1bitsquared.com/products/jtag-idc-cable))

You can build your own JTAG/SWD ribbon cable using the following materials. (consider just an example there are many manufacturers making 1.27mm pitch IDC crimps and ribbons)
* CNC Tech 3230-10-0103-00 IDC crimp with polarizing key. (Buy: [Digi-key](https://www.digikey.com/product-detail/en/cnc-tech/3230-10-0103-00/1175-1646-ND/3883463))
* 3M 3756/10 0.025" (0.64mm) pitch 10 conductor flat ribbon cable. (Buy: [Digi-key](https://www.digikey.com/product-detail/en/3m/3756-10-100/ME10G-10-ND/5308218))

## What are those UART connectors and cables?

The UART connector is Molex PicoBlade 0532610471. (Buy: [Digi-key](http://www.digikey.com/product-detail/en/0532610471/WM7622CT-ND/699109)).

The UART cable can be built by hand using the following materials:
* Molex PicoBlade 050079-8000 26-28AWG or 50058-8000 28-32AWG crimp sockets. (Buy: [Digi-key](https://www.digikey.com/product-detail/en/molex-llc/0500798000/WM1142CT-ND/467835) [Digi-key](https://www.digikey.com/product-detail/en/molex-llc/50058-8000/WM1775CT-ND/242897))
* Molex PicoBlade 0510210400 housing (Buy: [Digi-key](https://www.digikey.com/product-detail/en/molex-llc/0510210400/WM1722-ND/242844))
* Molex PicoBlade 0638271400 crimp tool (Buy: [Digi-key](https://www.digikey.com/product-detail/en/molex/0638271400/WM15815-ND/6577355)) (Warning: if you don't want to be very frustrated and destroy a lot of crimps skip trying to use cheaper options that claim to be compatible with the PicoBlade crimps, they are not.)
* 26-32AWG wire of your choosing and whatever termination you need on the other side of the cable.

The UART cable can also be built with pre crimped wires:
* [Digi-key](https://www.digikey.com/short/08n0q938) Molex Picoblade pre-crimped cables, you can choose from all kinds of colors as well as doublesided or single sided crimps.
* [1BitSquared](https://1bitsquared.com/products/picoblade-wire-kit) pre-crimped cable assortment

There are also pre made UART cables:
* [1BitSquared](https://1bitsquared.com/products/black-magic-01in-pin-header-serial-cable) UART to 0.1" pin header pigtail cable.
* [1BitSquared](https://1bitsquared.com/products/serial-interface-cable) UART to [Paparazzi UAV](http://paparazziuav.org) autopilot cable.

## Where can I find different JTAG/SWD connectors? (Adapters & Cables)

Many vendors provide adapters allowing easy connection between different JTAG/SWD and UART interfaces. For example [1BitSquared](https://1bitsquared.com/collections/embedded-hardware) offers a wide range of different adapters and cables. There is also a collection of adapter designs that you can find on the [1BitSquared GitHub Page](https://github.com/1bitsquared/1b2-adapter-collection) that you can use as basis for your custom adapter. If there is an adapter missing for your specific application it is usually quite easy to put one together using [KiCad](http://kicad.org/) and order the needed board from [OSHPark](https://oshpark.com/).

## Are binary firmware images available for download?

Automatically built firmware images for the official hardware are [here](https://github.com/blackmagic-debug/blackmagic/releases).

## How can I access memory mapped I/O from GDB?

The peripheral registers are not included in the memory map provided to GDB.
It is suggested that you add the command `set mem inaccessible-by-default off` to
your `.gdbinit` file.  That will allow you to access addresses outside of
the memory map. It will treat anything outside of the memory map as
RAM.

## How do I prevent memory corruption when writing to flash on an LPC MCU?

The first 512 bytes of the address space are mapped to boot ROM by default. Once you write the `SYSMEMREMAP` register (address `0x40048000`) to have a value of 2, those 512 bytes are mapped to flash and all sections will match. The LPC bootloader automatically does this upon detecting valid user code, but the bootloader cannot run while you are holding the chip in reset with a debugger. See section 3.5.1 of the manual. In gdb, you can `set {int}0x40048000 = 2` to achieve the same result.

You can add the following to your `.gdbinit` to set the bit on startup.

```
set mem inaccessible-by-default off
set {int}0x40048000 = 2
```

This solution is known to work on the LPC8xx/LPC11xx families of chips. If you are using something different refer to the reference manual and look for `SYSMEMREMAP` register. If the address differs please add it to this FAQ item or let us know in the [Discord #blackmagic channel](https://discord.gg/P7FYThy) or mailing list. For the discussion of this problem refer to issue [#99](https://github.com/blackmagic-debug/blackmagic/issues/99).

## It's annoying to look up an always-changing device name on Linux.

Use the bmp devices created under /dev/serial/by-id/usb-Black_Sp...-if00 or create a file named `/etc/udev/rules.d/99-blackmagic.rules` with the following contents:

    # Black Magic Probe
    # there are two connections, one for GDB and one for uart debugging
      SUBSYSTEM=="tty", ATTRS{interface}=="Black Magic GDB Server", SYMLINK+="ttyBmpGdb"
      SUBSYSTEM=="tty", ATTRS{interface}=="Black Magic UART Port", SYMLINK+="ttyBmpTarg"

Then unplug / replug the probe, or restart the computer.

Now you can access the probe at the stable names `/dev/ttyBmpGdb` and `/dev/ttyBmpTarg`.

## I want to connect to a Black Magic Probe on another machine.

You can use stty and netcat.  On the machine with the probe connected, make a little TCP server on port 2000 with these commands:

    stty -F /dev/ttyBmpGdb raw -onlcr -iexten -echo -echoe -echok -echoctl -echoke
    nc -vkl -p 2000 > /dev/ttyBmpGdb < /dev/ttyBmbGdb

In gdb on the remote machine, connect with `target extended-remote hostname:2000` where `hostname` is the name or IP address of the machine running the probe.

## Is it normal that my Black Magic Probe is warming up noticeably?

Yes, under normal operations the Black Magic Probe V2.1 is drawing 30-60mA. When using the `tpwr` functionality to supply power to a target like the 1Bitsy it can draw up to 120mA resulting in 0.6W of dissipated heat. The voltage regulator can heat up to 75°C under normal operations, it is rated for up to 125°C.

The problem is fixed on firmware v1.8.0 and newer

![Black Magic Probe Heatmap](/_assets/BMP_V2_1_heat_image.jpg)

## How does the Black Magic Probe compare to the ST-Link programmer?

There are a few advantages of the Black Magic Probe. BMP is open-source, meaning that you can look inside it if you need or want to. We are getting support for new ARM Cortex-M based chips on a regular basis, so you are not limited to just the STM32. We have preliminary support for Cortex-A this will result in the ability to use the probe with Raspberry PI and Beagle Bone Black and many others. The Black Magic Probe also supports JTAG not only SWD, because not all microcontrollers use SWD. Also JTAG makes it possible to chain together more than one microcontroller. The GDB server is implemented on the probe itself, this means we do not use some proprietary protocol to talk to your debugger software, making the setup more repeatable and removing the need for custom config files. All you need to do is fire up GDB and connect to the virtual serial port of the Black Magic Probe, no special setup necessary. It is physically small, you can plug it into your hardware even if it is buried deeply inside your killer robot. We have equipped the Black Magic Probe V2.1 (this is the version the Kickstarter backers will receive) with dual supply level shifters that make it possible to connect to targets that run on voltages as low as 1.7V and as high as 5V. The transceivers are more robust than the STM32 GPIO meaning that if the BMP is connected wrongly to the target it is less likely you will hurt either the Black Magic Probe or your target. Also the Black Magic Probe comes with a TTL level UART providing a bonus USB to Serial capability that can be used simultaneously with the GDB JTAG/SWD debugger.

## Why is XXX not supported?

Because nobody implemented the required functions yet. Look on [GitHub](https://github.com/blackmagic-debug/blackmagic/pulls) if there is a pending pull request for your target. Consider testing PRs that try to implement the desired target to help us triage merge of new hardware support.

## Why is Raspberry Pi 1 not supported?

Because it is an old ARM TDMI architecture, that is not compatible with ADIv5. (if you want to work on adding support for this contact us on [![Discord](https://img.shields.io/discord/613131135903596547?logo=discord)](https://discord.gg/P7FYThy) we have some sample code that needs work, if you want to dig deep into protocol spec sheets this is a project for you. :) )

## Why is Raspberry PI 3 not supported?

Because it is a 64Bit architecture. We are working on adding 64bit support but it is not trivial. If you want to help with that contact us on [![Discord](https://img.shields.io/discord/613131135903596547?logo=discord)](https://discord.gg/P7FYThy).

## Why is Beagle Bone Black not supported?

Because Texas Instruments... but we are working on it. :) If you want to help with that contact us on [![Discord](https://img.shields.io/discord/613131135903596547?logo=discord)](https://discord.gg/P7FYThy). See [issue #166](https://github.com/blackmagic-debug/blackmagic/issues/166) for details.

## How do I upgrade to a more recent version?

Follow the [upgrade](/upgrade.md) instructions.
