# Black Magic Debug V1.10.0-rc1 Release Candidate

```{post} October 11, 2023
:author: esden
```

We are happy to announce the second [V1.10.0 release candidate](https://github.com/blackmagic-debug/blackmagic/releases/tag/v1.10.0-rc1) of [Black Magic Debug](https://black-magic.org).

This will be the final minor release of the v1 series.

# In this release

- Fixed RTT hanging the firmware when the aux serial port is not being monitored on the host [koendv]
- Fixed a bug in the firmware-side remote protocol initialisation logic that can in certain circumstances lead to the firmware crashing during remote protocol operations [dragonmux]
- Updated documentation and comments to reflect the cleaned up and improved SWD support nomenclature [perigoso]
- Improved the Cortex-A support and its ability to function on the same AP as a Cortex-M core [dragonmux]
- Improved handling of the OS Lock registers on Cortex-A targets to handle if the lock gets set between resumption and the next halt [dragonmux]
- Added suport for variants other than the i.MXRT1060 [tannewt]
- Fixed handling of old SFDP basic parameter tables which lack the field for the page program size [tannewt]
- Fixed the Cortex-A cores on the STM32MP15x inducing a hang on scan and probe [ALTracer]
- Fixed a crash in the LPC40xx probe routine during probe of unrelated Cortex-M4 targets that have FPUs [desertsagebrush]
- Introduced a workaround for buggy Tiva-C devices that result in the device answering for all AP numbers, leading to 256 target entries for a device that should have just one [desertsagebrush]
- Added support for ST Micro’s STM32MP15x SoCs (Cortex-M4 coprocessor core only) [ALTracer]
- Reduced the Flash usage caused by the new soft-start feature on the native platform [dragonmux]
- Added pinout documentation to the ST-Link platform README.md [dragonmux]
- Improved the clarity and documentation of the FTDI interface state structure and usage [dragonmux]
- Fixed a bug in BMDA’s ADIv5 access decoding for the protocol log level that caused AP accesses to always be reported as being for AP1 [dragonmux]

## Contributors to v1.10.0-rc1

We have had 6 individuals contribute 52 commits since the v1.10.0-rc0 release.

Contributor (Contributions)
dragonmux (22)  
ALTracer (13)  
Scott Shawcroft (6)  
perigoso (6)  
Sage Myers (3)  
Koen De Vleeschauwer (2)

## Sponsors

This project is sponsored in parts by:

- [1BitSquared](https://1bitsquared.com/) - Design, Manufacture and distribution of open source embedded hardware development tools and platforms, as well as educational electronics. Thank you everyone who buys Black Magic Probes from 1BitSquared directly through our [stores](https://1bitsquared.com/products/black-magic-probe) or indirectly through [Adafruit](https://www.adafruit.com/product/3839). The hardware sales allow us to continue supporting the Black Magic Debug project.
- All the generous [Patrons](https://www.patreon.com/1bitsquared) and [GitHub Sponsors](https://github.com/sponsors/esden) supporting esden’s work
- All the generous [GitHub Sponsors](https://github.com/sponsors/dragonmux) supporting dragonmux’s work