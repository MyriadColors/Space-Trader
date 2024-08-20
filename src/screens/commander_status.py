"""
    Space Trader (PalmOS) | RPINerd, 2024

    Commander Status Screen
    Shows your stats, time played, etc.
"""

from tkinter import ttk

# from ..constants import BKG_COLOR, GameStateID
from .screens import Screen

NO_QUARTER = "No quarters available"
NO_HIRE = "No one for hire"


class CommanderInfo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        # self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Commander Info", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class ShipInfo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        # self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Ship Info", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class SpecialCargo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        # self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Special Cargo", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class Personnel(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        # self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Personnel", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class Quests(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        # self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Quests", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)
