legend = [
    ("SWD", "swd"),
    ("JTAG", "jtag"),
    ("UART", "uart"),
    ("SPI", "spi"),
    ("Reset", "rst"),
    ("Pin Number", "pin"),
    ("Power", "pwr"),
    ("Ground", "gnd"),
    ("Not Connected", "nc"),
]



left_header = [
    [
        ("10", "pin"),
        ("nRst", "rst"),
        ("nRst", "rst"),
        ("nRST", "rst"),
    ],
    [
        ("8", "pin"),
        ("NC", "nc"),
        ("TDI", "jtag"),
        ("PICO", "spi"),
    ],
    [
        ("6", "pin"),
        ("TRACESWO", "swd"),
        ("TDO", "jtag"),
        ("POCI", "spi"),
    ],
    [
        ("4", "pin"),
        ("SWDCLK", "swd"),
        ("TCK", "jtag"),
        ("SCLK", "spi"),
    ],
    [
        ("2", "pin"),
        ("SWDIO", "swd"),
        ("TMS", "jtag"),
        ("CS", "spi")
    ],
]

right_header = [
    [
        ("9", "pin"),
        ("GND", "gnd"),
        ("UART RX", "uart"),
    ],
    [
        ("7", "pin"),
        ("Key", "nc"),
        ("UART TX", "uart"),
    ],
    [
        ("5", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("3", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("1", "pin"),
        ("vRef", "pwr")
    ],
]

# Text

title = "<tspan class='h1'>Black Magic Debug Unified Connector</tspan>"

description = """This connector is derived from the standard ARM Cortex
JTAG/SWD Debug connector. This pinout is supported by setting two solder
jumpers on the Black Magic Probe V2.3.

<tspan class='strong'>NOTE:</tspan> The TX/RX directionality is from the perspective of the Debugger. On the
Target (DUT) side these pins are swapped and pin 7 is RX and 9 is TX.
<tspan class='strong'>NOTE:</tspan> The SPI mapping is valid when SPIFlashProgrammer firmware is loaded.
<tspan class='strong'>NOTE:</tspan> The header is HALF PITCH! This means it is 0.05 inch (1.27 mm) pitch pin header.
"""
