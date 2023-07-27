from tkinter import Scale
from pinout import config
from pinout.core import Group, Image
from pinout.components.layout import Diagram_2Rows, Panel
from pinout.components.pinlabel import PinLabelGroup
from pinout.components.annotation import AnnotationLabel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend

import data

diagram = Diagram_2Rows(800, 700, 450, "diagram")
diagram.add_stylesheet("styles.css", embed=True)

# panel_graphic = content.add(
#     Panel(
#         width=860,
#         height=300,
#         tag="panel__graphic",
#     )
# )

graphic = diagram.panel_01.add(Group(320, 50))

hardware = graphic.add(Image("../models/20-pin-shrouded.svg", width=180, height=360, embed=True))

hardware.add_coord("p1", x=75, y=45)
hardware.add_coord("p2", x=105, y=45)
hardware.add_coord("p3", x=75, y=75)
hardware.add_coord("p4", x=105, y=75)
hardware.add_coord("p5", x=75, y=105)
hardware.add_coord("p6", x=105, y=105)
hardware.add_coord("p7", x=75, y=135)
hardware.add_coord("p8", x=105, y=135)
hardware.add_coord("p9", x=75, y=165)
hardware.add_coord("p10", x=105, y=165)
hardware.add_coord("p11", x=75, y=195)
hardware.add_coord("p12", x=105, y=195)
hardware.add_coord("p13", x=75, y=225)
hardware.add_coord("p14", x=105, y=225)
hardware.add_coord("p15", x=75, y=255)
hardware.add_coord("p16", x=105, y=255)
hardware.add_coord("p17", x=75, y=285)
hardware.add_coord("p18", x=105, y=285)
hardware.add_coord("p19", x=75, y=315)
hardware.add_coord("p20", x=105, y=315)
hardware.add_coord("pin_pitch_v", x=0, y=30)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("p1").x,
        y=hardware.coord("p1").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, 30),
        scale=(-1, 1),
        labels=data.left_header,
    )
)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("p2").x,
        y=hardware.coord("p2").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, 30),
        labels=data.right_header,
    )
)

# Create a title and description text-blocks
title_block = diagram.panel_02.add(
    TextBlock(
        data.title,
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)
diagram.panel_02.add(
    TextBlock(
        data.description,
        x=20,
        y=60,
        width=title_block.width,
        height=diagram.panel_02.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)


# Create a legend
legend = diagram.panel_02.add(
    Legend(
        data.legend,
        x=630,
        y=8,
        max_height=230,
    )
)

license = diagram.panel_02.add(Group(x=20, y=200))

license.add(Image("../models/by-nc-sa.svg", embed=True))

license.add(
    TextBlock(
        """2023 (C) 1BitSquared &lt;info@1bitsquared.com&gt;
        2023 (C) Rafael Silva &lt;perigoso@riseup.net&gt;""",
        x=130,
        y=20,
        width=100,
        height=30,
        line_height=18,
        tag="panel license",
    )
)
