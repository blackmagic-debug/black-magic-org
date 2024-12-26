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

## What even is SWO and what is it used for really?

SWO, or Serial Wire Output, is one of two methods available in ARM's CoreSight tracing and instrumentation framework
for getting data out of a target over a sideband channel to the main debugging channel or mechanisms like a UART or RTT.
The two output methods are Trace and SWO.

Trace is a parallel mechanism that has a 1, 2, or 4 bit (most commonly, though more bits are possible in higher spec
parts) wide bus + clock for rappidly outputting tracing, requiring specialised connectors like ARM's 20-pin CoreSight
connector, or a Mictor connector. This is great for very high bandwidth but requires specific design considerations and
adaptors like ORBTrace, or one of the big commercial offerings like Lauterbach's TRACE32 tools. This is expensive.

SWO however uses just a single pin (sometimes known as TRACESWO, though strictly just SWO) which repurposes what would be
the JTAG TDO pin. It cannot achieve particularly high throughput by comparison, but it is very simple to use and is
provided on a stadard ARM 10-pin CoreSight connector. Do note though that not all parts supply trace outputs, so do
check the part's datasheet to ensure it can do this. An example is the RP2040 which forgoes the tracing infrastructure
entirely.

### Okay, but what can SWO actually do?

The way that CoreSight is architected means there are a few moving pieces to this question. We will work from the output
pin itself backwards as this should hopefully make it make the most sense.

The first piece and the part which makes wiggles on a pin or set of pins, is the TPIU (Trace Port Interface Unit). This
is the component which receives tracing and instrumentation data from the ATB (Advanced Trace Bus) and turns all that
into a coherent stream on the wire. This includes choosing whether the data will be output over Trace or SWO interfaces,
and if over SWO whether that will be via Manchester or UART (Async) encoding schemes. It contains a FIFO for the data
being produced.

Feeding a TPIU are trace funnels, which multiplex multiple tracing/instrumentation sources into a single coherent
ATB stream for the TPIU. We can mostly ignore this though and focus on what feeds a trace funnel with data.

Data sources include the ETM (Embedded Trace Macrocell) and ITM (Instrumentation Trace Macrocell). These are what the
following sections focus on and discuss. Note, if you enable more than one source you *must* enable TPIU framing for
formatting. This is so the recievier can then figure out which component a given packet came from to decode and consume.

### The ETM

This is a component that is not found on all Cortex-M parts, but is found on many. The main job of this component is to
trace execution on its attached core - sampling the program counter, and allowing building of an execution flow graph.
Depending on the version of the ETM integrated onto the target core, this can take the form of either samples every
few instructions (eg, once every 16th cycle), or it can be a complete trace of execution w/ the ETM halting execution
when the FIFO gets too full.

This component is integral to the Cortex-M core and is found duplicated on all cores that the integrating vendor has
chosen to enable execution tracing on. There are 3 main versions you will encounter in the wild: v3, v3.5 and v4.
Older versions of the ETM are found on older core designs typically, though the vendor may choose to replace, eg,
a Cortex-M3's defualt ETM with a newer ETMv4 as part of integrating debug and trace in a system that uses newer tracing
components downstream of the ETM.

### The ITM

This is a component usually found on all Cortex-M cores, with some notable exceptions. The main job of this component is
to allow you to instrument your firmware with state that allows fine grained tunable tracing of flow with the one downside
that it is intrusive, unlike the ETM. There are up to 32 "stimulus ports" provided by the block which the processor
can write into to output state information - for example, port 0 used for the main execution thread, while port 1 is
used for interrupt tracing w/ 8-bit writes done to each to output simple ASCII characters, or 32-bit writes to output
addresses in the code being executed.

The data output to the ITM from the code is free-form. Each core has its own instance of the ITM w/ differing capabilities
depending on what the vendor integrates. The packets output by the ITM onto the ATB are called SWIT packets - SoftWare
Instrumentation Trace packets.

The ITM depends on one additional block in the core for generating timestamping and other utility functions - the DWT.
In typical usage, the DWT must be configured to enable synchronisation for timing. This is also the source of triggers
for the ETM for when it will sample the program counter.

### Putting it all together

An example is provided below showing how you can configure Manchester-mode SWO on a STM32 atop of libopencm3:

```c
#define SWO_BAUDRATE 115200U
#define ARM_LAR_ACCESS_ENABLE 0xc5acce55U

static void swo_setup(void)
{
	/* Enable tracing in DEMCR */
	SCS_DEMCR |= SCS_DEMCR_TRCENA;

	/* Get the active clock frequency of the core and use that to calculate a divisor */
	const uint32_t clock_frequency = rcc_ahb_frequency;
	const uint32_t divisor = (clock_frequency / SWO_BAUDRATE) - 1U;
	/* And configure the TPIU for 1-bit async trace (SWO) in Manchester coding */
	TPIU_LAR = ARM_LAR_ACCESS_ENABLE;
	TPIU_CSPSR = 1U; /* 1-bit mode */
	TPIU_ACPR = divisor;
	TPIU_SPPR = TPIU_SPPR_ASYNC_MANCHESTER;
	/* Ensure that TPIU framing is off */
	TPIU_FFCR &= ~TPIU_FFCR_ENFCONT;

	/* Configure the DWT to provide the sync source for the ITM */
	DWT_LAR = ARM_LAR_ACCESS_ENABLE;
	DWT_CTRL |= 0x000003feU;
	/* Enable access to the ITM registers and configure tracing output from the first stimulus port */
	ITM_LAR = ARM_LAR_ACCESS_ENABLE;
	/* User-level access to the first 8 ports */
	ITM_TPR = 0x0000000fU;
	ITM_TCR = ITM_TCR_ITMENA | ITM_TCR_SYNCENA | ITM_TCR_TXENA | ITM_TCR_SWOENA | (1U << 16U);
	ITM_TER[0] = 1U;

	/* Now tell the DBGMCU that we want trace enabled and mapped as SWO */
	DBGMCU_CR &= ~DBGMCU_CR_TRACE_MODE_MASK;
	DBGMCU_CR |= DBGMCU_CR_TRACE_IOEN | DBGMCU_CR_TRACE_MODE_ASYNC;
}
```
