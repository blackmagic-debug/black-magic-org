# This information was referenced from the following sources:
# https://www.segger.com/products/debug-probes/j-link/technology/interface-description
# https://wiki.segger.com/Using_J-Link_VCOM_functionality
# UM08001_JLinkARM User Manual

legend = [
    ("SWD", "swd"),
    ("JTAG", "jtag"),
    ("UART", "uart"),
    ("Reset", "rst"),
    ("Pin Number", "pin"),
    ("Power", "pwr"),
    ("Ground", "gnd"),
    ("Not Connected", "nc"),
]

left_header = [
    [
        ("1", "pin"),
        ("vRef", "pwr"),
    ],
    [
        ("3", "pin"),
        ("NC", "nc"),
        ("tRST", "rst"),
    ],
    [
        ("5", "pin"),
        ("UART TX", "uart"),
        ("TDI", "jtag"),
    ],
    [
        ("7", "pin"),
        ("SWDIO", "swd"),
        ("TMS", "jtag"),
    ],
    [
        ("9", "pin"),
        ("SWDCLK", "swd"),
        ("TCK", "jtag"),
    ],
    [
        ("11", "pin"),
        ("NC", "nc"),
        ("RTCK", "jtag"),
    ],
    [
        ("13", "pin"),
        ("TRACESWO", "swd"),
        ("TDO", "jtag"),
    ],
    [
        ("15", "pin"),
        ("nRst", "rst"),
        ("nRst", "rst"),
    ],
    [
        ("17", "pin"),
        ("UART RX", "uart"),
        ("NC", "nc"),
    ],
    [
        ("19", "pin"),
        ("5V Supply", "pwr"),
    ],
]

right_header = [
    [
        ("2", "pin"),
        ("NC", "nc"),
    ],
    [
        ("4", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("6", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("8", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("10", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("12", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("14", "pin"),
        ("GND*", "gnd"),
    ],
    [
        ("16", "pin"),
        ("GND*", "gnd"),
    ],
    [
        ("18", "pin"),
        ("GND*", "gnd"),
    ],
    [
        ("20", "pin"),
        ("GND*", "gnd"),
    ],
]

# Text

title = """<tspan class='h1'>SEGGER 20pin JTAG/SWD Connector Pinout</tspan>"""

description = """J-Link and J-Trace have a JTAG connector compatible with ARM's Multi-ICE/JTAG connector.

<tspan class='strong'>NOTE:</tspan> The header is FULL PITCH! This means it is 0.1 inch (2.54 mm) pitch pin header.
<tspan class='strong'>NOTE:</tspan> The TX/RX directionality is from the perspective of the Debugger. On the
Target (DUT) side these pins are swapped and pin 5 is RX and 17 is TX.
<tspan class='strong'>NOTE:</tspan> The UART functionality is not available on all J-Link models nor all modes of operation.
<tspan class='strong'>NOTE:</tspan> On later J-Link products pins 14, 16, 18, and 20 are reserved for firmware extensions,
they can be left open or connected to GND in normal debug environments and are not essential for normal operation.
"""
