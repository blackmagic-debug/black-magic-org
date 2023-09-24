legend = [
    ("JTAG", "jtag"),
    ("Reset", "rst"),
    ("Pin Number", "pin"),
    ("Power", "pwr"),
    ("Ground", "gnd"),
    ("Not Connected", "nc"),
]

left_header = [
    [
        ("14", "pin"),
        ("nRST", "rst")
    ],
    [
        ("12", "pin"),
        ("NC", "nc")
    ],
    [
        ("10", "pin"),
        ("TDI", "jtag")
    ],
    [
        ("8", "pin"),
        ("TDO", "jtag")
    ],
    [
        ("6", "pin"),
        ("TCK", "jtag")
    ],
    [
        ("4", "pin"),
        ("TMS", "jtag")
    ],
    [
        ("2", "pin"),
        ("vRef", "pwr")
    ],
]

right_header = [
    [
        ("13", "pin"),
        ("GND", "gnd")
    ],
    [
        ("11", "pin"),
        ("GND", "gnd")
    ],
    [
        ("9", "pin"),
        ("GND", "gnd")
    ],
    [
        ("7", "pin"),
        ("GND", "gnd")
    ],
    [
        ("5", "pin"),
        ("GND", "gnd")
    ],
    [
        ("3", "pin"),
        ("GND", "gnd")
    ],
    [
        ("1", "pin"),
        ("NC", "nc")
    ],
]

# Text

title = "<tspan class='h1'>Xilinx JTAG Debug Connector Pinout</tspan>"

description = """This is the debug connector Xilinx came up with,
it is used on a majority of Xilinx boards for test and debug, especially
the Zynq and Kria SoCs.

<tspan class='strong'>NOTE:</tspan> The header is METRIC! It's a 2mm pin pitch.
"""
