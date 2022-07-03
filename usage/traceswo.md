# SWD - TRACESWO support

The Black Magic Probe when in Serial Wire Debug (rather than JTAG) mode can receive the TRACESWO diagnostic stream from targets which support it.

ARM Cortex chips include a comprehensive tracing framework, in brief there is an Embedded Trace Macrocell (ETM) which can generate trace output on various kinds of events such as data watchpoints, and there is an Instrumentation Trace Macrocell (ITM) which is similar but oriented towards software generated log messages. The instrumentation can be left enabled in your shipped product.

The ETM and ITM streams are combined in the TPIU which generates a series of frames in a specified format, this stream can be sent out on a 1-wire, 2-wire or 4-wire synchronous serial bus if enabled in your design, or it can be sent out the TRACESWO pin which is a 1-wire asynchronous serial stream. The TRACESWO output can be in UART (start, 8 data bits, stop) or Manchester encoded format.

The Black Magic Probe supports only the Manchester encoded format [at the time of writing -- this may be out of date -- see note at the end], which is a sensible choice because it allows automatic synchronization to the target's baudrate (within some range of sensible speeds). Note that the Black Magic Probe uses essentially a bit-banged input-only UART for this task, implemented in software using a timer input capture pin, and does not support high baudrates.

Mostly the TRACESWO pin will be used as a convenient way to get printf() style output to the debugger host, without wasting an I/O pin by assigning a dedicated UART to this function. The ETM/ITM/TPIU scheme is over-designed for this task, so it makes sense to turn off formatting in the TPIU when doing this. This gives an output stream consisting of 16-bit words, each containing a stream ID and a character.

A simple Linux application is available to dump Black Magic Probe TRACESWO output to stdout. This will be fine for basic usage. See https://github.com/nickd4/bmp_traceswo, it also contains some sample code to insert in your STM32 application showing how to set up and use the ITM and TPIU for printf() style output. It would be good if this could be extended to give examples for other major families such as the NXP ARM chips, etc.

Note that the STM32 case is a bit peculiar (contains a so-called Pelican TPIU at a non-ARM-mandated address), so you will need this example to get started. The code in the example is derived from here:  
https://mcuoneclipse.com/2016/10/17/tutorial-using-single-wire-output-swo-with-arm-cortex-m-and-eclipse  
A better example is here, which is cleaner and also shows how to enable the TRACESWO pin, missing above:  
http://forum.segger.com/index.php?page=Thread&threadID=608

The major IDEs are also able to interpret TRACESWO packets, in particular the formatted style, which might be more appropriate for advanced usage, with separate windows for different streams, and search, filtering etc. It is uncertain whether these support the Black Magic Probe's TRACESWO endpoint, if so please insert instructions.

See also https://github.com/tristanseifert/bmp_traceswo, the original version was taking one word at a time from the TRACESWO stream, ignoring the high byte and dumping the low byte, whereas this modification seems to be taking frames. I (nickd4) noticed the Black Magic TRACESWO firmware has changed and improved since my version was published, I will investigate it later. If you use Tristan's fork, you should take the /etc/udev/rules.d/99-blackmagic.rules from https://github.com/nickd4/bmp_traceswo, since it has improved since the fork.