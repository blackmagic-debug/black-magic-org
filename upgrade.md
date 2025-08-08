# Firmware Upgrade

There are many ways to update your Black Magic Probe. For most users the stable release firmware will be sufficient and
in most cases will not require to compile anything. We recommend updating the firmware using `bmputil`. It is also
possible to use `dfu-util` that used to be the recommended way in the past, you can find the instructions for *other*
tools at the end of this document. If you have trouble using `bmputil` please let us know, we strive to make the
experience as easy as possible.

## Install bmputil-cli

Binary releases for Linux, mac OS (amd64/AArch64) and Windows (amd64/AArch64) are now available with every
[release](https://github.com/blackmagic-debug/bmputil/releases). These should work out-of-the-box with no
extra dependencies or software needing to be installed.

Alternatively `cargo binstall` can be used. Which allows for easy updates of `bmputil-cli`.
We recommend the following order of operations:

* [Install rustup](https://rustup.rs/)
* [Install cargo-binstall](https://github.com/cargo-bins/cargo-binstall?tab=readme-ov-file#installation)
* Install bmputil by invoking
  * `cargo binstall bmputil` for the stable release
  * `cargo binstall bmputil@1.0.0-rc.2` for a release candidate

The tool will be available as `bmputil-cli` starting with v1.0.0 and `bmputil` for older releases.

Another alternative is to use `cargo install` instead of `cargo binstall` which will install the tool from source. In
such case `cargo-binstall` can be skipped in the instructions above. The `binstall` path will fall back to source
compilation if a binary build is not available for the specific os/architecture combination.

```{note}
If you decide to choose the `cargo install` path on Windows. Please refer to the
[detailed documentation about the process](knowledge/bmputil-on-windows.md) as it is not trivial.
```

`bmputil` on Windows will automatically setup driver installation on first run for a probe if appropriate.  This will
require administrator access when it occurs, and uses the Windows Driver Installer framework.

## Setup permissions

In case you are using Linux we highly recommend setting up the official project
[udev rules](https://github.com/blackmagic-debug/blackmagic/tree/main/driver).

```{warning}
On Windows `bmputil-cli` will automatically take care of the needed drivers.
Do **not** run Zadig on the DFU endpoint if using bmputil.
```

You can check if everything is working correctly by running:

```sh
bmputil-cli probe info
```

The tool should be able to find and list the Black Magic Probe connected to the system. Which will look something like
this:

```text
Found: Black Magic Probe 2.0.0
  Serial: 81C5797B
  Port:  0-85000192
```

## Automatic Update

This is the recommended procedure.

```{note}
This procedure is currently only supported by the [native](hardware.md#native-hardware) hardware. Third party
hardware running Black Magic Firmware is not currently supported and the appropriate firmware has to be manually built.
Refer to the [Manual Update](#manual-update) for instructions.
```

### Run update

To upgrade the firmware on the connected Black Magic Probe all that should be necessary is running:

```sh
bmputil-cli probe update
```

And follow the instructions.

If you would like to update the firmware to the latest release candidate you can run the following:

```sh
bmputil-cli probe update --use-rc
```

## Manual Update

This procedure is necessary when the host platform is not the native hardware. We currently do not offer an automatic
update path for third party hardware.

This is also the procedure to follow if you are have some other reason to build the firmware manually. For example you
are addinng new hardware support.

### Download or build the firmware

Download or compile the Black Magic Debug (BMD) firmware. Regarding firmware selection:

* You can find the newest pre-built binaries on the
  [GitHub Release Page](https://github.com/blackmagic-debug/blackmagic/releases).
* You can download cutting edge binaries built with every commit to the main branch
  [here](https://nightly.link/blackmagic-debug/blackmagic/workflows/build-and-upload/main).  When using the daily builds
* expect breaking changes. Please report issues on
  [our issue page](https://github.com/blackmagic-debug/blackmagic/issues) or ask on our Discord server.
* You can also build your own firmware from the cloned sources. Follow the [build instructions in the project
  README](https://github.com/blackmagic-debug/blackmagic?tab=readme-ov-file#building).

### Flash Using `bmputil`

To flash a downloaded or manually built binary, the resulting `.elf` file can be provided to the `bmputil-cli probe
update` command.

```sh
bmputil-cli probe update blackmagic-binary.elf
```

## Update using *other* tools

Besides `bmputil` you can also update the firmware on your Black Magic Probe using `dfu-util` or `stlink-tool`. Both can
be useful if you have trouble getting `bmputil` to work on your system, and/or your Black Magic host platform is not the
[native](hardware.md#native-hardware) and is not supported by `bmputil`.

### dfu-util on Linux/macOS

Install [`dfu-util`](http://dfu-util.sourceforge.net/). On macOS you can use homebrew, macports or fink depending
on your preferred package manager. You will need version 0.8.0 or greater to support the dfuse commands.

Plug the Black Magic Probe into your computer and run the following command:

```sh
sudo dfu-util -d 1d50:6018,:6017 -s 0x08002000:leave -D blackmagic-native.bin
```

To upgrade non-native hardware see the READMEs of the different
[platforms on GitHub](https://github.com/blackmagic-debug/blackmagic/tree/main/src/platforms).

```{note}
If `dfu-util` fails to switch your BMP into bootloader mode, or you feel like you might have **bricked** your BMP, you
can also plug in your BMP while holding down the button. This will force the BMP to stay in the bootloader on power up.
```

### stlink-tool on Linux/macOS

The firmware on an ST-Link can be upgraded using
[blackmagic-debug/stlink-tool](https://github.com/blackmagic-debug/stlink-tool).

To upgrade, run the following command:

```sh
stlink-tool blackmagic.bin
```

```{note}
This software upgrades the firmware of the ST-Link probe, **not** the firmware of a target connected to the probe.
Therefore please ensure you want to upgrade the firmware of the ST-Link probe, and use a blackmagic.bin file built
specifically for ST-Link.
```

### dfu-util on Windows

Download the Windows release of [`dfu-util`](http://dfu-util.sourceforge.net/).

Plug the Black Magic Probe into your computer and run the following command:

```sh
dfu-util.exe -d 1d50:6018,:6017 -s 0x08002000:leave -D blackmagic.bin
```

To upgrade non-native hardware see the readme of the different
[platforms on GitHub](https://github.com/blackmagic-debug/blackmagic/tree/main/src/platforms).

You may need use [Zadig](https://tracker.iplocation.net/icsj/) to install the WinUSB driver. Both PID 0x6017 and
0x6018 need to be known to [Zadig](https://tracker.iplocation.net/icsj/).

```{note}
On first run Zadig may not see the 6017 PID. Once the dfu exe runs and detaches the device, it should appear in
Zadig. Install the WinUSB driver on it and re-run the dfu exe.
```

```{note}
If `dfu-util` fails to switch your BMP into bootloader mode, or you feel like you might have **bricked** your BMP,
you can also plug in your BMP while holding down the button. This will force the BMP to stay in the bootloader on
power up.
```

### stlink-tool on Windows

The firmware on an ST-Link can be upgraded using
[blackmagic-debug/stlink-tool](https://github.com/blackmagic-debug/stlink-tool).

The linked repository is forked from [UweBonnes/stlink-tool](https://github.com/UweBonnes/stlink-tool), which in
turn is a fork from [jeanthom/stlink-tool](https://github.com/jeanthom/stlink-tool).

To upgrade, run the following command:

```sh
stlink-tool blackmagic.bin
```

```{note}
This software upgrades the firmware of the ST-Link probe, **not** the firmware of a target connected to the probe.
Therefore please ensure you want to upgrade the firmware of the ST-Link probe, and use a blackmagic.bin file built
specifically for ST-Link.
```
