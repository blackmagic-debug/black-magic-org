# Firmware Upgrade

## Linux / macOS

Download or compile the Black Magic Debug (BMD) firmware. Regarding firmware selection:

* You can find the newest pre-built binaries on the [GitHub Release Page](https://github.com/blackmagic-debug/blackmagic/releases).
* You can find the bleeding cutting edge binaries uploaded as assets on the ["build and upload" GitHub actions page](https://github.com/blackmagic-debug/blackmagic/actions/workflows/build-and-upload.yml), Click on the newest successful build and download the `blackmagic-firmware.zip` file. It contains binaries for all the supported platforms.
* When using the daily builds expect breaking changes. Please report issues on [our issue page](https://github.com/blackmagic-debug/blackmagic/issues) or ask on our Discord server.

Upgrade the firmware of the Black Magic Debug Probe using either:
- bmputil
- dfu-util
- stlink-tool

### bmputil

Clone and build the [bmputil](https://github.com/blackmagic-debug/bmputil) tool.

Plug your Black Magic Probe into your computer and run the following command:

```bash
bmputil flash blackmagic-native.elf
```

Provided you have suitable udev rules in play, this will already do everything you need and automatically reboot your unit back into the new firmware.

### dfu-util

Install [`dfu-util`](http://dfu-util.sourceforge.net/). On macOS you can use homebrew, macports or fink depending on your preferred package manager. You will need version 0.8.0 or greater to support the dfuse commands.

Plug the Black Magic Probe into your computer and run the following command:

```bash
sudo dfu-util -d 1d50:6018,:6017 -s 0x08002000:leave -D blackmagic-native.bin
```

To upgrade non-native hardware see the readme of the different [platforms on GitHub](https://github.com/blackmagic-debug/blackmagic/tree/main/src/platforms).

```{note}
If `dfu-util` fails to switch your BMP into bootloader mode, or you feel like you might have **bricked** your BMP, you can also plug in your BMP while holding down the button. This will force the BMP to stay in the bootloader on power up.
```

### stlink-tool

The firmware on an ST-Link can be upgraded using [blackmagic-debug/stlink-tool](https://github.com/blackmagic-debug/stlink-tool).

To upgrade, run the following command:

```bash
stlink-tool blackmagic.bin
```

```{note}
This software upgrades the firmware of the ST-Link probe, **not** the firmware of a target connected to the probe. Therefore please ensure you want to upgrade the firmware of the ST-Link probe, and use a blackmagic.bin file built specifically for ST-Link.
```

## Windows

Download or compile the Black Magic Debug (BMD) firmware. Regarding firmware selection:

* You can find the newest pre-built binaries on the [GitHub Release Page](https://github.com/blackmagic-debug/blackmagic/releases).
* You can find the bleeding cutting edge binaries uploaded as assets on the ["build and upload" GitHub actions page](https://github.com/blackmagic-debug/blackmagic/actions/workflows/build-and-upload.yml), Click on the newest successful build and download the `blackmagic-firmware.zip` file. It contains binaries for all the supported platforms.
* When using the daily builds expect breaking changes. Please report issues on [our issue page](https://github.com/blackmagic-debug/blackmagic/issues) or ask on our Discord server.

Upgrade the firmware of the Black Magic Debug Probe using either:
- bmputil
- dfu-util
- stlink-tool

### bmputil

Clone and build the [bmputil](https://github.com/blackmagic-debug/bmputil) tool.

Plug your Black Magic Probe into your computer and run the following command:

```bash
bmputil flash blackmagic-native.elf
```

bmputil will automatically take care of the needed drivers.
Do **not** run Zadig on the DFU endpoint if using bmputil.

### dfu-util

Download the Windows release of [`dfu-util`](http://dfu-util.sourceforge.net/).

Plug the Black Magic Probe into your computer and run the following command:

```bash
dfu-util.exe -d 1d50:6018,:6017 -s 0x08002000:leave -D blackmagic.bin
```

To upgrade non-native hardware see the readme of the different [platforms on GitHub](https://github.com/blackmagic-debug/blackmagic/tree/main/src/platforms).

You may need use [Zadig](https://tracker.iplocation.net/icsj/) to install the WinUSB driver. Both PID 0x6017 and 0x6018 need to be known to [Zadig](https://tracker.iplocation.net/icsj/).

```{note}
On first run Zadig may not see the 6017 PID. Once the dfu exe runs and detaches the device, it should appear in Zadig. Install the WinUSB driver on it and re-run the dfu exe.
```

```{note}
If `dfu-util` fails to switch your BMP into bootloader mode, or you feel like you might have **bricked** your BMP, you can also plug in your BMP while holding down the button. This will force the BMP to stay in the bootloader on power up.
```

### stlink-tool

The firmware on an ST-Link can be upgraded using [dragonmux/stlink-tool](https://github.com/dragonmux/stlink-tool/tree/feature/compilation-fixes).

The linked repository is forked from [UweBonnes/stlink-tool](https://github.com/UweBonnes/stlink-tool), which in turn is a fork from [jeanthom/stlink-tool](https://github.com/jeanthom/stlink-tool). The link points to a specific branch named `feature/compilation-fixes`. Please ensure to checkout to to this branch after cloning the repository, as both UweBonnes and dragonmux have made fixes that are not included in the repository by jeanthom.


To upgrade, run the following command:

```bash
stlink-tool blackmagic.bin
```

```{note}
This software upgrades the firmware of the ST-Link probe, **not** the firmware of a target connected to the probe. Therefore please ensure you want to upgrade the firmware of the ST-Link probe, and use a blackmagic.bin file built specifically for ST-Link.
```
