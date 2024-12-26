# Serial Wire Output

Serial Wire Output (SWO) allows the target to produce tracing and logging information from your firmware
without using precious peripherals such as USB or UARTs. Instead, the data is emitted via a single pin,
which is usually what would be JTAG's TDO, but re-purposed for the purpose.

To set up SWO, you need to:

* Wire the target to your probe running BMD
* Configure the target processor
* Enable SWO handling in BMD
* Set up a viewer for the tracing and logging data

## Wires

You will need a connection between the target's SWO output and your probe. See your probe's README.md for details.
As the SWO pin is typically the JTAG TDO pin, you cannot run SWO when using JTAG. Instead you will need to access
the target via SWD and perform a SWD scan before SWO will start working.

A setup with Blue Pills might look like this:

![Back-to-backed Blue Pills](https://raw.githubusercontent.com/koendv/Connecting-Black-Magic-Probe-and-Blue-Pill/master/bmp_bp.svg)

## Target processor setup

Registers must be set up to configure the SWO pin for output. Different processors have different SWO setups.
You can setup SWO via the chosen viewer, debugger, or directly on the target.

* [Orbuculum](https://github.com/orbcode/orbuculum) has scripts to configure the target in GDB, and STM32 C source to include in your build.
* [bmtrace](https://github.com/compuphase/Black-Magic-Probe-Book) configures target processor in the viewer, button *Configure target*. Supports STM32 and LPC.
* [SerialWireOutput](https://github.com/koendv/SerialWireOutput) arduino library, does STM32 set up in code. Userland source for initializing, `write()` and `flush()`.

## Black Magic Debug

When the firmware receives SWO from a target, it can do one of two things: It can send the raw capture data to the
trace interface for use by a decoder and viewer suite, or decoded ITM data to the auxillary USB serial port.

For everything to work, the target and probe:

* Must speak the same protocol (UART (aka Async or NRZ) or Manchester coded), and
* For UART, at the same baud rate - this is configured as part of enabling SWO on the probe.

There are two SWO transport protocols: Manchester coded and UART (aka async). You can see what protocol your probe
speaks with `monitor help`. The protocol is listed next to the `swo` command. In the case of BMP, and some
third party probes, both protocols are supported in the firmware together. In this case, the protocol to decode
is given as a part of the instruction to enable SWO.

The Manchester coded SWO auto-synchronizes and the firmware auto-detects baud. However, for UART SWO, you have to
configure the baud rate both in the target configuration and on the probe. The default baud rate for async is 2.25MBaud.

### SWO decoding in firmware

You can switch on SWO decoding in BMD with

```gdb
monitor swo enable decode
```

This defaults to decoding all ITM streams. If your probe talks async mode, you can optionally specify a baud rate
between the `enable` verb and optionally requesting decoding. Following the `decode` verb, you can then specify
which ITM streams you wish to have decoded. For example:

```gdb
monitor swo enable 4500000 decode 0 2
```

This example is for an async mode probe, and configures 4.5MBaud and decoding of ITM streams 0 and 2.

SWO decoding in the probe does not need any special utilities and works on every OS. For setups that use only a
single ITM stream this may be all you need. Please note that if you use more than just the ITM, or if you use many
ITM channels, an external viewer such as the Orbuculum suite is required.

```{note}
On a BMP or on other platforms that implement the new switchable SWO, you will need to specify which protocol
encoding you wish to have the probe recover data from as part of the `swo enable` command. This is done by
specifying one of either `manchester` or `uart` just after `enable` in the invocation and if omitted defaults
to UART. Such an invocation looks like: `monitor swo enable manchester decode`.

As with any other command verb, you can shorten this - eg, `mon swo en manc dec` works just fine.
```

### Linux

Please first ensure that you have set up udev with the appropriate set of
[the project's udev rules](https://github.com/blackmagic-debug/blackmagic/tree/main/driver) so you get the proper
device permissions, and the friendly serial interface names in /dev.

To view the decoded data stream you can then connect in to `/dev/ttyBmpTarg` (or include your probe's serial number
after if you have more than one plugged in) using your favourite serial terminal program such as `screen`, `minicom`
or, in a pinch, `cat`.

If the decoded ITM stream data is not shown, check the configured baud rate on the target or on the probe.

### Windows

The probe shows up in Device Manager as two COM ports and two other USB interfaces. For Windows 8, 10 and 11, no
drivers should needto be installed to use the device and all interfaces should show up properly out of the box.
For earlier versions of Windows, you will need to use the
[two driver installation `.inf` files](https://github.com/blackmagic-debug/blackmagic/tree/main/driver) to get
Windows to bind the proper drivers to the device interfaces.

Once your probe has all interfaces properly bound, connect a program such as
[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) or any other serial terminal program to
the "Black Magic UART Port" COM port. On W8+ you will need to locate the COM port with the higher interface number
in Device Manager. This may not be the higher numbered COM port.

## External viewer

You can switch on SWO for external viewers with

```gdb
monitor swo enable
```

The recovered SWO data is output to the USB trace interface. If using a probe that works with async mode, you can
specify a baud rate like so: `monitor swo enable 1125000`. The default is 2.25MBaud.

```{note}
On a BMP or on other platforms that implement the new switchable SWO, you will need to specify which protocol
encoding you wish to have the probe recover data from as part of the `swo enable` command. This is done by
specifying one of either `manchester` or `uart` just after `enable` in the invocation and if omitted defaults
to UART. Such an invocation looks like: `monitor swo enable manchester`.

As with any other command verb, you can shorten this - eg, `mon swo en manc` works just fine.
```

### Viewers

The following is a (non-comprehensive) list of viewers that can work with Black Magic Debug Firmware:

* [Orbuculum](https://github.com/orbcode/orbuculum) - A comprehensive but easy to use suite of tools with GDB
scripts for target setup. Run `orbuculum` to start collecting trace data. (All OSes. Command line driven)
* [swolisten](https://github.com/blackmagic-debug/blackmagic/blob/main/scripts/swolisten.c) - Simplistic in-tree viewer
for ITM data and predecessor to Orbuculum. (Linux-only. Command line driven)
* [bmtrace](https://github.com/compuphase/Black-Magic-Probe-Book) - Basic ITM stream viewer. Configures BMD and tries
to configure your target for you. Windows binaries available. (Windows and Linux only. Graphical)

## Halting SWO recovery

If you wish to stop recovery of SWO, decoding of ITM data, or need to get the firmware to resynchronise with your
target, you can run `monitor swo disable` to spin the SWO engine down. Note, this frees any buffers associated
with the SWO data recovery and resets state. This is required if you wish to scan for targets over JTAG.
