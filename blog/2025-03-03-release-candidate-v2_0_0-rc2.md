# Black Magic Debug V2.0.0-rc2 Release Candidate

```{post} March 03, 2025
:author: esden
```

We are happy to announce the second [v2.0.0 release candidate](https://github.com/blackmagic-debug/blackmagic/releases/tag/v2.0.0-rc2) of [Black Magic Debug](https://black-magic.org). This is the first major release of the v2 series.

## In **this release**
- Fixed a mistake in the name of the `mscratch` CSR for RISC-V [ALTracer]
- Implemented better control of the nTRST and TCK/SWCLK pin modes on the Black Pill platforms [ALTracer]
- Fixed a bug in STM32WL55 discovery and an error recovery issue [dragonmux]
- Updated the contribution guidelines for the project to clarify the stance on LLM/”AI” generated contributions [dragonmux]
- Fixed an issue with support for 64-bit break/watch points [marysaka]
- Fixed some shortcomings in BMDA’s CMSIS-DAP backend’s nRST control implementation [dragonmux]
- Fixed a sector calculation bug causing erase to go wrong on STM32H5 parts [dragonmux]
- Treat the GD32E5 series JTAG-DP as ADIv5 [ALTracer]
- Globally enable GDB noackmode support by default [perigoso]
- Fixed a bug in ADIv5/v6 JTAG DP version handling which broke DPv1-2 parts [dragonmux]
- Make sure the bootloader LED is only set up once on the Black Pill platforms [lenvm]
- Formally parse the `misa` register to form the CPU string on RISC-V targets [perigoso]
- Fix Cortex-M4 core detection for the i.MXRT1176 [litui]
- Re-introduced the SHIELD selection build option for the Meson build system on Back Pill platforms [lenvm]
- Fixed an issue in GDB noackmode state handling that would cause a kind of “zombie” state [perigoso]
- Corrected a mistake on the Black Pill platforms in the conditional compilation macro name used for the bootloader LED pin [sidprice]
- Documented the `on_carrier_board` option for the Black Pill platforms [sidprice]
- Fixed an issue in discovery of v2 device info pages on EFM32 parts [mmmspatz]
- Corrected the initialisation and control of the nRST pin on the Black Pill platforms [ALTracer]
- Fixed an issue on the Black Pill and ST-Link v3 platforms with slew rates not scaling with frequency selection leading to SI problems in poor setups [ALTracer]
- Switched the default target clock speed on the Black Pill platforms to 2MHz [birkenfeld]

## **Contributors to v2.0.0-rc2**
We have had 6 individuals contribute 47 commits since the v2.0.0-rc1 release candidate.

Contributor (Contributions)  
dragonmux (14)  
perigoso (13)  
ALTracer (10)  
Sid Price (2)  
Mary Guillemard (2)  
lenvm (2)  
Aria Burrell (2)  
Mark H.Spatz (1)  
Georg Brandl (1)

## **Sponsors**

This project is sponsored in parts by:

- [1BitSquared](https://1bitsquared.com/) - Design, Manufacture and distribution of open source embedded hardware development tools and platforms, as well as educational electronics. Thank you everyone who buys Black Magic Probes from 1BitSquared directly through our [stores](https://1bitsquared.com/products/black-magic-probe) or indirectly through [Adafruit.](https://www.adafruit.com/product/3839) The hardware sales allow us to continue supporting the Black Magic Debug project.
- All the generous [Patrons](https://www.patreon.com/1bitsquared) and [GitHub Sponsors](https://github.com/sponsors/esden) supporting esden’s work
- All the generous [GitHub Sponsors](https://github.com/sponsors/dragonmux) supporting dragonmux’s work