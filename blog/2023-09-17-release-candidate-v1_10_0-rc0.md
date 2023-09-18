# Release Candidate V1.10.0-rc0

```{post} September 17, 2023
:author: esden
```

We are happy to announce the first [V1.10.0 release candidate](https://github.com/blackmagic-debug/blackmagic/releases/tag/v1.10.0-rc0) of [Black Magic Debug](https://black-magic.org).

This will be the final minor release of the v1 series.

Here are some of the highlights:

- Implemented support for talking with SPI Flash directly
- The firmware now automatically binds drivers for the Trace and DFU interfaces on Windows
- And a bunch of newly supported targets:
    - MindMotion MM32
    - ST Micro STM32WB1X
    - GigaDevice GD32F4
    - NXP LPC43x0
    - NXP LPC55
    - ST Micro STM32C0xx
    - NXP LPC40
    - NXP/Freescale i.MXRT
    - GigaDevice GD32F2
    - GigaDevice GD32E5
    - ST Micro STM32H5
    - TI MSP432E4
    - HDSC HD32L110
    - Arterytek AT32F435
    - ST Micro STM32U5
    - Nordic Semi nRF91
- Target power now has soft-start on native hardware v2.3+ to address potential brown out. This feature was also backported to all other native BMP hardware that has a digital target power control to remove power rail overshoot. For more detail about this change refer to [V1.9.2 release notes](2023-09-16-release-v1_9_2)

For more details please refer to the ChangeLog down below.

# ChangeLog v1.10.0

## Core Changes

- Handle continue-with-signal messages from GDB [zyp]
- Restructured the GDB main loop from blocking to polling [xobs]
- Cleaned up and fixed some style issues in the RTT code [dragonmux]
- Refactored out the JEP-106 manufacturer codes into their own header [dragonmux]
- Improved the GDB register API nomenclature and organisation [dragonmux]
- Fixed some formatting issues with ternaries [dragonmux]
- Improved the correctness of JTAG bitbanging due to the generation of setup-and-hold violations upsetting RISC-V targets [dragonmux]
- Implemented automatic sizing of the Flash write buffers for targets [perigoso]
- Fixes for the setjmp header used under Windows in the exception code [sidprice]
- Restore the old GDB detach behaviour from pre-v1.8 as the auto-reattach-on-connect behaviour was breaking certain debug integrations [tlyu]
- Fixed some issues that caused several nasty linker warnings under GCC 12 [dragonmux]
- Implemented JTAG IR quirk handling to deal with parts whose IR lengths cannot be simply detected [dragonmux]
- Fixed a regression in the semihosting implementation caught by koendv [dragonmux]
- Round up reads in the generic CRC32 implementation to the nearest multiple of 4 [zyp]
- Fixed a regression in the JTAG→SWD sequence code caused by generating one too few cycles [dragonmux]
- Fixed part of how JTAG scan implements IR lengths handling [dragonmux]
- Improved the debug logging subsystem and introduced error and protocol debug levels [dragonmux]
- Fixed an issue where running `load` followed immediately by `kill` from GDB would result in a crash [dragonmux]
- Added a parameter to `mon reset` that allows specification of the pulse length [silbe]
- Removed the JTAG scan IR lengths mechanism [dragonmux]
- Unified the help syntax used in `mon help` [silbe]
- Replaced all usage of `strtol` with `strtoul` to help reduce Flash usage [ALTracer]
- Switched to the reentrant `strtok_r` from `strtok` to fix a correctness issue and reduce Flash usage [ALTracer]
- Implemented the firmware side of a new SPI remote protocol [dragonmux]
- Implemented Microsoft OS Descriptors support and provided driver binding descriptors for the Trace and DFU interfaces [dragonmux]
- Improved connect-under-reset handling reliability [jelson/dragonmux]
- Reworked the JTAG bitbanging with-delay routines to solve a bug in how they work [dragonmux]
- Decoupled the general.h and platform.h headers to reduce build churn for low performance build hosts [ALTracer]
- Increased the SysTick frequency from 100Hz to 1kHz in the firmware [ALTracer]
- Refactored the integer-only stdio definitions for the firmware [ALTracer]
- Implemented Flash state tracking for targets that need more complicated handling [dragonmux]
- Various fixes for type mistakes, missing integer suffixes and debug level usage [perigoso]
- Fixed a regression which caused SWD to hang if configured for max speed [dragonmux]
- Fixed some type mismatches in the CRC32 implementation [dragonmux]
- Fixed an issue with the fake threads implementation that can hang certain IDEs [dragonmux]
- Improved the organisation of the remote protocol packet handling logic [dragonmux]
- Fixed a pile of `-fanalzyer` lints highlighting bugs in target code [dragonmux]
- Fixed some return types issues in the scan logic and switched `swdp_scan` → `swd_scan` (with a fallback) as part of phasing out the “SWDP” nomenclature [perigoso]
- Fixed a missing include for `stdbool.h` in the GDB packet code [xobs]
- Improved the safety around target power by implementing detection of backfeeding and cutting power when this is detected [dragonmux]
- Improved the wording of the documentation around `vMustReplyEmpty` packets [perigoso]
- Reduced the Flash usage of the JTAG devices table [dragonmux]
- Fixed a race condition and resulting `NULL` dereference in the morse code subsystem [jcamdr]
- Fixed `-Wpedantic` warnings about forward referencing of enums [perigoso]
- Fixed `-Wpedantic` warnings about empty initialiser lists [perigoso]
- Fixed `-Wpedantic` warnings about returns in functions that return `void` [perigoso]
- Fixed several warnings about using characters for array subscripts (`-Wchar-subscripts`) [perigoso]
- Fixed several warnings about local variable shaddowing (`-Wshadow=local`) [perigoso]
- Fixed several warnings about bad function casts (`-Wbad-function-cast`) [perigoso]
- Fixed several string formatting warnings [perigoso]
- Fixed `-Wpedantic` warnings about using range expressions in switch-case and array definitions [perigoso]
- Removed a dangling extern variable declaration that is unused in the code base [perigoso]
- Fixed some missing braces on array of structure initializers [zyp]
- Fixed `-Wpedantic` warnings about binary constants [perigoso]
- Consolidated the alignment macros originally defined for ADIv5 and moved them into their own header [perigoso]

## Build System Changes

- Don’t delete version.h when building from an extracted archive [esden]
- Fixed Git detection when using BMD as a Git submodule [esden]

## Script/Utility Changes

- Fixed a section heading issue in the contribution guidelines [SludgeGirl]
- Updated the clang-format pre-commit hook to v16.0.2 [lenvm]
- Added clang-tidy configuration for identifier case checking [sidprice]

## Project CI Changes

- Implemented CI for Windows [dragonmux]
- Updated the main build CI to use the GitHub Actions `actions/checkout@v3` action [gemesa]
- Spelling, punctuation and grammar fixes in the GHA configs [gemesa]
- Updated the lint CI to use the GHA `actions/checkout@v3` and `pre-commit/action@v3.0.0` actions [perigoso]
- Updated the ARM compilers used in the PR workflows [esden]
- Restricted the CI flows with `ENABLE_RTT=1` set due to the Flash usage limitations problems [dragonmux]

## ARM (ADIv5) Changes

- Cortex-A: Fixes and improvements for Cortex-R5 support
- ARM Debug: De-duplicated parts of the ADIv5 implementation and re-introduced the SWD interface header/structure [dragonmux]
- ARM Debug: Added support for the Chinese STAR-MC1 core type [koendv]
- ARM Debug: Added the Nordic Trace Buffer (NTB) to the component identification table [dragonmux]
- ARM Debug: Fixed a whole pile of JTAG protocol regressions (see #1389 for details) [dragonmux]
- ARM Debug: Improved Cortex-M halt/resume correctness [dragonmux]
- ARM Debug: Fixed an issue with the Cortex-M DWT mask calculation [silbe]
- ARM Debug: Correctness fixes for AP handling, implementing AP type dispatch, TrustZone handling and some multi-drop noise [dragonmux]
- ARM Debug: Reworked early DP bringup to improve correctness and reduce code bloat [perigoso]
- ARM Debug: Begun seperating out SWD multi-drop handling and untangling it [perigoso]
- ARM Debug: Improved the reliability of debug bringup to handle parts like the Ambiq Apollo 3 which get upset when debug resetting them too much [dragonmux]
- ARM Debug: Improved how JTAG DPv0 ID codes are handled to correctly identify more parts using them [dragonmux]
- ARM Debug: Refactored the Cortex handling to pull out commonality into a new implementation file ready for proper Cortex-R support [dragonmux]

## Target Changes

- stm32l4/stm32wb: Fixed the Flash erase error handling and detection [DrZlo13]
- lpc43x0: Implemented external Flash support [dragonmux]
- nrf51: Fixed handling for the recovery access port core register faking to allow attaching again [TheyCallMeNobody]
- ch32f1: Fixed `load` handling with CH32F103C8T6 parts [lasutek]
- ARM Cortex-M: Fixed a missing call to `sam3x_probe()` [AnantaSrikar]
- ch32f1: Improved support for CH32F103C8T6 parts [lasutek]
- stm32g0: Implemented support for STM32C0 option bytes erase [fabalthazar]
- stm32f1: Improved the STM32F1 option bytes handling correctness [dragonmux]
- lmi: Fixed TM4C129 identifications [dragonmux]
- lpc: Updated Flash registration to conform to the new APIs [dragonmux]
- sam3x: Fixed an issue that had Flash programming broken due to nRST interactions [dragonmux]
- stm32l0: Provided an implementation for mass erase for STM32L0 and STM32L1 [dragonmux]
- lpc55xx: Fixed a memory leak in `lpc55x_add_flash()` [francois-berder]
- target: Fixed an out of bounds array access in `jtag_scan()` [francois-berder]
- renesas: General documentation and cleanup [perigoso]
- rp: Fixed the Flash erase and write reliability issues caused by the ROM table calls hanging under certain circumstances [dragonmux]
- lpc55xx: Implemented support for LPC551x and LPC55S1x devices [dragonmux]
- lpc: Improved the correctness of the LPC IAP call mechanism and fixed some undefined behaviour [dragonmux]
- imxrt: Corrected some mistakes in debug formatting specifiers [xobs]
- ARM Cortex-M: Avoid doing long (64-bit) division in the HostIO implementation [ALTracer]
- imxrt: Fixed an error caused by an unused variable with `ENABLE_DEBUG=1` [ALTracer]
- stm32h7: Fixed a mass erase status check issue on the second Flash bank [bugobliterator]
- stm32h7: Improved support for the series [dragonmux]
- lpc546xx: Reduced Flash usage by refactoring the device identification code [ALTracer]
- target: De-duplicate various message strings to improve the Flash usage footprint [ALTracer]
- imxrt: Allow the definition and use of the `boot_mode` variable for Farpatch [xobs]
- lpc43xx: Refactored the target SRAM handling code to reduce Flash usage [ALTracer]
- lpc43x0: Fixed an ASAN crash in the LPC43x0 Flash detection logic due to it mishandling failure [dragonmux]
- stm32l4: Fixed the RAM sizing being in kibibytes but not being multiplied up properly to bytes [jcamdr]
- lpc55xx: Implemented support for the LPC55S69 [UweBonnes]
- ARM Cortex-M: Implemented a timeout for release from reset for parts that have non-functional nRST [UweBonnes]
- samx5x: Fixed an assumption that block size == Flash region lock size  which broke Flash write on these parts [Qyriad/ktemkin]

## Targets Added

- MindMotion MM32 [koendv]
- ST Micro STM32WB1X [grevaillot]
- GigaDevice GD32F4 [via]
- NXP LPC43x0 [dragonmux]
- ST Micro STM32C011 and STM32C031 [djix123]
- NXP LPC55 [dragonmux/UweBonnes/TomCrypto]
- NXP LPC40 [zyp]
- NXP i.MXRT [dragonmux]
- GigaDevice GD32F2 [iysheng]
- GigaDevice GD32E5 [ALTracer]
- ST Micro STM32H5 [dragonmux]
- TI MSP432E4 [neutered]
- HDSC HD32L110 [vesim987]
- Arterytek AT32F435 [ALTracer]
- ST Micro STM32U5 [jcamdr]
- Nordic Semi nRF91 [zyp]

## Host Platform Changes

### Added

- Support for the ST-Link v3 [jamesturton/stoyan-shopov/UweBonnes]
- Implemented support for the USB CDC command `GET_LINE_CODING` [dragonmux]
- Add error LED feedback for USB enumeration state [krogozinski]

### Common

- Enable semihosting output redirection on all firmware platforms [koendv]
- Restructured the platforms folder so the `stm32` and `tm4c` common components are in the `common` area [lenvm]

#### STM32

- Fixed an off-by-one issue in the STM32F4 DFU bootloader implementation which broke erase [Electronshik]

#### TM4C

### Black Magic Probe (aka “Native”) host

- Fixed some pinout and clarity issues with nRST and TPWR [dragonmux]
- Implemented target power soft-start for hw1+ (hardware v2.0a+) [dragonmux]

### ST-Link host

- Fixed the pinout for the nRST pin to handle clones using PB6/7 instead of PB0/1 [silbe]

### F4 Discovery host

- Added pin definition documentation for the UART to the README [franzflasch]

### Blackpillv2 host (now blackpill-f401cc, blackpill-f401ce and blackpill-f411ce, aka “The Blackpill hosts”)

- Implemented support for target power voltage sensing [lenvm]
- Redid the pinout for the platform to rationalise it - see #1465 for details on the new pinout [lenvm]
- Created an alternative pinout for the platform - see #1467 for details on this alternative pinout [lenvm]
- Restructured and renamed the platform, adding support for all current Blackpill variants [lenvm]
- Fixed a typo in the platform README [lenvm]
- Fixed and improved support and handling for using the in-tree DFU bootloader and the boot ROM DFU bootloader on the platform [ALTracer]
- Fixed the tpwr control implementation for the platform being inverted (”enable” meant off, “disable” meant on) [lenvm]
- Implemented the platform backend for support for the SPI remote protocol [ALTracer]

### Black Magic Debug App (aka “PC Host”)

- Fixed how target selection and memory access works on the CMSIS-DAP backend [dmsc]
- Implemented a structure for holding information about discovered probes [dragonmux]
- Use the correct header for memory allocation functions in the probe information implementation [tlyu]
- Fixed a include path problem with libusb [sidprice]
- Fixed the implementation of target power control [sidprice]
- Dead code removal in `cl_execute()` [sidprice]
- Updated and modernised the CMSIS-DAP implementation and reorganised [dragonmux]
- Fixed the FTDI implementation and a discovery issue with Tigard [dragonmux]
- Addressed several naming inconsistencies in the BMP remote protocol SWD implementation [dragonmux]
- Implemented support for compiling on cygwin [hydra]
- Reimplemented the BMP remote protocol and implemented proper protocol feedbacks for older versions of the protocol [dragonmux]
- Fixed an issue in the ST-Link backend which results in a crash when trying to read a single byte from a target [dragonmux]
- Fixed building on macOS [lenvm]
- Fixed handling for selecting between multiple identical CMSIS-DAP devices [zyp]
- Simplified the ST-Link and J-Link USB access code [zyp]
- Fixed an regression in the remote protocol write length alignment calculations [dragonmux]
- Rewrote the J-Link backend, fixing several ASAN crashes and lack of error handling [dragonmux]
- Improved the consistency of the backends and partially harmonised the nomoenclature used [dragonmux]
- Implemented a CMSIS-DAP quirks system and version check for ORBTrace due to older gateware having broken JTAG multi-TAP [dragonmux]
- Fixed CMSIS-DAP version identification when the version string has a ‘v’ suffix [dragonmux]
- Fixed an issue with how debug output is implemented on Windows that results in garbage being displayed for strings [dragonmux]
- Rebuild the probe detection and scan engine [sidprice]
- Implemented a libftdi-like shim layer for FTD2xx on Windows to allow native access to FTDI devices [sidprice]
- Fixed a long-standing issue with original ST-Link v2 serial number readout being broken [dragonmux]
- Fixed a regression where devices implementing CMSIS-DAP v2 would have their v2 interfaces be ignored [dragonmux]
- Implemented a workaround for Darwin (macOS, iOS) not implementing the Unicode character types (uchar.h) header [amyspark]
- Fixed an issue with CMSIS-DAP transfer failure handling that lead to some targets getting upset [dragonmux]
- Implemented target power handling for the J-Link backend and cleaned up in the backend [perigoso]
- Reworked the J-Link backend’s handling of the adaptor hardware version code [perigoso]
- Cleaned up after the implementation of the new probe discovery engine [dragonmux]
- Fixed a regression in the J-Link backend’s handling of frequency setting [dragonmux]
- Fixed a bug in the CMSIS-DAP implementation’s handling of WAIT which resulted in FAULT being generated on some targets and scan failing [dragonmux]
- Refactored and improved handling of VID:PID wildcards for J-Links [perigoso]
- Rewrote the ST-Link backend to fix how multi-drop is handled and solve several crashes [dragonmux]
- Fixed a regression in the CMSIS-DAP backend for v1 (HID) interfaces that broke writes with long buffers [projectgus]
- Added support for J-Link v5 adaptors by honouring the capability bits of J-Link devices [ALTracer]
- Fixed a memory leak and handling issue with FTDI adaptors in the probe detection and scan engine [lethalbit]

## Contributors to v1.10.0

We have had 42 individuals contribute 1208 commits since the v1.9.2 release.

Contributor (Contributions)  
dragonmux (872)  
perigoso (111)  
Sid Price (37)  
lenvm (37)  
ALTracer (28)  
Uwe Bonnes (20)  
James Turton (20)  
Sean Cross (13)  
Vegard Storheil Eriksen (10)  
Jean-Christian de Rivaz (6)  
Sascha Silbe (5)  
Maciej 'vesim' Kuliński (5)  
Koen De Vleeschauwer (4)  
Lars Sundström (3)  
TheyCallMeNobody (2)  
Stoyan Shopov (2)  
Piotr Esden-Tempski (2)  
Gareth McMullin (2)  
Francois Berder (2)  
dpf (2)  
Daniel Serpell (2)  
Andras Gemes (2)  
Amy (2)  
Aki Van Ness (2)  
Vitaliy (1)  
Thomas Bénéteau (1)  
Taylor Yu (1)  
Sludge (1)  
Siddharth Bharat Purohit (1)  
SG (1)  
Qyriad (1)  
Matthew Via (1)  
Kamil Rogozinski (1)  
Jonathan Giles (1)  
Jeremy Elson (1)  
iysheng (1)  
Guillaume Revaillot (1)  
franzflasch (1)  
Fabrice Prost-Boucle (1)  
Angus Gratton (1)  
AnantaSrikar (1)


## Sponsors

This project is sponsored in parts by:

- [1BitSquared](https://1bitsquared.com/) - Design, Manufacture and distribution of open source embedded hardware development tools and platforms, as well as educational electronics. Thank you everyone who buys Black Magic Probes from 1BitSquared directly through our [stores](https://1bitsquared.com/products/black-magic-probe) or indirectly through [Adafruit](https://www.adafruit.com/product/3839). The hardware sales allow us to continue supporting the [Black Magic Debug](https://black-magic.org) project.
- All the generous [Patrons](https://www.patreon.com/1bitsquared) and [GitHub Sponsors](https://github.com/sponsors/esden) supporting esden’s work
- All the generous [GitHub Sponsors](https://github.com/sponsors/dragonmux) supporting dragonmux’s work
