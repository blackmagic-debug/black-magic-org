# Compiling on Windows

This guide covers the following:

* [Building the firmware on a Windows machine](#building-the-firmware-on-a-windows-machine)
* [Building BMDA on a Windows machine](#building-bmda-on-a-windows-machine)

Note: The BMDA guide defines the supported (but not only) way to build BMDA for Windows.

## Building the firmware on a Windows machine

To build the firmware on Windows you will need the following minimum requirements:

* The [ARM GNU Toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads) compiler suite for bare metal
* A POSIX-compliant shell such as Bash
* Git for Windows, if building from the repository instead of a release

The easiest way to get to a working setup is to use:

* [MSYS2](https://www.msys2.org/) and follow the installation guide
* [ARM GNU Toolchain release 12.2.Rel1](https://developer.arm.com/-/media/Files/downloads/gnu/12.2.rel1/binrel/arm-gnu-toolchain-12.2.rel1-mingw-w64-i686-arm-none-eabi.zip?rev=709f3f15b2ee4763b186c10153ee6ca9&hash=8C0761A17A1E4861B96DDB604C177F5B)

### Setting up the firmware build environment

Having installed MSYS2 and with the toolchain Zip file downloaded to the Downloads directory in your user profile area,
you will need to open the MSYS2 UCRT64 prompt from the start menu.
That is the prompt item with this icon: ![UCRT64 icon](../_assets/ucrt64.png){width=32 height=32}

Inside the MSYS2 environment run the following to update the environment and follow all prompts provided:

```bash
pacman -Syu
pacman -S pactoys git unzip
pacboy -S python:p make:p
unzip $USERPROFILE/Downloads/arm-gnu-toolchain-12.2.rel1-mingw-w64-i686-arm-none-eabi.zip -d .
export PATH=$HOME/arm-gnu-toolchain-12.2.rel1-mingw-w64-i686-arm-none-eabi/bin:$PATH
```

At this point you will have the tools required to build the firwmare and they will all be available from the shell.
It is important that all further steps be performed in this same shell, or if you do open a new one, that you
run the final line of this setup on each new shell you use.

### Acquiring the source

You have a choice at this point:

* of either grabbing down a release from the project's GitHub repositories, or
* cloning the main repository.

#### From release Zip file

If you want to use a release, visit [the project release index](https://github.com/blackmagic-debug/blackmagic/releases)
and download the "Source code (zip)" entry's file from the release's assets, saving the file in your downloads as
`blackmagic.zip`.

You can then extract this file in a usable form by running:

```bash
unzip $USERPROFILE/Downloads/blackmagic.zip
```

This will make a directory of the source tree named following the release's version string - for example,
for v1.10.0-rc0 the directory is named `blackmagic-1.10.0-rc0`. You will then need to change directory into this, eg:

```bash
cd blackmagic-1.10.0-rc0
```

#### From repository clone

If you wish to use a source clone, run the following to get set:

```bash
git clone https://github.com/blackmagic-debug/blackmagic
cd blackmagic
```

### Building for a probe

Now you are in a copy of the source tree for BMD, you can build the source for your probe of choice. Use the
platform README.md for the probe as a guide for any differences to the below steps.

NB: If you are building the firmware for a Blue Pill and your device does not fit one the descriptions of any in the
`swlink` platform, you must use the `stlink` platform and defined `BLUEPILL=1` in the `make` step.

To build the firmware and update your probe, assuming you've already acquired `bmputil` per the
[upgrading instrucitons](../upgrade.md):

```bash
mingw32-make PROBE_HOST=native
bmputil flash src/blackmagic.elf
```

The `make` step will automatically clone and build libopencm3, which is one of the firmware's dependencies.
The resulting output of this step are 4 files:

* `src/blackmagic.elf` - The firmware main binary w/ debug and address space information
* `src/blackmagic.bin` - The firmware's .text and .data sections objcopy'd into a bare file
* `src/blackmagic_dfu.elf` - The project's bootloader w/ debug and address space information
* `src/blackmagic_dfu.bin` - The project bootloader's .text and .data sections in a bare file

When the upgrade step completes, your probe will be automatically rebooted into the new firmware and be ready to go.

If you wish to build the project for a different platform or do a BMDA build, you must run `mingw32-make clean`
between builds to remove the incompatible build outputs.

## Building BMDA on a Windows machine

To build BMDA on Windows you will need a MSYS2 environment - please go to the [MSYS2](https://www.msys2.org/) project
and follow the installation guide.

### Setting up the build environment

Having installed MSYS2, you will need to open the MSYS2 UCRT64 prompt from the start menu.
That is the prompt item with this icon: ![UCRT64 icon](../_assets/ucrt64.png){width=32 height=32}

Inside the MSYS2 environment run the following to update the environment and follow all prompts provided:

```bash
pacman -Syu
pacman -S pactoys git unzip
pacboy -S python:p make:p toolchain:p libusb:p hidapi:p
```

At this point you will have everything needed to build BMDA in the UCRT64 environment.

### Building BMDA

With the environment set up, you will need to acquire the source same as in the firmware build steps above.
Once you have the source, building BMDA is as easy as running:

```bash
mingw32-make PROBE_HOST=hosted HOSTED_BMP_ONLY=0
```

If you wish to build BMDA for only talking to BMP, the `HOSTED_BMP_ONLY=0` may be dropped.

After the `make` step, you will have a file - `src/blackmagic.exe`, you can execute this by running `src/blackmagic`.
This is the BMDA binary. When you run `mingw32-make clean` in the sources, this file will be kept behind. This is done
to allow you to build BMDA, then the firmware, and then have both to use simultaneously.

You may not want to require users to have an MSYS2 environment to use `blackmagic.exe`.

In that case, all you need to do is copy the following files to a directory of
your choosing:

```bash
# Optional - strip the executable to minimize it
strip src/blackmagic.exe

cp src/blackmagic.exe             /c/path/to/project
cp 3rdparty/ftdi/amd64/ftd2xx.dll /c/path/to/project
cp /ucrt64/bin/libusb-1.0.dll     /c/path/to/project
cp /ucrt64/bin/libhidapi-0.dll    /c/path/to/project
```

Note: The file paths above assume you are still in the MSYS2 UCRT64 prompt.

Now you can run `c:\path\to\project\blackmagic` from the Windows commandline or shortcut.
