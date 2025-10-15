# Black Magic Debug V2.0.0-rc1 Release Candidate

```{post} January 07, 2025
:author: esden
```

We are happy to announce the first [v2.0.0 release candidate](https://github.com/blackmagic-debug/blackmagic/releases/tag/v2.0.0-rc1) of [Black Magic Debug](https://black-magic.org). This is the first major release of the v2 series.

Here are some of the highlights:

- Switched to the Meson build system
- Implemented RISC-V support
- Implemented Cortex-R support
- Implemented ARMv8-M support
- And a bunch of newly supported targets:
  * Ambiq Apollo 3
  * ArteryTek AT32F405/F403/F413/F421/F423/F437
  * Atmel SAMC21
  * GigaDevice GD32F405
  * GigaDevice GD32VF1
  * Nordic Semi nRF54L
  * NXP Kinetis MK20DX256
  * NXP S32K344
  * Puya PY32
  * Renesas RZ/A1 A1L, A1LU and A1H
  * RPi Foundation RP2350
  * ST Micro STM32F410
  * ST Micro STM32H72/H73
  * ST Micro STM32H7A/H7B
  * ST Micro STM32WB0
  * TI MSPM0
  * TI TM4C1294KCDT
  * WinChipHead CH579

For more details please refer to the ChangeLog down below.

# Release Artifact Notes
With this release we are now officially releasing the [Black Magic Debug Application (aka. BMDA)](https://black-magic.org/knowledge/terminology.html) binaries for Linux, MacOS and Windows. You can find them as `blackmagic-[OS NAME]-[VERSION].zip` files attached to the release.
 
In this release we are officially beyond the flash capacity of the native hardware MCU flash memory. This means we are splitting the firmware up into 4 versions, each firmware supports a subset of targets and architectures. You can find the firmware binaries as `blackmagic-[FIRMWARE TYPE]-[VERSION].(elf|bin|hex)`. Here is the legend of supported targets in each firmware type:

* `native` -> Common targets:
  * Cortex-M architecture support
  * LPC targets support
  * nRF targets support
  * NXP (LPC + Kinetis) targets support
  * Renesas MCUs support
  * RPi Foundation MCUs support
  * ATSAM targets support
  * STM32 targets support
  * TI targets support
* `native-uncommon` -> Uncommon targets:
  * Cortex-A/R architecture support
  * Cortex-M architecture support
  * Ambiq Apollo3 support
  * EFM32 targets support
  * HC32 targets support
  * Renesas RA + RZ targets support
  * Xilinx Zinq support
* `native-st-clones` -> ST + ST Clone targets:
  * Cortex-A/R architecture support
  * Cortex-M architecture support
  * STM32 targets support
  * AT32 targets support
  * GD32 targets support
  * CH32 targets support
  * CH579 support
  * MindMotion targets support
  * Puya32 targets support
  * HC32 targets support
* `native-riscv` -> RISC-V targets (including hybrids):
  * RISC-V 32-bit architecture support
  * RISC-V 64-bit architecture support
  * GD32 targets support (GD32VF103)
  * RPi Foundation MCUs support

# ChangeLog V2.0.0-rc1

## Core Changes

- Implemented proper IR quirk handling for Xilinx FPGAs [lethalbit]
- Fixed some preprocessor logic issues for when RISC-V Debug is disabled [dragonmux]
- Implemented support for the `vCont` and `qAttached` GDB packets [dragonmux]
- Format string fixes in the RTT support [koendv]
- Format string and documentation fixes for `monitor heapinfo` [koendv]
- Introduced new `DEBUG_*_IS_NOOP` macros to allow better logic to be built around debug output [dragonmux]
- Format string fixes across the GDB server and monitor command systems [ALTracer]
- Missing prototypes and macro usage improvements [elagil]
- Fixed some `DEBUG_*()` calls with bad format strings [xobs]
- Improvements to allow the GDB server to idle more [ALTracer]
- Fixed various typos and spelling mistakes across the code code base [francois-berder]
- Improved the performance of the GDB `qCRC` packet handling [ALTracer]
- Fixed an issue with how aliasing works under macOS breaking the build of the CRC32 code [ALTracer]
- Improved the space efficiency and correctness of the 12 character serial number logic [ALTracer]
- Format string fixes and clean up [dragonmux]
- Reorganised the semihosting support out from the Cortex-M support [dragonmux]
- Refactored the semihosting implementation and fixed some implementation errors [dragonmux]
- Fixed an issue with alias handling on macOS [amyspark]
- Warnings and nomenclature fixes across the code base [dragonmux]
- Fixed the Clang fall-through warnings as the compiler doesn't understand the magic comment used before [dragonmux]
- Laid the groundwork for supporting the AM335x family parts from TI [dragonmux]
- Fixed some issues with the handling of GDB's single register read/write commands [OmniTechnoMancer]
- Removed all usage of `sscanf()` in the firmware to reduce code size and improve speed [OmniTechnoMancer]
- Added the specific IR quirk for the Xilinx Artix 7 XC7A200T [LAK132]
- Fixed an error in the remaining length calculation for the `vFlashWrite` GDB command handling [OmniTechnoMancer]
- Cleaned up from the tooling changes [dragonmux]
- Fixed a timeout mishandling issue that would result in timeouts executing wrongly for a few seconds every 49.7 days of uptime [dragonmux]
- Converted all uses of `sprintf()` over to `snprintf()` for improved safety and code size [ALTracer]
- Fixed a bug where the result of `vasprintf()` was ignored in the GDB packet handling, leading to crashes and badness [ALTracer]
- Improved handling of faults in the remote protocol so BMDA can properly recover from them [dragonmux]
- Overhaulled the exception system to fix a bug in how exception frames were being handled [dragonmux]
- Fixed a bug in how F-packets are detected during semihosting response processing [OmniTechnoMancer]
- Implemented support for semihosting's `SYS_ELAPSED` and `SYS_TICKFREQ` calls [ALTracer]
- Fixed a crash from in `target_list_free()` caused by improper exception handling within the function [dragonmux]
- Fixed a `NULL` pointer dereference in the target voltage handling and made the implementations consistent [ALTracer]
- Fixed compilation with newlib 4.3.0+ by opting out of the unwinder logic it now pulls in [ALTracer]
- Implemented deinit for the SWO implementation and made the buffer for async mode heap allocated [ALTracer]
- Demarked the platform-specific commands in the `monitor help` output [Misaka0x2730]
- Fixed the format string warnings for all `tc_printf()` usage [HrMitrev]
- Fixed several bugs in the Manchester-mode SWO support that had it broken across several platforms [ALTracer]
- Fixed a NULL dereference that was possible in the `vFlashDone` handler when run with no target selected [ALTracer]
- Made the SWO command report back the actual baud rate achieved for UART-mode, not just the one requested [ALTracer]
- Reduced duplication by consolidating the GDB packet buffer sizing macros [Misaka0x2730]
- Implemented support for other RTT channels than 0, and improved the documentation of the implementation [xobs]
- Overhauled the SWO implementation, implementing runtime switchable decoder selection [dragonmux]
- Fixed the Git ignore configuration to properly ignore the dependency clones [desertsagebrush]
- Switched the gate macro nomenclature for several things to `CONFIG_<thing>` for consistency [dragonmux]
- Implemented a proper non-halting memory access marker for targets (`TOPT_NON_HALTING_MEM_IO`) to replace the previous heuristic that was broken [dragonmux]
- Fixed a crash caused by too short a buffer being passed to a `hexify()` call in the remote protocol implementation [xobs]
- Fixed several bugs in the RTT implementation and improved some code clarity [xobs]
- Fixed a crash in the `tdi_low_reset` monitor command when run before any JTAG scans have yet been done [dragonmux]
- Overhauled the target mass erase system, pulling lots of common logic not the target API layer [perigoso]
- Improved the GDB packet handling system, reducing allocations and improving speed a bit [perigoso]
- Fixed a missing include for `string.h` in the GDB packet handler [xobs]
- Allow an external buffer to be supplied to the GDB packet handler [xobs]
- Overhauled the main project README [dragonmux]
- Fixed a pile of cast-based conversions warnings [dragonmux]
- Fixed a regression in the GDB server that meant block memory reads would inexplicably fail [ALTracer]

## Build System Changes

- Introduced a new build system based on Meson [perigoso/dragonmux]
- Added a build target summary to the Meson build system [dragonmux]
- Improved the `pre-commit` hook setup for `clang-format` [amyspark]
- Fixed an encoding issue for `pre-commit` under Windows [perigoso]
- Fixed a typo in one of the warnings in the Meson build system [lasutek]
- Documented a small hitch with how PowerShell consumes Meson options lines [perigoso]
- Updated the BMDA dependencies `libusb` and `HIDAPI` to address some issues, particularly on M3 devices [dragonmux]
- Added a Meson Wrap fallback for the `libftdi1` BMDA dependency [dragonmux]
- Fixed the build exploding under Meson on macOS due to BMDA dependencies needing a C++ compiler [amyspark]
- Added a guard for the CH579 support to help with Flash size [ALTracer]
- Made the at32f43x support optional in both build systems [ALTracer]
- Updated the targets enabled for larger Flash platforms under Meson [ALTracer]
- Updated the libopencm3 version used to get various fixes upstream has not yet merged [dragonmux]
- Implemented the ability to select the SWO decoder built into the firmware [sidprice]
- Cleaned up the build system a bit, fixing some target family description texts [dragonmux]
- Disable some of the targets by default for the f072, stlink and native probe platforms to get things to fit Flash [esden]
- Removed the Makefile-based build system [esden]
- Implemented better control over the targets that can be enabled and created a suite of profiles for native for what is enabled out the box [dragonmux]

## Script/Utility Changes

- Added nix-direnv integrations [wucke13]
- Removed deprecated tooling [dragonmux]
- Fixed a typo in the ST-Link udev rules [WeissbMa]
- Fixed an error in the `clang-tidy` configuration which rendered it invalid [OmniTechnoMancer]
- Fixed up the udev rules to work with udev >= 247 [dragonmux]
- Updated the `swolisten` utility to properly walk the descriptors for the endpoint to use [ALTracer]
- Implemented a script for building firmware for all probes under Meson [esden]

## Project CI Changes

- Upgraded the `pre-commit` check for accidental assignment to correct handling of char literals [perigoso]
- Added MSVC and macOS jobs for PR builds to help prevent regressions [amyspark]
- Worked around a macOS 14 SDK issue making CI fail [amyspark]
- Various fixes for GCC builds on macOS [amyspark/dragonmux]
- Overhauled the CI configs to use newer OSes, compilers and have more sensible build matrices for better code coverage [dragonmux]
- Made use of `make`'s `-j` option in CI for a speed boost [ALTracer]
- Fixed CI breaking due to changes in the Ubuntu images used due to Python PEP 668 [dragonmux]
- Fixed the macOS version we used becoming deprecated by upgrading the configs [dragonmux]
- Added the Black Pill platforms back into CI as they got missed [ALTracer]
- Fixed an issue in the build-and-upload flow that results in improper version information being embedded [dragonmux]

## ARM (ADIv5 and ADIv6) Changes

- ARM Debug: De-duplicated the SWD error handling logic across all supported probes [perigoso]
- ARM Debug: Implemented support for discovering and debugging Cortex-R cores [dragonmux]
- ARM Debug: Unified the Cortex-A and Cortex-R handling [dragonmux]
- ARM Debug: Implemented memory I/O diagnostics for Cortex-A/R cores [dragonmux]
- ARM Debug: Extracted and de-duplicated the SWD parity calculation logic, giving it consistency [ALTracer]
- ARM Debug: Used the AP banked registers to speed up Cortex-A/R instruction launches used for register and memory access [dragonmux]
- ARM Debug: Fixed a typo in one of the defines for the Cortex-M support [RoboSchmied]
- ARM Debug: Implemented support for 64-bit APs in preparation for 64-bit Cortex support [dragonmux]
- ARM Debug: Fixed a couple of regressions in the SWD and ADIv5 memory access handling [dragonmux]
- ARM Debug: Fixed an error in the DPIDR revision decoding mask [iysheng]
- ARM Debug: Harmonised all SWD backends on what they return from `seq_in_parity` for consistency [dragonmux]
- ARM Debug: Improved the SWD bitbanging to make timing more consistent [tlyu]
- ARM Debug: Fixed a CPSR mapping error for the Cortex-A/R support [litui]
- ARM Debug: Implemented ADIv6 support [dragonmux]
- ARM Debug: Fixed an issue where the Cortex-A/R implementation could cause hangs due to the target not being halted when it should be [litui]
- ARM Debug: Implemented proper support for TrustZone on Cortex-M parts [dragonmux]
- ARM Debug: Allow access to DEMCR outside of the implementation for Cortex-M devices [xobs]
- ARM Debug: Implemented use of the JTAG -> Dormant State sequence to work with targets that need it [mean00]
- ARM Debug: Implemented proper configuration of CSW for APB2 and APB3 [marysaka]
- ARM Debug: Ensure the CPUID register is only read once a Cortex-A/R core is actually powered [marysaka]
- ARM Debug: Implemented parsing of CoreSight ROM tables found on APs [marysaka]
- ARM Debug: Implemented support for ADIv6 JTAG-DPs [dragonmux]
- ARM Debug: Refactored MEM-AP configuration out from `adi_config_ap()`, reducing code complexity [HrMitrev]
- ARM Debug: Implemented watchpoints support for ARMv8-M parts [mean00]
- ARM Debug: Fixed a typo in the Cortex-A/R error checking routine [marysaka]
- ARM Debug: Make sure the core gets halted in `cortexar_mem_write()` same as `cortexar_mem_read()` [marysaka]
- ARM Debug: Performed some structural clean up and fixed some issues around ARMv8-M debug [dragonmux]

## RISC-V Debug Changes

- RISC-V: Implemented support for JTAG-based RISC-V Debug v0.13 [dragonmux/perigoso/mean00]
- RISC-V: Implemented System Bus memory access support [dragonmux]
- RISC-V: Implemented a `tinfo` register read quirk to handle odd targets [dragonmux]
- RISC-V: Made sure we stop when we hit ebreak's when the target's running [mean00]
- RISC-V: Implemented support for handling targets implementing single precision float [mean00]
- RISC-V: Implemented JTAG protocol acceleration in the BMD remote protocol [dragonmux]
- RISC-V: Fixed a bug in the single-stepping vs normal execution logic for when to suspend interrupts [mean00]

## Target Changes

- at32f435/f437: Implemented Flash support [ALTracer]
- samd: Fixed an error in the device ID masks [koendv]
- stm32mp15: Implemented support for the Cortex-A cores in this part series [dragonmux]
- zynq7000: Re-introduced proper Zynq-7000 support as a discrete target seperate from the Cortex-A support [dragonmux]
- at32f403a/407: Implemented dual Flash bank support [ALTracer]
- lmi: Fixed a missed variable initialisation in the Flash stub [francois-berder]
- stm32h7: Improved the SRAM part of the memory maps [ALTracer]
- stm32f1: Fixed a bug in split-bank erase handling [tlyu]
- gd32f3: Fixed handling of XL-density devices by handling them as dual bank [ALTracer]
- renesas_rz: Fixed a mishap in the Meson BMDA build logic [dragonmux]
- stm32mp15: Implemented a revision reporting monitor command like with other STM32 parts [ALTracer]
- stm32h7: Improved the revision reporting command implementation to be more complete [ALTracer]
- rp2040: Implemented a Flash stub to improve reprogramming throughput [vesim987/dragonmux]
- s32k3xx: Fixed a formatting string mistake [xobs]
- samd/samx5x: Fixed how parts are identified using the target structure instead of extra register reads [dragonmux]
- ke04: Added a missing probe call so these parts are properly identified again [nqbit]
- stm32h7b: Implemented Flash programming support [ALTracer]
- stm32l4: Fixed the Flash size handling and Flash registration for the STM32U5 parts [rob-the-dude]
- imxrt: Simplified one of the debug logging guards using the new `DEBUG_*_IS_NOOP` macros [ALTracer]
- stm32: Improved the UID command readout and display with a proper decoder for this data [ALTracer]
- stm32f103: Implemented support for recognising another of the clones [nboehm99]
- stm32f4: Made sure to freeze the WDTs on halt as they were causing problems [dragonmux]
- at32f435/437: Implemented support for the option bytes on these parts [ALTracer]
- stm32: Avoid displaying non-printable characters in the UID decoder [ALTracer]
- stm32g0/c0: Enable the UID decoder for these parts [ALTracer]
- efm32/nrf51/renesas_ra: Unified the UID strings to reduce Flash usage and be more consistent [ALTracer]
- stm32mp15/stm32h74: Fixed a misidentification issue for the M4 cores on these parts due to ROM table issues [ALTracer]
- stm32: Implemented control of the WDTs across all STM32's so they get frozen when the target is halted [dragonmux]
- stm32: Fixed some format string errors for some `DEBUG_TARGET()` invocations [xobs]
- stm32h7: Formatted the address the DBGMCU IDCODE was read from in hex [xobs]
- stm32h5: Fixed an address error for the DBGMCU and some missing SRAM mappings [ALTracer]
- stm32l4: Fixed an error in the WDT handling in the DBGMCU which resulted in a crash [dragonmux]
- s32k3xx: Removed an assert that is always true for a code size improvement [ALTracer]
- renesas/rz: Implemented auto-detection of the SRAM available on the part [litui]
- at32f43x: Implemented WDT control and sleep management to get parity with the STM32 targets [ALTracer]
- rp2350: Implemented support for the RISC-V half of the part [dragonmux]
- at32f43x: Fixed some typos in the WFI/WDT handling support [ALTracer]
- lpc43xx: Fixed a typo in the part numbering for the LPC433x and LPC435x [via]
- stm32wbxx: Implemented option bytes support [Lars-inspiro]
- stm32l4: Fixed some isues with STM32L4/L5/U5/G4/WL/WB family identification [dragonmux]
- stm32f1: Improved the option bytes support for ArteryTek parts [ALTracer]
- stm32f1: Fixed a couple of format string errors [xobs]
- at32f43x: Cleaned up in the implementation, eliminating some complexity and making use of the STM32 UID handler [ALTracer]
- mspm0: Removed a couple of always-true asserts [ALTracer]
- mspm0: Consistency and code pattern cleanups [dragonmux]
- stm32: Fixed a bug in the attach/detach behaviour caused by how the DBGMCU state was being maintained [dragonmux]
- stm32f0: Corrected the SRAM mappings sizes as they were wrong [ALTracer]
- at32f405: Fixed a Flash mappings size error caused by a units mistake [ALTracer]
- stm32l4: Fixed a couple of discovery bugs leading to miss-detections and improper memory maps [ALTracer]

## Targets Added

- TI TM4C1294KCDT [desertsagebrush]
- Atmel SAMC21 [koendv]
- GigaDevice GD32VF1 [dragonmux]
- Renesas RZ/A1LU [dragonmux]
- Renesas RZ/A1, RZ/A1H [litui]
- NXP S32K344 [via]
- NXP Kinetis MK20DX256 [vedranMv]
- ST Micro STM32F410 [dragonmux]
- WinChipHead CH579 [ArcaneNibble]
- ST Micro STM32H72/H73 [dragonmux]
- Puya PY32 [ArcaneNibble]
- ST Micro STM32H7A/H7B [ALTracer]
- GigaDevice GD32F405 [dragonmux/klenSA]
- Ambiq Apollo 3 [sidprice/litui]
- ST Micro STM32WB0 [dragonmux]
- RPi Foundation RP2350 [dragonmux]
- ArteryTek AT32F405/F403/F413/F421/F423 [ALTracer]
- TI MSPM0 [hardesk]
- Nordic Semi nRF54L [zyp]

## Host Platform Changes

### Added

- Support for the USB side of ctxLink [sidprice]
- Support for the WiFi side of ctxLink [sidprice]

### Common

- Changed the firmware SRAM layout organisation so heap and stack cannot run into each other silently [dragonmux]
- Reordered endpoint usage so all core features work even on the DWC2 platforms with only 4 usable endpoints [ALTracer]
- Implemented the ability for platforms to have commands specific to them [Misaka0x2730]
- Implemented use of `OVER8` for more available baud rates on platforms that support it [ALTracer]
- Gated USB-specific definitions behind a check for not `NO_LIBOPENCM3` [xobs]
- Allow platforms to be dynamically identified, cleaning up the platform identification system [Misaka0x2730]
- Cleaned up in the AUX serial handling and logic to improve code quality and simplify the flow [dragonmux]
- Removed use of librdimon for `DEBUG_*()`-enabled builds, saving ~1.2kiB of Flash [tlyu]

### STM32

- Fixed some UB bit shifts in some left shift expressions [tlyu]
- Fixed the timeouts used in the F1 DFU bootloader, speeding everything up [ALTracer]
- Further improvements to GDB server idling on the DWC2-based platforms [ALTracer]
- Adapted the async (UART) SWO implementation for use on the F4-based platforms [ALTracer]
- Fixed a USB enumeration bug on F4-based platforms [sidprice]

### Black Magic Probe (aka “Native”) host

- Improved the USB re-enumeration timings to be more spec compliant to help how controllers like the M3's interact [dragonmux]
- Improved handling of `hwversion` for a speed and Flash usage improvement [dragonmux]

### ctxLink host

- Optimized the code for calling the boot ROM a bit [sidprice]
- Fixed a bug with the DMA configuration for the aux serial interface [sidprice]
- Fixed a bug with the target voltage handling which resulted in a crash [sidprice]
- Implemented support for async-mode (UART) SWO [sidprice]
- Switched the platform to use the ROM bootloader exclusively [sidprice]
- Fixed a crash in the voltage reporting logic when reporting battery voltage [sidprice]
- Updated the README to refect build system changes [sidprice]
- Improved the ADC usage to reduce its impacts on WiFi interface speed [sidprice]
- Fixed some variable references that went wrong when `DEBUG_*()` is enabled [sidprice]
- Switched the WINC1500 into manual power mode for a bit of a performance increase [sidprice]
- Enabled using the platform with `DEBUG_*()` being enabled [sidprice]

### ST-Link v2/v2.1 host

- Implemented support for the ST-Link v2-ISOL dongle variant [HrMitrev]
- Switched mechanisms for generating output on the ST-Link v2-ISOL dongle to improve code size [HrMitrev]
- Fixed a pin conflict between the `SWIM_AS_UART` build option and the nRST pin mapping [positron96]
- Added a Meson cross-file and probe type for the ST-Link v2-ISOL dongle support [HrMitrev]

### ST-Link v3 host

- Fixed the CRC logic for `compare-sections` (`qCRC`) not working on this platform [ALTracer]
- Fixed the target serial interface not working on this platform [ALTracer]
- Fixed an issue with the `DEBUG_*()` output when enabled on this platform [ALTracer]
- Improved the documentation on how to program a dongle with the firmware [robots]
- Implemented support for tristating SWDIO and SWCLK, implementing clock tristating [ALTracer]

### Black Pill v2 host (now blackpill-f401cc, blackpill-f401ce and blackpill-f411ce, aka “The Black Pill hosts”)

- Added a `SHIELD` macro for defining if you are using your Black Pill with an expansion (shield) board [lenvm]
- Turned a couple of magic numbers into proper defines for the user button [lenvm]
- Sped up bus turnarounds, matching how the other platforms perform them [ALTracer]
- Added debug output support for the platform [ALTracer]
- Improved the DFU bootloader for the platform [ALTracer]
- Fixed some issues with the project bootloader on this platform [ALTracer]
- Fixed the platform requiring an extra reset after leaving the boot ROM [ALTracer]
- Switched the platform to use async-mode SWO as Manchester-mode is broken [ALTracer]
- Implemented the ability for the bootloader to report more state when built for use with a carrier board [sidprice]
- Fixed a documentation error in the platform SWO definitions [sidprice]
- Better documented how to build the platform and upgrade the firmware on a probe [ALTracer]
- Added a `swlink`-like alternative pinout (alt pinout 2) [ALTracer]
- Fixed the build instructions and updated the platform README [sidprice]

### Black Magic Debug App (aka “PC Host”)

- Assorted fixes to the J-Link backend [perigoso]
- Fixes for building under MSVC [xobs]
- Fixes for building on FreeBSD [ALTracer]
- Improved the speed of communications to BMPs via proper read buffering [dragonmux]
- Fixed the CMSIS-DAP backend's WAIT/FAULT response data phase handling [dragonmux]
- Fixed the semihosting implementation for BMDA to make the implementation conform to the spec [dragonmux]
- Fixed the CMSIS-DAP backend mishandling the adaptor packet sizing [dragonmux]
- Fixed an issue in the timeouts configuration under Windows leading to slowdowns [dragonmux]
- Implemented full MSVC compatibility [amyspark]
- Fixed the max frequency handling to respect user changes and not be entirely ephemeral [perigoso]
- Fixed a response buffer sizing mistake in the CMSIS-DAP backend [dragonmux]
- Implemented a gpiod based bitbanging backend [OmniTechnoMancer]
- Made BMDA listen on both IPv4 and IPv6 to properly support dual-stack setups [OmniTechnoMancer]
- Fixes for the ST-Link v2 backend buffer sizing and AP selection handling [ALTracer]
- Fixed an issue where MINDP was not properly handled on the ST-Link backend due to firmware doing extra steps [ALTracer]
- Fixed a typo in the platform's nRST state accessor [iysheng]
- Turned off stdout buffering under Windows to see progress output as it happens [ALTracer]
- Fixed a UB bit shift in the CMSIS-DAP backend's SWD code [dragonmux]
- Fixed a bug in the CMSIS-DAP backend where it used too many bits of the response packets as ACK bits [robots]
- Fixed a bug in how some CMSIS-DAP implementations handle the `DAP_SWD_SEQUENCE` command [dragonmux]
- Implemented display of the aux serial port on Windows to help users find it [HrMitrev]
- Implemented support for automatically opening CMSIS-DAP adaptors in v1 mode when available if unable to open in v2 mode [ALTracer]
- Rewrote the BMP-only probe discovery logic for Windows to avoid some stack overflows and other nastiness [dragonmux]
- Addressed where the `monitor version` output was put and what it contained to help with bug reporting [dragonmux]
- Implemented support for connecting to dongles running the firmware over TCP/IP [xobs]
- Implemented compatibility for building on 32-bit Windows [ALTracer]
- Fixed an include order error that had the build broken under some circumstances [xobs]
- Fixed an implicit fallthrough error in the CLI options processing logic [ALTracer]
- Fixed how we identify old firmware such as pre-v1.7 builds running the old product string scheme [dragonmux]
- Fixed a series of bugs in the CMSIS-DAP implementation which had block I/O broken under certain circumstances [dragonux]
- Fixed a bug caused by some versions of the MCU-Link firmware reporting broken version strings that need special handling [dragonmux]

## Contributors to v2.0.0-rc1

We have had 38 individuals contribute 1593 commits since the v1.10.2 release.

Contributor (Contributions)  
dragonmux (971)  
ALTracer (201)  
Sid Price (118)  
perigoso (102)  
OmniTechnoMancer (34)  
Sean Cross (25)  
Amy (21)  
Aria Burrell (12)  
Mary Guillemard (10)  
Dmitry Rezvanov (9)  
ArcaneNibble (9)  
Taylor Yu (8)  
mean00 (8)  
Aki Van Ness (7)  
Piotr Esden-Tempski (6)  
Hristo Mitrev (6)  
elagil (6)  
Matthew Via (4)  
lenvm (4)  
Koen De Vleeschauwer (4)  
Michal Demin (3)  
hardesk (3)  
Vegard Storheil Eriksen (2)  
Vedran (2)  
Sage Myers (2)  
Maciej Kuliński (2)  
iysheng (2)  
Francois Berder (2)  
wucke13 (1)  
RoboSchmied (1)  
Rob Newberry (1)  
Paul Melnikov (1)  
nqbit (1)  
Niko Boehm (1)  
Markus Weissbacher (1)  
Lars Sundström (1)  
Lars Smit (1)  
LAK132 (1)  

## Sponsors

This project is sponsored in parts by:

- [1BitSquared](https://1bitsquared.com/) - Design, Manufacture and distribution of open source embedded hardware development tools and platforms, as well as educational electronics. Thank you everyone who buys Black Magic Probes from 1BitSquared directly through our [stores](https://1bitsquared.com/products/black-magic-probe) or indirectly through [Adafruit.](https://www.adafruit.com/product/3839) The hardware sales allow us to continue supporting the Black Magic Debug project.
- All the generous [GitHub Sponsors](https://github.com/sponsors/dragonmux) supporting dragonmux’s work
- All the generous [Patrons](https://www.patreon.com/1bitsquared) and [GitHub Sponsors](https://github.com/sponsors/esden) supporting esden’s work