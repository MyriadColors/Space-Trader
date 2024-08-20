"""
    Space Trader (PalmOS) | RPINerd, 2024

    Commander Status Screen
    Shows your stats, time played, etc.
"""

import tkinter as tk
from tkinter import ttk

# from ..constants import BKG_COLOR, GameStateID
from .screens import Screen

NO_QUARTER = "No quarters available"
NO_HIRE = "No one for hire"


class CommanderInfo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class ShipInfo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class SpecialCargo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class Personnel(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class Quests(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
