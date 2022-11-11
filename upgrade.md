# Firmware Upgrade

## Linux / MacOS

### dfu-util

Download or compile a Black Magic Debug (BMD) firmware. Regarding firmware selection:

* You can find the newest pre-built binaries on the [GitHub Release Page](https://github.com/blackmagic-debug/blackmagic/releases).
* You can find the bleeding cutting edge binaries uploaded as assets on the ["build and upload" GitHub actions page](https://github.com/blackmagic-debug/blackmagic/actions/workflows/build-and-upload.yml), Click on the newest successful build and download the `blackmagic-firmware.zip` file. It contains binaries for all the supported platforms.
* When using the daily builds expect breaking changes. Please report issues on [our issue page](https://github.com/blackmagic-debug/blackmagic/issues) or ask on our Discord server.

Plug in the Black Magic Probe into your computer and run the following command:

```bash
sudo dfu-util -d 1d50:6018,:6017 -s 0x08002000:leave -D blackmagic-native.bin
```

You will need to install [`dfu-util`](http://dfu-util.sourceforge.net/) package. On MacOS you can use homebrew, macports or fink depending on your preferred package manager. You will need version 0.8.0 or greater to support the dfuse commands.

```{note}
If `dfu-util` fails to switch your BMP into bootloader mode, or you feel like you might have **bricked** your BMP, you can also plug in your BMP while holding down the button. This will force the BMP to stay in the bootloader on power up.
```

## Windows

### dfu-util

Download or compile a Black Magic Probe (BMP) firmware.

Plug in the Black Magic Probe into your computer and run the following command:

```bash
dfu-util.exe -d 1d50:6018,:6017 -s 0x08002000:leave -D blackmagic.bin
```

You will need to download the Windows release of [`dfu-util`](http://dfu-util.sourceforge.net/) package.

You may need use [Zadig](https://tracker.iplocation.net/icsj/) to install the WinUSB driver. Both PID 0x6017 and 0x6018 need to be known to  [Zadig](https://tracker.iplocation.net/icsj/).

```{note}
On first run Zadig may not see the 6017 PID. Once the dfu exe runs and detaches the device, it should appear in Zadig. Install the WinUSB driver on it and re-run the dfu exe.
```

```{note}
If `dfu-util` fails to switch your BMP into bootloader mode, or you feel like you might have **bricked** your BMP, you can also plug in your BMP while holding down the button. This will force the BMP to stay in the bootloader on power up.
```

## Using stm32-mem.py

An alternative solution is using `stm32_mem.py` script included in the Black Magic Debug source repository. It is not the recommended way of updating the Black Magic Probe as `dfu-util` is easier to install without the need to clone the Black Magic Debug repository and all the associated source code.

```bash
cd blackmagic && scripts/stm32_mem.py blackmagic.bin
```

### Built-in Upgrade tool

Instructions for Linux in [hacking section](https://github.com/blacksphere/blackmagic/wiki/Hacking#updating-firmware)
