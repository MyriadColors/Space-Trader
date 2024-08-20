"""
    Space Trader (PalmOS) | RPINerd, 2024

    Shipyard Screen
    Counterintuitively, not actually where you buy ships.
    Houses refuel, repair, escape pod purchase and then link to ship sales.
"""

from tkinter import ttk

# from ..constants import BKG_COLOR
# from ..game_data import ShipID
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


class BuyShip(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
