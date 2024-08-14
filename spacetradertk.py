"""
    Space Trader (PalmOS) | RPINerd, 08/07/24

    An early space strategy RPG game for PalmOS.

    This file is the start of a rewrite of the Space Trader game using Tkinter for the GUI.
"""

import tkinter as tk
from tkinter import ttk

import src.constants as c

# import src.game_data as gd
from src.screens.char_create import CreateCommander


class SpaceTrader(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Space Trader")
        self.minsize(str(160 * c.SCALAR), str(160 * c.SCALAR))
        self.geometry(f"{str(160 * c.SCALAR)}x{str(160 * c.SCALAR)}")
        self.resizable(False, False)
        self.configure(bg=c.BKG_HEX)

        self.create_commander = CreateCommander(self)
        self.create_commander.pack(expand=True, fill="both")


game = SpaceTrader()
game.mainloop()
