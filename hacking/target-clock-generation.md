# Target Clock Generation

The Black Magic Debug firmware generates a clock signal to the debug target for both JTAG and SWD
by bitbanging, timed to the other signals involved in ths bus to generate transactions and transmit
data back and forth. The bitbanging routines are not perfect at this and so generate a signal with
an odd mark-to-space ratio and at different frequencies depending on which routine is in play.

Due of all of the above, this winds up requiring a very particular approach for measuring the
clock frequency generated to produce a number to report to the user, and to take clock speed requests
and map them to delay loop iteration counts, internally called the clock divider, and represent them
in the firmware.

The aim of this page is to lay out the method used to derive these clock frequency numbers and the
analytical tools used to then generate a calibration for a platform's platform.h header to make the
reporting and interaction as usefully accurate as possible.

## Measurement

In measuring TCK, because of how the bitbanging routines are written and work, it is assumed that
we are also deriving a reasonably accurate measurement for SWCLK - within 10kHz or so for a MHz range
clock speed measurement. Further, because of how the JTAG routines work, we must measure 3 key routines'
clock frequencies to come to a typical/average clock frequency, especially as these are the most common
3 routines that get called. They are, from the jtag_proc structure, jtagtap_next(), jtagtap_tms_seq() and
jtagtap_tdi_tdo_seq().

### The methodology

To make measurements, one will need a logic analyser capable of at least a 24MHz capture such as the
BitMagic Basic. We start out with firmware compiled for the target probe that has by modifying the remote
protocol implementation, been forced to use the _no_delay bitbanging routines and a matching BMDA with
which to run JTAG scans of a suitable JTAG target. Within this section we will be using the BitMagic Basic
logic analyser and PulseView to make measurements, and have just two lines of the JTAG bus tapped - TCK and TMS.

TMS is used to help navigate the capture and find the correct routines to measure, TCK is of course the
thing we want to measure. We use a 1% pre-trigger capture ratio, 24MHz sampling frequency and 100 million
samples per capture to ensure we get sufficient data.

To prepare the first (no-delay) run, we co-opt the remote protocol by [editing remote.c](https://github.com/blackmagic-debug/blackmagic/blob/799a4088e6c98fcbd977d9c3f2036bef4ba1e9b6/src/remote.c#L272).
We do this by commenting out the referenced line and replacing it with `target_clk_divider = UINT32_MAX;`
which, by virtue of how the bitbanging routines are written, forces the _no_delay variants.

We then load the firmware onto the probe, arm the logic analyser capture, and run BMDA as
`src/blackmagic -tjv 1`. This will perform a JTAG scan, printing the results, and exit.
Once complete, we can then turn our attention to PulseView where you should see a capture like the following:
