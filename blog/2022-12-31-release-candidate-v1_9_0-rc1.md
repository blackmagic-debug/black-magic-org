# Release Candidate V1.9.0-rc1

```{post} December 31, 2022
:author: esden
```

We are happy to announce the second [V1.9.0 release candidate](https://github.com/blackmagic-debug/blackmagic/releases/tag/v1.9.0-rc1) of [Black Magic Debug](https://black-magic.org).

## In this release

- Fixed an error in BMDA’s DAP link reset logic [zyp]
- Fixed the USB serial port control notifications (such as DTR) being sent over the wrong endpoint [dragonmux]
- Fixed the CRC32 calculations being broken in BMDA and non-STM32 probes [perigoso]
- Fixed a regression in the identification of STM32F0 parts [dragonmux]
- Fixed a regression in the `HOSTED_BMP_ONLY=1` build of BMDA for Windows due to mishandling a possible return value form `RegGetValue()` [LAK132]
- Fixed the nRF52 target support being able to trigger probe memory exhaustion due to the size of the write buffers [dragonmux]
- Fixed a `NULL` pointer dereference issue in the RTT monitor command when no arguments are given [koendv]
- Corrected the part lookup for STM32F4 series and adjacent parts [perigoso]
- Added a second set of symlinks to the udev rules to handle when multiple probes are attached to one host properly [dragonmux]
- Added a missing `NULL` check in `target_flash_erase` [perigoso]
- Fixed the BMDA build on OSX [djix123]
- Fixed the Cortex-M SWD attach regression that occurs when there is a delay between scan and attach [dragonmux]
- Fixed the target register description allocation inducing memory exhaustion and not being reliably cleaned up [dragonmux]
- Fixed compilation of the DFU bootloaders under some ARM GCC toolchains [dragonmux]
- Fixed a regression in BMDA’s file handling which caused Flash write and verify operations to be no-ops [hollinsky]
- Implemented a monitor command to allow clean BMDA shutdowns [dragonmux]
- Fixed dap_jtagtap_tdi_tdo_seq() crashing when ticks is 0 and final_tms is true [dragonmux]

## Contributors to v1.9.0-rc1

We have had 8 individuals contribute 97 commits to the v1.9.0-rc1 release. It would not have been possible without your help! Thank you!

Contributor (Contributions)  
dragonmux (86)  
Rafael Silva (3)  
Jonathan Giles (2)  
Paul Hollinsky (2)  
Vegard Storheil Eriksen (1)  
Koen De Vleeschauwer (1)  
LAK132 (1)  
Piotr Esden-Tempski (1)

## Sponsors

This project is sponsored in parts by:

- [1BitSquared](https://1bitsquared.com/) - Design, Manufacture and distribution of open source embedded hardware development tools and platforms, as well as educational electronics. Thank you everyone who buys Black Magic Probes from 1BitSquared directly through our [stores](https://1bitsquared.com/products/black-magic-probe) or indirectly through [Adafruit](https://www.adafruit.com/product/3839). The hardware sales allow us to continue supporting the [Black Magic Debug](https://black-magic.org) project.
- All the generous [Patrons](https://www.patreon.com/1bitsquared) and [GitHub Sponsors](https://github.com/sponsors/esden) supporting esden’s work
- All the generous [GitHub Sponsors](https://github.com/sponsors/dragonmux) supporting dragonmux’s work
