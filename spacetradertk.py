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

    def __init__(self, screen_x: int, screen_y: int) -> None:
        super().__init__()
        self.title("Space Trader")
        self.resizable(False, False)
        self.geometry(self._center_window(screen_x, screen_y))
        self.configure(bg=c.BKG_HEX)
        self._load_assets()

        self.manager = ScreenManager(self)

        self.boot()

    def _center_window(self, screen_x: int, screen_y: int) -> str:
        """
        Builds a geometry string to center window on the monitor
        """
        res = c.INTERNAL_RES * c.SCALAR
        x_adj = int((screen_x / 2) - (res / 2))
        y_adj = int((screen_y / 2) - (res / 2))

        return f"{str(res)}x{str(res)}+{x_adj}+{y_adj}"

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

    def boot(self):
        """
        Starts the game
        """
        CreateCommander(self).tkraise()


def splash() -> tuple[int, int]:
    """Splash screen"""
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.resizable(False, False)

    # Place the splash screen in the center
    screen_x = splash.winfo_screenwidth()
    screen_y = splash.winfo_screenheight()
    x_adj = int((screen_x / 2) - (160 / 2))
    y_adj = int((screen_y / 2) - (160 / 2))
    splash.geometry(f"160x160+{x_adj}+{y_adj}")

    splash_image = tk.PhotoImage(file=os.path.join("assets/images", "splash.png"))
    splash_label = tk.Label(splash, image=splash_image)
    splash_label.pack(expand=True, fill="both")
    splash.after(1500, lambda: [splash.destroy(), print("Splash screen closed")])
    splash.mainloop()

    # Return the monitor resolution just to reduce the re-polling in main window
    return screen_x, screen_y


def main():

    # Show the splash screen
    screen_x, screen_y = splash()

    # Start the main game window
    window = SpaceTrader(screen_x, screen_y)
    window.mainloop()


if __name__ == "__main__":
    main()
