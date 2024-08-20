"""
    Space Trader (PalmOS) | RPINerd, 2024

    Basic system information screen
"""

import tkinter as tk
from tkinter import ttk

import src.ui_actions as actions

from .screens import Screen


class SystemInfo(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)

    def create_widgets(self):

        # Info Frame
        self.info_frame = ttk.Frame(self)
        self.info_frame.columnconfigure(0, weight=1)
        self.info_frame.columnconfigure(1, weight=1)
        info_headings = ["Name:", "Size:", "Tech Level:", "Government:", "Resources:", "Police:", "Pirates:"]
        for i, heading in enumerate(info_headings):
            ttk.Label(self.info_frame, text=heading, style="Heading.TLabel", justify="left").grid(
                row=i, column=0, sticky="ew"
            )
        #! Placeholder content
        for i in range(0, 7):
            ttk.Label(self.info_frame, text="Placeholder", justify="left").grid(row=i, column=1, sticky="ew")
        self.info_frame.pack(fill="x", expand=True)

        # Pressure Frame
        self.pressure_frame = ttk.Frame(self)
        ttk.Label(self.pressure_frame, text=actions.get_system_info()).grid(row=0, column=0)
        self.pressure_frame.pack(side="top", fill="both", expand=True)

        # Shortcut Frame
        self.shortcut_frame = ttk.Frame(self)
        ttk.Button(self.shortcut_frame, text="News", command=actions.buy_news).pack(side="left")
        self.shortcut_frame.pack(side="top", fill="both", expand=True)

    def change_screen(self, event):
        # TODO probably can be a super method
        pass


class ShortRange(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class LongRange(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class TargetSystem(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)


class AvgPrices(Screen):

    def __init__(self, parent, screen_title, manager) -> None:
        super().__init__(parent, screen_title, manager)
