# GDB Flash Automation

In many cases it is useful to automatically flash and test the uploaded firmware. GDB has a built in scripting language as well as python bindings.

Here is a collection of a few ways to automate the flashing process.

There are many ways to accomplish this.

## Commandline
For example with the following "one liner":
```sh
arm-none-eabi-gdb -nx --batch \
  -ex 'target extended-remote /dev/ttyACM0' \
  -ex 'monitor swdp_scan' \
  -ex 'attach 1' \
  -ex 'load' \
  -ex 'compare-sections' \
  -ex 'kill' \
  yourbinary.elf
```

```{note}
Remember that `/dev/ttyACM0` is only valid on linux, you will need to use `COMx` for windows and `/dev/cu.usbmodemXXXXXXX1` for Mac OS.
```
```{note}
As always you can use `monitor jtag_scan` instead of `monitor swdp_scan` to use JTAG protocol instead of SWD.
```
```{note}
In cases when the target is not powered or you don't have the VREF pin connected you will need to add `monitor tpwr enable` to enable power to the target side of the level translators. (especially important for BMP V2.0 and V2.1 probes)
```

The above invocation can be simplified if you put most of the `-ex` commands into a GDB script file. You can create a file named for example `black_magic_probe_flash.scr` with the following content:

```
#monitor jtag_scan
monitor swdp_scan
attach 1
load
compare-sections
kill
```

Then the above invocation shrinks down to the following:

```sh
arm-none-eabi-gdb -nx --batch \
  -ex 'target extended-remote /dev/ttyACM0' \
  -x black_magic_probe_flash.scr \
  yourbinary.elf
```

## Makefile

If you are using GNU Makefiles for your project you can add a `make flash` target. Reusing the script from the [Commandline](#commandline) section above the target like that can look something like this:

```make

flash: yourbin.flash

BMP_PORT ?= /dev/ttyACM0

%.flash: %.elf
	@printf "  BMP $(BMP_PORT) $(*).elf (flash)\n"
	$(Q)$(GDB) -nx --batch \
	           -ex 'target extended-remote $(BMP_PORT)' \
	           -x black_magic_probe_flash.scr \
	           $(*).elf

```

This is a very simple flash target. It assumes that your binary target ends with `.elf` suffix. You can call the target by running `make flash` and it will build the `yourbinary.elf`, flash it and test that the flash worked out.

You can also call the target providing a different Black Magic Probe GDB serial port by calling for example: `make flash BMP_PORT=/dev/cu.usbmodemXXXXXXX1` on Mac OS.

Following is a more complicated make setup that automatically detects Black Magic Probe GDB serial ports.

```make
PREFIX		?= arm-none-eabi
GDB		:= $(PREFIX)-gdb
SCRIPT_DIR	:= scripts

ifeq ($(BMP_PORT),)
BMP_PORT_CANDIDATES := $(wildcard \
/dev/serial/by-id/usb-Black_Sphere_Technologies_Black_Magic_Probe_*-if00 \
/dev/cu.usbmodem*1)
ifeq ($(words $(BMP_PORT_CANDIDATES)),1)
BMP_PORT := $(BMP_PORT_CANDIDATES)
else
BMP_PORT = $(error Black Magic Probe gdb serial port not found, please provide the device name via the BMP_PORT variable parameter$(if \
$(BMP_PORT_CANDIDATES), (found $(BMP_PORT_CANDIDATES))))
endif
endif
%.flash: %.elf
	@printf "  BMP $(BMP_PORT) $(*).elf (flash)\n"
	$(Q)$(GDB) -nx --batch \
	           -ex 'target extended-remote $(BMP_PORT)' \
	           -x $(SCRIPT_DIR)/black_magic_probe_flash.scr \
	           $(*).elf
```

For a full example using this kind of a makefile target you can look at the [1Bitsy template project](https://github.com/1Bitsy/1bitsy-locm3-template).

## Windows Batch

You can use a similar technique on windows too. Here is a `.bat` that implements binary flashing:

```bat
@echo off
rem: Note %~dp0 get path of this batch file
rem: Need to change drive if My Documents is on a drive other than C:
set driverLetter=%~dp0
set driverLetter=%driverLetter:~0,2%
%driverLetter%
cd %~dp0
rem: get all parameters that we will be using and make sure the slashes are all correct
set working_directory=%~p0
set toolchain_path=%~1
set toolchain_path=%toolchain_path:/=\%
set bmp_gdb_port=%2
set bmp_gdb_port=%bmp_gdb_port:/=\%
set elf_file=%3
set elf_file=%elf_file:/=\%
%toolchain_path%\arm-none-eabi-gdb.exe --batch -nx ^
	-ex "target extended-remote %bmp_gdb_port%" ^
	-x %working_directory%..\shared\bmp_gdb_upload_swd.scr ^
	%elf_file%
```

This batch script takes three parameters: `toolchain path`, `Black Magic Probe GDB Port name` and `binary elf file`
You can call that batch script for example like this: `bmp_upload.bat C:\\gcc-arm-none-eabi\bin COM1 yourbinary.elf`

## In Production Batch Programming

You can use the Black Magic Probe to bulk program large numbers of devices in production. The easiest way to accomplish that is to use one of the above techniques and run them in the loop. It is also useful to have audible response when the flash process has been successful. You can add an audio file playback at the end of the GDB script and it will only be played when the flash cycle has been successful.

Here is a onliner loop for your unix system of choice:

```sh
while true; do sleep 1; arm-none-eabi-gdb --batch -nx \
  -ex "target extended-remote /dev/ttyACM0" \
  -x gdb_upload.scr \
  yourbinary.elf; done
```

Note: It is useful to have a short period of sleep between the gdb invocations, otherwise it is difficult to break the loop with `Ctrl-C` key combination. Most modern unix systems support also shorter periods than 1 as parameter to the sleep command. You can call it with 0.5 for half a second sleep period.

The newly added GDB flash script lines for audio response for Linux would look like this:

```
shell paplay /usr/share/sounds/ubuntu/stereo/message.ogg
shell sleep 3
```

Note: The additional 3 seconds of sleep after a successful firmware upload gives the operator time to disconnect the Black Magic Probe from the target without accidentally flashing the target multiple times. If you pull the cable in the middle of the flash process you can end up with a half programmed or reerased target...

And this is what those lines look like on Mac OS:

```
shell afplay /System/Library/Sounds/Ping.aiff
shell sleep 3
```

Note: The additional 3 seconds of sleep after a successful firmware upload gives the operator time to disconnect the Black Magic Probe from the target without accidentally flashing the target multiple times. If you pull the cable in the middle of the flash process you can end up with a half programmed or reerased target...

For convenience here is a full script that should work on an Ubuntu computer with a bunch of annotations as comments:
```
# Print BMPM version
monitor version
# To make sure the target is not in a "strange" mode we tell BMPM to reset the
# target using the reset pin before connecting to it.
monitor connect_srst enable
# Enable target power (aka. provide power to the target side of the level shifters)
monitor tpwr enable
# Scan for devices using SWD interface
monitor swdp_scan
# Alternatively scan for devices using JTAG. (comment out the above line...)
# monitor jtag_scan
# Attach to the newly found target if available. (if it fails the script exits)
attach 1
# Success! Lets make some sound!
shell paplay /usr/share/sounds/ubuntu/stereo/message.ogg
# Load aka. flash the binary
load
# Check if the flash matches the binary
compare-sections
# Reset the target and disconnect
kill
# Write to the terminal that we succeeded
echo "Upload success!!!"
# Finished flashing success! Lets make some more sound!
shell paplay /usr/share/sounds/ubuntu/stereo/system-ready.ogg
```

## Auto-detecting the GDB port in Windows PowerShell

It is not ideal to have to manually determine the serial port name and type it into the script invocation each time. The following command in Windows PowerShell will detect the GDB port and set an environment variable, which can then be used to call GDB.

```
Get-CimInstance -ClassName Win32_SerialPort -Filter "PNPDeviceID like 'USB\\VID_1D50&PID_6018&MI_00%'" | `
  Select -ExpandProperty DeviceID | Set-Variable -Name BMP_GDB_PORT

echo $BMP_GDB_PORT
```