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
        ("VCC", "pwr"),
    ],
    [
        ("3", "pin"),
        ("tRST", "rst"),
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
        ("TMS", "jtag")
    ],
    [
        ("9", "pin"),
        ("SWDCLK", "swd"),
        ("TCK", "jtag")
    ],
    [
        ("11", "pin"),
        ("RTCK", "swd"),
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
        ("NC", "nc"),
    ],
]

right_header = [
    [
        ("2", "pin"),
        ("VCC(opt)", "pwr"),
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
        ("GND", "gnd")
    ],
]

# Text

title = """<tspan class='h1'>ARM JTAG Connector Pinout</tspan>"""

description = """This is the old standard ARM JTAG Debug connector used on many older targets.
The SWD signal names are added for convenience keep in mind, this connector
predates SWD standard, so targets using this connector might not support
the SWD protocol.

<tspan class='strong'>NOTE:</tspan> The header is FULL PITCH! This means it is 0.1 inch (2.54 mm) pitch pin header.
"""
