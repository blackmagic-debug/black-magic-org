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
        ("14", "pin"),
        ("UART TX", "uart"),
    ],
    [
        ("12", "pin"),
        ("nRst", "rst"),
        ("nRst", "rst"),
    ],
    [
        ("10", "pin"),
        ("NC", "nc"),
        ("TDI", "jtag"),
    ],
    [
        ("8", "pin"),
        ("TRACESWO", "swd"),
        ("TDO", "jtag"),
    ],
    [
        ("6", "pin"),
        ("SWDCLK", "swd"),
        ("TCK", "jtag"),
    ],
    [
        ("4", "pin"),
        ("SWDIO", "swd"),
        ("TMS", "jtag"),
    ],
    [
        ("2", "pin"),
        ("Reserved", "nc"),
    ],
]

right_header = [
    [
        ("13", "pin"),
        ("UART RX", "uart"),
    ],
    [
        ("11", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("9", "pin"),
        ("Key", "nc"),
    ],
    [
        ("7", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("5", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("3", "pin"),
        ("vRef", "pwr")
    ],
    [
        ("1", "pin"),
        ("Reserved", "nc")
    ],
]

# Text

title = "<tspan class='h1'>STMicro STDC14 Debug Connector Pinout</tspan>"

description = """This is the debug connector STMicroelectronics came up with
pins 3-12 are the same as ARM Cortex Debug Connector. The 14pin ribbon
will plug into the 10 Pin ARM Cortex Debug Connector for compatibility.

<tspan class='strong'>NOTE:</tspan> The TX/RX directionality is from the perspective of the Debugger. On the
Target (DUT) side these pins are swapped and pin 14 is RX and 13 is TX.
<tspan class='strong'>NOTE:</tspan> The header is HALF PITCH! This means it is 0.05 inch (1.27 mm) pitch pin header.
"""
