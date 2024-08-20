"""
    Space Trader (PalmOS) | RPINerd, 2024

    Buy Cargo Screen
"""

from tkinter import ttk

# from ..constants import BKG_COLOR, GameStateID
# from ..economy import TradeItemId
from .screens import Screen


class BuyCargo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class SellCargo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class BuyEquipment(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class SellEquipment(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class Bank(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
