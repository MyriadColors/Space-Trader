"""
    Space Trader (PalmOS) | RPINerd, 2024

    Buy Cargo Screen
"""

import tkinter as tk
from random import randint
from tkinter import ttk

import src.ui_actions as actions

# from ..constants import BKG_COLOR, GameStateID
from ..economy import TradeItemId
from .screens import Screen


class BuyCargo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)

    def create_widgets(self):
        self.table_frame = ttk.Frame(self)
        for i, value in enumerate(TradeItemId.lst()):
            ttk.Button(self.table_frame, text=randint(0, 42)).grid(row=i, column=0)
            ttk.Label(self.table_frame, text=value).grid(row=i, column=1)
            ttk.Button(self.table_frame, text="Max", command=actions.buy_good).grid(row=i, column=2)
            ttk.Label(self.table_frame, text="1234 cr.").grid(row=i, column=3)
        self.table_frame.pack(fill="both", expand=True)


class SellCargo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)

    def create_widgets(self):
        self.table_frame = ttk.Frame(self)
        for i, value in enumerate(TradeItemId.lst()):
            ttk.Button(self.table_frame, text="0").grid(row=i, column=0)
            ttk.Label(self.table_frame, text=value).grid(row=i, column=1)
            ttk.Button(self.table_frame, text="All", command=actions.sell_good).grid(row=i, column=2)
            ttk.Label(self.table_frame, text="15cr").grid(row=i, column=3)
        self.table_frame.pack(fill="both", expand=True)


class BuyEquipment(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class SellEquipment(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class Bank(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
