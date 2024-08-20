"""
    Space Trader (PalmOS) | RPINerd, 2024

    Shipyard Screen
    Counterintuitively, not actually where you buy ships.
    Houses refuel, repair, escape pod purchase and then link to ship sales.
"""

import tkinter as tk
from tkinter import ttk

# from ..constants import BKG_COLOR
# from ..game_data import ShipID
import src.ui_actions as actions

from .screens import Screen

FUEL_STATUS = "You have fuel to fly {0} parsecs."
FULL_TANK = "Your tank cannot hold more fuel."
HULL_STATUS = "Your hull strength is at {0}%."
FULL_HULL = "No repairs are needed."
SHIP_SALES = "No new ships are for sale."
ESCAPE_POD = "No escape pods are for sale."


class Shipyard(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)

    def create_widgets(self):

        # Fuel Frame
        self.fuel_frame = ttk.Frame(self)
        ttk.Label(self.fuel_frame, text=FUEL_STATUS.format(0), font=("Palm Pilot Small", 14)).pack()
        ttk.Button(self.fuel_frame, text="Refuel", command=actions.buy_fuel).pack()
        self.fuel_frame.pack(side="top", fill="both", expand=True)

        # Hull Frame
        self.hull_frame = ttk.Frame(self)
        ttk.Label(self.hull_frame, text=HULL_STATUS.format(0), font=("Palm Pilot Small", 14)).pack()
        ttk.Button(self.hull_frame, text="Repair", command=actions.repair).pack()
        self.hull_frame.pack(side="top", fill="both", expand=True)

        # Escape Pod Frame
        self.escape_pod_frame = ttk.Frame(self)
        ttk.Label(self.escape_pod_frame, text=ESCAPE_POD, font=("Palm Pilot Small", 14)).pack()
        ttk.Button(self.escape_pod_frame, text="Buy Escape Pod", command=actions.buy_pod).pack()
        self.escape_pod_frame.pack(side="top", fill="both", expand=True)

        # Ship Sales Frame
        self.ship_sales_frame = ttk.Frame(self)
        ttk.Label(self.ship_sales_frame, text=SHIP_SALES, font=("Palm Pilot Small", 14)).pack()
        ttk.Button(self.ship_sales_frame, text="Buy Ship", command=actions.buy_ship).pack()
        self.ship_sales_frame.pack(side="top", fill="both", expand=True)


class BuyShip(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
