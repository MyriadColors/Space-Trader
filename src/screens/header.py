"""
    Space Trader (PalmOS) | RPINerd, 2024

    Renders the core header for vast majority of screens in the game.
    This includes the underline, as well as the BSYW button
    outlines for the top right.
"""

import tkinter as tk

from src.constants import BKG_HEX, FRG_HEX, INTERNAL_RES, SCALAR


class Heading(tk.Frame):

    def __init__(self, parent, heading: str):
        super().__init__(parent)
        self.parent = parent
        self.heading = heading
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.heading = tk.Label(self, text=self.heading, font=("Palm Pilot Bold", 16), fg=BKG_HEX, bg=FRG_HEX)
        self.heading.pack(side="left")

        self.b = tk.Button(
            self,
            text="B",
            font=("Palm Pilot Small", 14),
            fg=FRG_HEX,
            bg=BKG_HEX,
            width=2,
            height=1,
            command=lambda: self.shortcut_trigger("B"),
        )
        self.b.pack(side="right")
        self.s = tk.Button(
            self,
            text="S",
            font=("Palm Pilot Small", 14),
            fg=FRG_HEX,
            bg=BKG_HEX,
            width=2,
            height=1,
            command=lambda: self.shortcut_trigger("S"),
        )
        self.s.pack(side="right")
        self.y = tk.Button(
            self,
            text="Y",
            font=("Palm Pilot Small", 14),
            fg=FRG_HEX,
            bg=BKG_HEX,
            width=2,
            height=1,
            command=self.shortcut_trigger,
        )
        self.y.pack(side="right")
        self.w = tk.Button(
            self,
            text="W",
            font=("Palm Pilot Small", 14),
            fg=FRG_HEX,
            bg=BKG_HEX,
            width=2,
            height=1,
            command=lambda: self.shortcut_trigger(self, "W"),
        )
        self.w.pack(side="right")

        self.underline = tk.Canvas(self, width=INTERNAL_RES * SCALAR, height=2, bg=FRG_HEX)
        self.underline.pack(side="bottom", expand=True, fill="x")

    def shortcut_trigger(self, event):
        print(type(self))
        print(self)
        print(type(event))
        print(event)
        # self.parent.change_screen(event)
