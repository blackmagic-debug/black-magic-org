# Serial Wire Output

Serial Wire Output (SWO) allows the target to write tracing and logging to the host without using usb or serial port. All data goes over a single pin, the JTAG TDO pin.

To set up SWO, you need to

* connect target and bmp
* configure the target processor
* configure bmp
* set up the viewer

## Wires
SWO needs a connection between target SWO out and BMP SWO in (PA10 on stm32f103).
As the SWO pin is the JTAG TDO pin, you cannot run SWO when using JTAG. SWO is compatible with SWD, not with JTAG.

A setup with blue pills might look like this:

![](https://raw.githubusercontent.com/koendv/Connecting-Black-Magic-Probe-and-Blue-Pill/master/bmp_bp.svg)

## Target processor setup

Registers must be set up to configure the SWO pin for output. Different processors have different SWO setup.
You can setup SWO in viewer, debugger, or target.

* [bmtrace](https://github.com/compuphase/Black-Magic-Probe-Book) configures target processor in the viewer, button *Configure target*. Supports stm32 and lpc.
* [orbuculum](https://github.com/orbcode/orbuculum) has scripts to configure the target in gdb, and stm32 c source to include in your build.
* [SerialWireOutput](https://github.com/koendv/SerialWireOutput) arduino library, does stm32 set up in code. Userland source for initializing, write() and flush().

## Black Magic Probe
BMP receives SWO from the target and sends decoded SWO to a usb serial port, or undecoded SWO to a viewer. Target and probe:
* must speak the same protocol, async (NRZ) or Manchester
* at the same baud rate


There are two SWO protocols: Manchester and asynchronous (aka NRZ). You can see what protocol your BMP speaks with ``monitor help``. The protocol is listed next to the ``traceswo`` command.

Manchester coding auto-synchronizes. For asynchronous protocol, you have to configure the same baud rate in target and bmp. The default baud rate for async is 2250000.

Black Magic Probe can do SWO decoding in the probe itself, or pass the undecoded SWO stream to an external viewer.

### SWO decoding in BMP

You can switch on traceswo decoding in BMP with
```
monitor traceswo decode
```

``traceswo decode`` defaults to 2250000 baud (if using async) and decoding all channels. If using async, you can specify a baud rate. Optionally you can specify which stimulus channels to decode. Example:
```
monitor traceswo 4500000 decode 0 2
```
sets speed to 4500000 baud, and decodes only channels 0 and 2.

The decoded SWO stream is written to the usb uart. Viewing SWO is simply connecting to the usb uart.

### linux
On linux, set up [udev-rules](https://github.com/blackmagic-debug/blackmagic/blob/master/driver/99-blackmagic.rules) and type
```
cat /dev/ttyBmpTarg
```
If you have not set up udev-rules, connect to the second of the two serial ports, e.g ``cat /dev/ttyACM1``.
If the SWO stream is not shown, check baud rate.

### Windows
Black Magic Probe shows up in the device manager as two COM ports. For Windows 8 and 10, no drivers need to be installed for serial ports. For earlier versions, one can use an [.inf file](https://github.com/blackmagic-debug/blackmagic/tree/master/driver) that references the pre-installed serial driver. On Windows, connect [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to the second of the two COM ports, labeled "Black Magic UART Port".

SWO decoding in the probe does not need any special utilities and works on every os. For setups that use only a single channel this may be all you need.

For complex setups, especially with multiple channels, an external viewer may be more suitable.

## External viewer

You can switch on traceswo for external viewers with
```
monitor traceswo
```
The SWO stream is written to the usb trace port. (The usb trace port does not show up in /dev). If using async protocol, you can specify a baud rate: ``monitor traceswo 1125000``. The default for async is 2250000.

Viewers:
* [bmtrace](https://github.com/compuphase/Black-Magic-Probe-Book) (graphical, windows, ubuntu). Configures bmp and target for you. Windows binaries.
![](https://github.com/compuphase/Black-Magic-Probe-Book/raw/master/doc/bmtrace.png)
* [orbuculum](https://github.com/orbcode/orbuculum) (linux, command line) Advanced. Has gdb init scripts and target c source in the Support/ directory.
* [swo_listen](https://github.com/blackmagic-debug/blackmagic/blob/master/scripts/swolisten.c) (linux, command line)
* [bmp_traceswo](https://github.com/nickd4/bmp_traceswo) and [fork](https://github.com/tristanseifert/bmp_traceswo) (linux, command line) [detailed write-up](https://github.com/blackmagic-debug/blackmagic/wiki/Serial-Wire-Debug-TRACESWO-support)
