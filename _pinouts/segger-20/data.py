legend = [
    ("SWD", "swd"),
    ("JTAG", "jtag"),
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
        ("NC", "nc"),
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
        ("GND", "gnd"),
    ],
    [
        ("16", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("18", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("20", "pin"),
        ("GND", "gnd"),
    ],
]

# Text

title = """<tspan class='h1'>SEGGER 20pin JTAG/SWD Connector Pinout</tspan>"""

description = """J-Link and J-Trace have a JTAG connector compatible with ARM's Multi-ICE connector.

<tspan class='strong'>NOTE:</tspan> The header is FULL PITCH! This means it is 0.1 inch (2.54 mm) pitch pin header.
"""
