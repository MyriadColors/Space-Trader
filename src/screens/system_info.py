"""
    Space Trader (PalmOS) | RPINerd, 2024

    Basic system information screen
"""

from tkinter import ttk

import src.ui_actions as actions

from .screens import Screen


class SystemInfo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        # Info Frame
        self.info_frame = ttk.Frame(self)
        self.info_frame.columnconfigure(0, weight=1)
        self.info_frame.columnconfigure(1, weight=1)
        info_headings = ["Name:", "Size:", "Tech Level:", "Government:", "Resources:", "Police:", "Pirates:"]
        for i, heading in enumerate(info_headings):
            ttk.Label(self.info_frame, text=heading, font=("Palm Pilot Bold", 14), justify="left").grid(
                row=i, column=0, sticky="ew"
            )
        #! Placeholder content
        for i in range(0, 7):
            ttk.Label(self.info_frame, text="Placeholder", font=("Palm Pilot Small", 14), justify="left").grid(
                row=i, column=1, sticky="ew"
            )
        self.info_frame.pack(fill="x", expand=True)

        # Pressure Frame
        self.pressure_frame = ttk.Frame(self)
        ttk.Label(self.pressure_frame, text=actions.get_system_info(), font=("Palm Pilot Small", 14)).grid(
            row=0, column=0
        )
        self.pressure_frame.pack(side="top", fill="both", expand=True)

        # Shortcut Frame
        self.shortcut_frame = ttk.Frame(self)
        ttk.Button(self.shortcut_frame, text="News", command=actions.buy_news).pack(side="left")
        self.shortcut_frame.pack(side="top", fill="both", expand=True)

    def change_screen(self, event):
        print(f"Changing screen to {event}")


class ShortRange(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Short Range Chart", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class LongRange(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Long Range Chart", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class TargetSystem(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Target System", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)


class AvgPrices(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
        self.pack(expand=True, fill="both")
        # self.create_widgets()

    def create_widgets(self):

        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text="Average Prices", font=("Palm Pilot Small", 24)).pack(fill="both", expand=True)
