"""
    Space Trader (PalmOS) | RPINerd, 08/07/24

    An early space strategy RPG game for PalmOS.

    This file is the start of a rewrite of the Space Trader game using Tkinter for the GUI.
"""

import os
import tkinter as tk

import src.constants as c
from src.screens.char_create import CreateCommander
from src.screens.screen_manager import ScreenManager
from src.utils import FontManager


class SpaceTrader(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Space Trader")
        self.minsize(str(160 * c.SCALAR), str(160 * c.SCALAR))
        self.geometry(f"{str(160 * c.SCALAR)}x{str(160 * c.SCALAR)}")
        self.resizable(False, False)
        self.configure(bg=c.BKG_HEX)
        self._load_assets()

        self.manager = ScreenManager(self)

    def _load_assets(self):
        """
        Loads all game assets, currently just pointers to directories
        """

        # Load the configuration file
        # self.config = configparser.ConfigParser()
        # self.config.read(os.path.join("src/config", "config.ini"))

        # Load the directories for the game assets
        self.images = os.path.join("assets/images/")
        self.resources = os.path.join("assets/resources/")
        self.fonts = os.path.join("assets/fonts/")
        # self.data = os.path.join("data")
        FontManager.load_font(f"{self.fonts}palm-pilot-small.ttf")
        FontManager.load_font(f"{self.fonts}palm-pilot-bold.ttf")
        FontManager.load_font(f"{self.fonts}palm-pilot-large.ttf")
        FontManager.load_font(f"{self.fonts}palm-pilot-large-bold.ttf")


window = SpaceTrader()

CreateCommander(window).tkraise()

window.mainloop()
