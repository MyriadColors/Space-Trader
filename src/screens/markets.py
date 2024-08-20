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
        # self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Buy Cargo", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class SellCargo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        # self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Sell Cargo", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class BuyEquipment(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        # self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Buy Equipment", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class SellEquipment(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        # self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Sell Equipment", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class Bank(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        # self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Bank", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)
