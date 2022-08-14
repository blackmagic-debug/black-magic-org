legend = [
    ("SWD", "swd"),
    ("JTAG", "jtag"),
    ("Trace (ETM)", "trace"),
    ("Reset", "rst"),
    ("Pin Number", "pin"),
    ("Power", "pwr"),
    ("Ground", "gnd"),
    ("Not Connected", "nc"),
]



left_header = [
    [
        ("20", "pin"),
        ("TRACED[3]", "trace"),
    ],
    [
        ("18", "pin"),
        ("TRACED[2]", "trace"),
    ],
    [
        ("16", "pin"),
        ("TRACED[1]", "trace"),
    ],
    [
        ("14", "pin"),
        ("TRACED[0]", "trace"),
    ],
    [
        ("12", "pin"),
        ("TRACECLK", "trace"),
    ],
    [
        ("10", "pin"),
        ("nRst", "rst"),
        ("nRst", "rst"),
    ],
    [
        ("8", "pin"),
        ("NC", "nc"),
        ("TDI", "jtag"),
    ],
    [
        ("6", "pin"),
        ("TRACESWO", "swd"),
        ("TDO", "jtag"),
    ],
    [
        ("4", "pin"),
        ("SWDCLK", "swd"),
        ("TCK", "jtag"),
    ],
    [
        ("2", "pin"),
        ("SWDIO", "swd"),
        ("TMS", "jtag"),
    ],
]

right_header = [
    [
        ("19", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("17", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("15", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("13", "pin"),
        ("GND", "gnd"),
        ("TPwr+Cap", "pwr"),
    ],
    [
        ("11", "pin"),
        ("GND", "gnd"),
        ("TPwr+Cap", "pwr"),
    ],
    [
        ("9", "pin"),
        ("GND", "gnd"),
    ],
    [
        ("7", "pin"),
        ("Key", "nc"),
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

title = """<tspan class='h1'>ARM Cortex Debug &amp; Trace Connector Pinout</tspan>"""

description = """This is the standard ARM Cortex JTAG/SWD Debug and Trace
connector used on OrbTrace and some targets.
Half of the connector is pinout compatible with the 10-Pin ARM Cortex Debug.
This makes it easy to interoperate with debuggers using 10-Pin connectors, by
using a 10 to 20 pin ribbon cable.

<tspan class='strong'>NOTE:</tspan> The header is HALF PITCH! This means it is 0.05 inch (1.27 mm) pitch pin header.
"""
