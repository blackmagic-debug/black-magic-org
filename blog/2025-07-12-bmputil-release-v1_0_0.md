# bmputil V1.0.0 Stable Release

```{post} July 19, 2025
:author: esden
```

We are happy to announce the [v1.0.0](https://github.com/blackmagic-debug/bmputil/releases/tag/v1.0.0) first stable release of [Black Magic Probe Utility](https://github.com/blackmagic-debug/bmputil)!

This is the first full release of the tool, and comes with pre-built binaries available in the release assets below, and is compatible with `cargo binstall`.

# Installation

You can find the [installation instructions in the project README](https://github.com/blackmagic-debug/bmputil/tree/v1.0.0?tab=readme-ov-file#installation).

# Usage

Please refer to our [website for usage instructions](https://black-magic.org/upgrade.html).

## Command Line Interface improvements

In this release we introduce a big Command Line Interface (aka. CLI) change. The program was renamed from `bmputil` to `bmputil-cli` to allow us to expand application types in the future without having to break the interface in the future.

The existing functions of `bmputil-cli` are moved into `probe` command namespace, and we reserved additional `target`, `server`, `debug` namespaces for future use. This change is also in service of future proofing the CLI. We have mid term plans to add a bunch more functionality to bmputil and we want to avoid breaking the interface while doing that.

The behaviour of `probe update` and `probe switch` have also changed slightly.

`probe update` is now automatically checking the active firmware version on the attached Black Magic Probe and executes an update if there is a new version available. It can still flash an arbitrary firmware binary by passing the firmware file name to the command. It also can update to a release candidate of the firmware by providing a `--use-rc` override, and an update can be forced with `--force` even if the tool considers the probe as being fully up to date.

The `probe switch` command now only functions as a *firmware variant* selector. *firmware variants* are being introduced in Black Magic Firmware V2.0 series allowing the partitioning of firmware functionality to work around the flash size limitation of the Black Magic Probe hardware.

Following is a screenshot of the tool called without any parameters to illustrate what namespaces mean.
<img width="664" height="286" alt="Screenshot 2025-07-12 at 9 35 04 PM" src="https://github.com/user-attachments/assets/a44abe13-e18d-4da8-851c-fc679f1cdd0c" />


## In this release

* Updated the dependencies to mitigate a few having become outdated and fix build issues that arose [dragonmux]
* Implemented automated firmware download, using the new summon-blackmagic metadata service [dragonmux]
* Switched USB implementations from rusb to nusb - this should improve the reliability of the tool [dragonmux]
* Switched error handlers to color-eyre, providing much richer and coloured error reports you can provide to us [dragonmux]
* Implemented a guided firmware selection system to improve management of the firmware on a probe [dragonmux]
* Improved the UX for the tool in general, making things more polished and easier to work with [dragonmux]
* Fixed a spurious STALL error being emitted under Linux by the utility when it should be suppressed [dragonmux]
  * The STALL condition is real, but also not erroneous so should not prevent forward progress from the tool
* Overhauled the project's README and updated it to more accurate reflect what tool does and is [dragonmux]
* Fixed a spurious disconnect error being emitted under Windows by the utility [dragonmux]
  * The STALL condition is real, but also not erroneous so should not prevent forward progress from the tool
* Fixed the parsing of the firmware's identity string as it was breaking the string down slightly incorrectly [P-Storm]
* Restructured the tool's CLI, converting the style of the parser and moving commands around for better consistency and structure [dragonmux]
* Fixed several clippy lints and the code base formatting using rustfmt nightly [dragonmux/lethalbit]
* Implemented handling for `probe info --list-targets` and introduced BMD remote serial protocol support
* Implemented better `probe update` control, allowing a user to force a firmware change and ask the tool to consider using RC's as well as full releases [dragonmux]
* Implemented better upgrade diagnostics following on from the better `probe update` controls [dragonmux]
* Fixed an issue with product string parsing on bootloader strings, resulting in errors/crashes in those cases [dragonmux]
* Moved the suppressions to a more suitable layer and applied them + fixed reboot behaviour across all places DFU_DETACH can be generated [dragonmux]
* Unit tested and reworked some of the logic for the URI building for the firmware index machinary [P-Storm]
* Reconfigured the releases for use with `cargo binstall` and switch the install instructions over to that from `cargo install` [esden]
* Fixed an error in the USB DFU machinery that had it using the wrong byte of a descriptor in an error [P-Storm]
* Improved the help displays to include the tool version information, as well as crash error displays to help users with reporting issues [dragonmux]
* Reorganised the probe matching machinery into its own file, and cleaned up the implementation [P-Storm]

## Contributors to v1.0.0

We have had 3 individuals contribute 309 commits since the v0.1.3 release.

Contributor (Contributions)

dragonmux (281)  
P-Storm (22)  
Piotr Esden-Tempski (6)

## **Sponsors**

This project is sponsored in parts by:

- [1BitSquared](https://1bitsquared.com/) - Design, Manufacture and distribution of open source embedded hardware development tools and platforms, as well as educational electronics. Thank you everyone who buys Black Magic Probes from 1BitSquared directly through our [stores](https://1bitsquared.com/products/black-magic-probe) or indirectly through [Adafruit.](https://www.adafruit.com/product/3839) The hardware sales allow us to continue supporting the Black Magic Debug project.
- All the generous [Patrons](https://www.patreon.com/1bitsquared) and [GitHub Sponsors](https://github.com/sponsors/esden) supporting esden’s work
- All the generous [GitHub Sponsors](https://github.com/sponsors/dragonmux) supporting dragonmux’s work