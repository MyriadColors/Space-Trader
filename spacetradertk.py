"""
    Space Trader (PalmOS) | RPINerd, 08/07/24

    An early space strategy RPG game for PalmOS.

    This file is the start of a rewrite of the Space Trader game using Tkinter for the GUI.
"""

import os
import tkinter as tk

import src.constants as c
from src.screens.char_create import CreateCommander

# from customtkinter import FontManager
from src.utils import FontManager

# from time import sleep
# from tkinter import font
# from PIL import ImageFont


class SpaceTrader(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Space Trader")
        self.minsize(str(160 * c.SCALAR), str(160 * c.SCALAR))
        self.geometry(f"{str(160 * c.SCALAR)}x{str(160 * c.SCALAR)}")
        self.resizable(False, False)
        self.configure(bg=c.BKG_HEX)
        self._load_assets()

        # Splash screen
        # splash_img = tk.PhotoImage(file=os.path.join(self.images, "splash.png"))
        # splash = tk.Label(self, image=splash_img)
        # splash.pack(expand=True, fill="both")
        # sleep(4)
        # splash.pack_forget()
        # self.create_commander = CreateCommander(self)
        tk.Label(self, text="Space Trader", font=("palm-pilot-bold", 20)).pack(expand=True, fill="both")

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
        # self.data = os.path.join("data")
        FontManager.init_font_manager()
        a = FontManager.load_font("assets/fonts/palm-pilot-small.ttf")
        b = FontManager.load_font("assets/fonts/palm-pilot-bold.ttf")
        c = FontManager.load_font("assets/fonts/palm-pilot-large.ttf")
        d = FontManager.load_font("assets/fonts/palm-pilot-large-bold.ttf")
        if a and b and c and d:
            print("Fonts loaded successfully")


game = SpaceTrader()
game.mainloop()
