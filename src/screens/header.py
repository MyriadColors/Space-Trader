"""
    Space Trader (PalmOS) | RPINerd, 2024
    
    Renders the core header for vast majority of screens in the game.
    This includes the underline, as well as the BSYW button
    outlines for the top right.
"""

import tkinter as tk


class Heading(tk.Frame):
    def __init__(self, parent, heading: str):
        super().__init__(parent)
        self.heading = heading
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.heading = tk.Label(self, text=self.heading)
        self.heading.pack()
        self.underline = tk.Canvas(self, width=160, height=2, bg="#000000")
        self.underline.pack()
        self.b = tk.Button(self, text="B", width=2, height=1)
        self.b.pack(side="right")
        self.s = tk.Button(self, text="S", width=2, height=1)
        self.s.pack(side="right")
        self.y = tk.Button(self, text="Y", width=2, height=1)
        self.y.pack(side="right")
        self.w = tk.Button(self, text="W", width=2, height=1)
        self.w.pack(side="right")
