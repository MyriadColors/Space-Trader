"""
    UI Previewer | RPINerd, 2024

    This script is a simple UI previewer for the Space Trader game.
    It allows you to request a state and see what the current UI would look like.

    Usage:
        python ui_preview.py <state>
"""

import os
import sys
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src import constants as c
from src.screens.screen_manager import SCREENS
from src.screens.system_info import SystemInfo
from src.utils import FontManager


def main(state):

    preview = tk.Tk()
    preview.title("Space Trader")
    preview.minsize(str(160 * c.SCALAR), str(160 * c.SCALAR))
    preview.geometry(f"{160 * c.SCALAR!s}x{160 * c.SCALAR!s}")
    preview.resizable(False, False)
    preview.configure(bg=c.BKG_HEX)

    fonts = os.path.join("assets/fonts/")
    FontManager.load_font(f"{fonts}palm-pilot-small.ttf")
    FontManager.load_font(f"{fonts}palm-pilot-bold.ttf")
    FontManager.load_font(f"{fonts}palm-pilot-large.ttf")
    FontManager.load_font(f"{fonts}palm-pilot-large-bold.ttf")

    if state == "I":
        SystemInfo(preview)
    else:
        print(f"Invalid state: {state}")
    preview.mainloop()


if __name__ == "__main__":

    print("Select a state to preview...")
    for state in SCREENS:
        print(f"{state}: {SCREENS[state]['title']}")
    print("\n")
    state = input("Enter the state to preview: ").upper()

    if state in SCREENS:
        main(state)
    else:
        print(f"Invalid state: {state}")
        sys.exit(1)
