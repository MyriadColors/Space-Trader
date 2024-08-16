"""
    Space Trader | RPINerd, 2024
    An elite-inspired space trading RPG originally on PalmOS

    Utils Module
    The utils module has a couple of functions that were separated in the original codebase.
    Likely could refactor these into the respective modules, but for now they are here.
"""

import os
import shutil
import sys
from typing import Union

from .constants import MAX_WORMHOLES


def planet_distance(planet: tuple[int, int], x2: int, y2: int) -> float:
    """
    Calculate the distance between a planet and a point.

    params: planet - tuple containing the x and y coordinates of the planet
    params: x2 - x coordinate of point 2
    params: y2 - y coordinate of point 2

    returns: distance between the planet and the point
    """
    return distance(planet[0], planet[1], x2, y2)


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Calculate the distance between two points.

    params: x1 - x coordinate of point 1
    params: y1 - y coordinate of point 1
    params: x2 - x coordinate of point 2
    params: y2 - y coordinate of point 2

    returns: distance between the two points
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def wormhole_exists(wormholes: list[int], a: int, b: int) -> bool:
    """
    Check if a wormhole exists at the given coordinates.

    params: wormholes - list of wormholes
    params: a - first wormhole
    params: b - second wormhole, or -1 if only checking for any wormhole at a

    returns: True if wormhole exists, False otherwise
    """

    # TODO bit of a mess, probably should have small separate functions for each check
    if a in wormholes:

        if b < 0:
            return True

        index = wormholes.index(a)
        if index < MAX_WORMHOLES - 1:
            if wormholes[index + 1] == b:
                return True
        elif wormholes[0] == b:
            return True

    return False


class FontManager:

    linux_font_path = "~/.fonts/"

    @classmethod
    def init_font_manager(cls):
        # Linux
        if sys.platform.startswith("linux"):
            try:
                if not os.path.isdir(os.path.expanduser(cls.linux_font_path)):
                    os.mkdir(os.path.expanduser(cls.linux_font_path))
                return True
            except Exception as err:
                sys.stderr.write("FontManager error: " + str(err) + "\n")
                return False

        # other platforms
        else:
            return True

    @classmethod
    def windows_load_font(cls, font_path: Union[str, bytes], private: bool = True, enumerable: bool = False) -> bool:
        """Function taken from: https://stackoverflow.com/questions/11993290/truly-custom-font-in-tkinter/30631309#30631309"""

        from ctypes import byref, create_string_buffer, create_unicode_buffer, windll

        FR_PRIVATE = 0x10
        FR_NOT_ENUM = 0x20

        if isinstance(font_path, bytes):
            path_buffer = create_string_buffer(font_path)
            add_font_resource_ex = windll.gdi32.AddFontResourceExA
        elif isinstance(font_path, str):
            path_buffer = create_unicode_buffer(font_path)
            add_font_resource_ex = windll.gdi32.AddFontResourceExW
        else:
            raise TypeError("font_path must be of type bytes or str")

        flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
        num_fonts_added = add_font_resource_ex(byref(path_buffer), flags, 0)
        return bool(min(num_fonts_added, 1))

    @classmethod
    def load_font(cls, font_path: str) -> bool:
        # Windows
        if sys.platform.startswith("win"):
            return cls.windows_load_font(font_path, private=True, enumerable=False)

        # Linux
        elif sys.platform.startswith("linux"):
            try:
                shutil.copy(font_path, os.path.expanduser(cls.linux_font_path))
                return True
            except Exception as err:
                sys.stderr.write("FontManager error: " + str(err) + "\n")
                return False

        # macOS
        elif sys.platform.startswith("darwin"):
            customtkinter_directory = os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            )
            font_path = os.path.join(customtkinter_directory, "assets", "fonts", "noto_sans", "regular.ttf")
            try:
                # Define the path to the Fonts folder in the user's home directory
                fonts_folder = os.path.join(os.path.expanduser("~"), "Library", "Fonts")
                # Check if the Fonts folder exists, if not, create it
                if not os.path.exists(fonts_folder):
                    os.makedirs(fonts_folder)
                # Copy the font file to the Fonts folder
                shutil.copy(font_path, fonts_folder)
                return True
            except Exception as err:
                sys.stderr.write("FontManager error: " + str(err) + "\n")
                return False

        # others
        else:
            return
