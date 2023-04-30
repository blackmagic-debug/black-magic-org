# Firmware Upgrade

## bmputil

Download or compile the Black Magic Debug (BMD) firmware. Regarding firmware selection:

* You can find the newest pre-built binaries on the [GitHub Release Page](https://github.com/blackmagic-debug/blackmagic/releases).
* You can find the bleeding cutting edge binaries uploaded as assets on the ["build and upload" GitHub actions page](https://github.com/blackmagic-debug/blackmagic/actions/workflows/build-and-upload.yml), Click on the newest successful build and download the `blackmagic-firmware.zip` file. It contains binaries for all the supported platforms.
* When using the daily builds expect breaking changes. Please report issues on [our issue page](https://github.com/blackmagic-debug/blackmagic/issues) or ask on our Discord server.

Clone and build the [bmputil](https://github.com/blackmagic-debug/bmputil) tool.

Plug in your Black Magic Probe and run the following command:

```bash
bmputil flash blackmagic-native.elf
```

### Linux / macOS

Provided you have suitable udev rules in play, this will already do everything you need and automatically reboot your unit back into the new firmware.

### Windows

bmputil will automatically take care of the needed drivers.
Do **not** run Zadig on the DFU endpoint if using bmputil.

## dfu-util

Download or compile the Black Magic Debug (BMD) firmware.
As with the [bmputil](#bmputil) section above, the same considerations exist with this method for firmware selection.

### Linux / macOS

You will need to install [`dfu-util`](http://dfu-util.sourceforge.net/) package. On macOS you can use homebrew, macports or fink depending on your preferred package manager. You will need version 0.8.0 or greater to support the dfuse commands.

Plug in the Black Magic Probe into your computer and run the following command:

```bash
sudo dfu-util -d 1d50:6018,:6017 -s 0x08002000:leave -D blackmagic-native.bin
```

### Windows

You will need to download the Windows release of [`dfu-util`](http://dfu-util.sourceforge.net/) package.

Plug in the Black Magic Probe into your computer and run the following command:

```bash
dfu-util.exe -d 1d50:6018,:6017 -s 0x08002000:leave -D blackmagic.bin
```

You may need use [Zadig](https://tracker.iplocation.net/icsj/) to install the WinUSB driver. Both PID 0x6017 and 0x6018 need to be known to  [Zadig](https://tracker.iplocation.net/icsj/).

```{note}
On first run Zadig may not see the 6017 PID. Once the dfu exe runs and detaches the device, it should appear in Zadig. Install the WinUSB driver on it and re-run the dfu exe.
```

### Closing remarks

To upgrade non-native hardware see the readme of the different [platforms on GitHub](https://github.com/blackmagic-debug/blackmagic/tree/main/src/platforms).

```{note}
If `dfu-util` fails to switch your BMP into bootloader mode, or you feel like you might have **bricked** your BMP, you can also plug in your BMP while holding down the button. This will force the BMP to stay in the bootloader on power up.
```

## stlink-tool

An ST-Link can be used to upate the firmware using [stlink-tool](<https://github.com/jeanthom/stlink-tool>).

```bash
stlink-tools blackmagic.bin
```
