# PlatformIO

[PlatformIO](https://platformio.org/?utm_source=github&utm_medium=blackmagic) is an open source ecosystem for IoT development with the cross-platform build system, library manager and **full support for Black Magic Probe**. It works on the popular host OS: macOS, Windows, Linux 32/64, Linux ARM (like Raspberry Pi, BeagleBone, CubieBoard).

**Platforms:** Atmel AVR, Atmel SAM, Espressif 32, Espressif 8266, Freescale Kinetis, Intel ARC32, Lattice iCE40, Maxim 32, Microchip PIC32, Nordic nRF51, Nordic nRF52, NXP LPC, Silicon Labs EFM32, ST STM32, Teensy, TI MSP430, TI Tiva, WIZNet W7500

**Frameworks:** Arduino, ARTIK SDK, CMSIS, Energia, ESP-IDF, libOpenCM3, mbed, Pumbaa, Simba, SPL, STM32Cube, WiringPi

## Contents
- {ref}`usage/platformio:pio unified debugger`
- {ref}`usage/platformio:quick start`
- {ref}`usage/platformio:debugging from cli`
- {ref}`usage/platformio:advanced configuration`
- {ref}`usage/platformio:issues and support`

## PIO Unified Debugger

[PIO Unified Debugger](http://docs.platformio.org/en/latest/plus/debugging.html?utm_source=github&utm_medium=blackmagic) is "1-click" solution with zero configuration for the multiple architectures and development platforms. It supports over 200 embedded boards and the most popular IDEs:

* [VSCode](http://docs.platformio.org/en/latest/ide/vscode.html?utm_source=github&utm_medium=blackmagic#ide-vscode)
* [Atom](http://docs.platformio.org/en/latest/ide/atom.html?utm_source=github&utm_medium=blackmagic#ide-atom)
* [Eclipse](http://docs.platformio.org/en/latest/ide/eclipse.html?utm_source=github&utm_medium=blackmagic#ide-eclipse)
* [Sublime Text](http://docs.platformio.org/en/latest/ide/sublimetext.html?utm_source=github&utm_medium=blackmagic#ide-sublimetext)

See a full list of [compatible boards for Black Magic Probe](http://docs.platformio.org/en/latest/plus/debugging.html?utm_source=github&utm_medium=blackmagic#boards) ("Debug" column).

[![PlatformIO IDE](https://raw.githubusercontent.com/platformio/platformio-docs/develop/_static/ide/vscode/platformio-ide-vscode.png)](https://platformio.org/platformio-ide?utm_source=github&utm_medium=blackmagic)

## Quick Start

1. Install [PlatformIO IDE](https://platformio.org/platformio-ide?utm_source=github&utm_medium=blackmagic).
2. Create a new project using "PlatformIO Home > New Project" wizard (🏠 icon on the toolbar)
3. Edit **Project Configuration File** [platformio.ini](http://docs.platformio.org/en/latest/projectconf.html?utm_source=github&utm_medium=blackmagic) and set Black Magic Probe as default tool for debugging and programming/uploading, update `upload/debug` port following {ref}`this guide <gdb-commands>`:

```ini
[env:someboard]
platform = ...
framework = ...
board = ...
debug_tool = blackmagic
upload_protocol = blackmagic
upload_port = !!!UPDATE_ME!!!
monitor_port = !!!UPDATE_ME!!!
```

4. Start debug session:
   * PlatformIO IDE for Atom: Menu > PlatformIO > Debug > Start a debug session
   * PlatformIO IDE for VSCode: Menu > Debug > Start Debugging
5. Happy debugging with PlatformIO!

## Debugging from CLI

Further details in documentation for [platformio debug](http://docs.platformio.org/en/latest/userguide/cmd_debug.html?utm_source=github&utm_medium=blackmagic) command.

## Advanced configuration

Please visit official PlatformIO documentation for the [advanced debugging configuration](http://docs.platformio.org/en/latest/projectconf/section_env_debug.html?utm_source=github&utm_medium=blackmagic).

## Issues and support

Please mail [contact@pioplus.com](mailto:contact@pioplus.com?Subject=PlatformIO%20Unified%20Debugger%20and%20Black%20Magic%20Probe) or use our well-established [PlatformIO Community](https://community.platformio.org?utm_source=github&utm_medium=blackmagic) for questions and answers.
