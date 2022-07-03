# Terminology

Black Magic Debug consists of multiple elements that have fairly similar naming that can be confusing. To make this Change Log bit easier to decipher here is a little bit of history and term explanation.

Black Magic Debug (BMD) was originally designed as just a firmware for a purpose made hardware called Black Magic Probe (BMP) that can speak the GNU Debugger (GDB) “remote” serial protocol. The original BMP hardware is also called “native” as over time additional “Host” platforms were added that the firmware could be loaded onto. (such host hardware can be an STM32F4 discovery board, or ST-Link hardware and many more)

Additionally BMD can also be compiled as a stand alone PC application, (we call it Black Magic App, or **BMA** and formally known as **hosted**) that can act as a software in the middle, similar to the way OpenOCD works. In this case BMP is only acting as a USB to JTAG/SWD translator and the Black Magic App (BMA) does all the heavy lifting. Additionally this also allows the use of BMA with other probe hardware running non Black Magic Firmware (BMF), like for example: JLink, ST-Link, sw-link, FTDI and more.

- **Black Magic Debug** (abbreviated to **BMD**) - Is the project name, an umbrella describing the project but also sometimes acts as the term describing the software.
- **Black Magic Firmware** (abbrev. **BMF**) - More specifically just the Black Magic Firmware that is loaded either onto Black Magic Probe hardware or onto any other supported host hardware.
- **Black Magic App** (abbrev. **BMA**) (formerly known as **Hosted** or **PC-Hosted**) - The Black Magic Debug system compiled as a PC application instead of a Firmware. Allowing it to be used in software in the middle mode instead of being contained to a hardware device. This used to be called “**hosted**” in the context of the project.
- **Black Magic Probe** (abbrev. **BMP**) - The “**native**” Black Magic Debug (BMD) hardware that was specifically designed and intended for the BMD project. This is the hardware you can buy from 1BitSquared, Adafruit and other resellers as “the Black Magic Probe”.
- **Black Magic Core** (Abbrev. BMC) - This describes the core code of the project that handles JTAG/SWD protocol, implements Flashing, target detection and all target specific functionality. It does not include host platform specific code like for example code that toggles GPIO.
- **Host Platform** - Refers to the hardware that the BMD software (either Firmware or Application) runs on. It can be the PC, STM32, lm4f or some more specific hardware like Black Magic Probe aka. native, ST-Link, sw-link and so on.
- **Probe** aka. **Cable** - Refers to the hardware that is connected between the PC running GDB (and/or BMA) and the Target (DUT). In the simplest case it is a USB to JTAG/SWD converter like an FTDI chip but in most cases it is a dedicated hardware running either our BMF or some other firmware.
- **Target** - Refers to the Device Under Test (DUT), this is the hardware that the user wants to debug using BMD.
