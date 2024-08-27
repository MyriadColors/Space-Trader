"""
    Space Trader (PalmOS) | RPINerd, 2024

    Character creation screen
"""

import tkinter as tk
from tkinter import ttk

from ..commander import Commander
from ..constants import BKG_HEX, FRG_HEX, GAME, Difficulty


class StatAdjuster(ttk.Frame):
    """
    A frame that contains a label, a decrement button, a value label, and an increment button.
    """

    def __init__(self, parent, label_text, initial_value, row, column, **kwargs) -> None:
        super().__init__(parent, **kwargs)

        global points_pool
        self.value = tk.IntVar(value=initial_value)
        self.label = ttk.Label(self, text=label_text)
        self.decrement = ttk.Button(self, text="-", command=self.decrement_value)
        self.value_label = ttk.Label(self, textvariable=self.value)
        self.increment = ttk.Button(self, text="+", command=self.increment_value)

        self.label.grid(row=row, column=column)
        self.decrement.grid(row=row, column=column + 1)
        self.value_label.grid(row=row, column=column + 2)
        self.increment.grid(row=row, column=column + 3)

    def get_value(self) -> int:
        return self.value.get()

    def decrement_value(self) -> None:
        if self.value.get() == 1:
            return
        self.value.set(max(self.value.get() - 1, 1))
        points_pool.set(points_pool.get() + 1)

    def increment_value(self) -> None:
        if points_pool.get() == 0 or self.value.get() == 10:
            return
        self.value.set(min(self.value.get() + 1, 10))
        points_pool.set(points_pool.get() - 1)


class CreateCommander(ttk.Frame):

    def __init__(self, parent) -> None:
        self.parent = parent
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()

    def create_widgets(self):

        # Initial values
        self.cmdr_name = tk.StringVar(value="Jameson")
        self.diff_current_value = 2
        global points_pool
        points_pool = tk.IntVar(value=0)

        # Title Bar
        self.header = ttk.Label(
            self,
            text="New Commander",
            style="Title.TLabel",
            # font=("Palm Pilot Bold", 28),
            anchor="center",
            background=FRG_HEX,
            foreground=BKG_HEX,
        )
        self.header.pack(expand=True, fill="x")

        # Commander name
        self.name_frame = ttk.Frame(self)
        self.name_label = ttk.Label(self.name_frame, text="Name:")
        self.name_entry = ttk.Entry(self.name_frame, textvariable=self.cmdr_name)
        self.name_label.pack(side="left")
        self.name_entry.pack(side="left")

        # Game difficulty selection
        self.difficulty_frame = ttk.Frame(self)
        self.difficulty_label = ttk.Label(self.difficulty_frame, text="Difficulty:")
        self.difficulty_dec = ttk.Button(self.difficulty_frame, style="TButton", text="-", command=self.dec_difficulty)
        self.difficulty_current = ttk.Label(
            self.difficulty_frame,
            text=Difficulty.name(self.diff_current_value),
        )
        self.difficulty_inc = ttk.Button(self.difficulty_frame, text="+", command=self.inc_difficulty)
        self.difficulty_label.pack(side="left")
        self.difficulty_dec.pack(side="left")
        self.difficulty_current.pack(side="left")
        self.difficulty_inc.pack(side="left")

        # Skill points allocation grid
        self.skills_frame = ttk.Frame(self)
        self.points_label = ttk.Label(self.skills_frame, text="Skill Points:")
        self.points_current = ttk.Label(self.skills_frame, textvariable=points_pool)
        self.pilot_skill = StatAdjuster(self.skills_frame, "Pilot:", 5, 0, 0)
        self.fighter_skill = StatAdjuster(self.skills_frame, "Fighter:", 5, 1, 0)
        self.trader_skill = StatAdjuster(self.skills_frame, "Trader:", 5, 2, 0)
        self.engineer_skill = StatAdjuster(self.skills_frame, "Engineer:", 5, 3, 0)

        self.points_label.pack(expand=True, fill="x")
        self.points_current.pack(expand=True, fill="x")
        self.pilot_skill.pack(expand=True, fill="x")
        self.fighter_skill.pack(expand=True, fill="x")
        self.trader_skill.pack(expand=True, fill="x")
        self.engineer_skill.pack(expand=True, fill="x")

        # Button to start the game
        self.start_button = ttk.Button(self, text="OK", command=self.cmdr_create, width=15)

        self.name_frame.pack(expand=True, fill="x")
        self.difficulty_frame.pack(expand=True, fill="x")
        self.skills_frame.pack(expand=True, fill="x")
        self.start_button.pack(expand=True)

    def dec_difficulty(self) -> None:
        print("Decreasing difficulty")
        print("Current value:", self.diff_current_value)
        new_difficulty = max(self.diff_current_value - 1, 0)
        print("New value:", new_difficulty)
        if new_difficulty == 0:
            self.difficulty_dec["state"] = "disabled"
        self.difficulty_inc["state"] = "enabled"
        self.difficulty_current["text"] = Difficulty.name(new_difficulty)
        self.diff_current_value = new_difficulty

    def inc_difficulty(self) -> None:
        print("Increasing difficulty")
        print("Current value:", self.diff_current_value)
        new_difficulty = min(self.diff_current_value + 1, 4)
        print("New value:", new_difficulty)
        if new_difficulty == 4:
            self.difficulty_inc["state"] = "disabled"
        self.difficulty_dec["state"] = "enabled"
        self.difficulty_current["text"] = Difficulty.name(new_difficulty)
        self.diff_current_value = new_difficulty

    def cmdr_create(self) -> None:

        # TODO Show a message box for invalid submissions
        if points_pool.get() != 0:
            print("You have unspent skill points!")
            return
        elif self.cmdr_name.get() == "":
            print("You must enter a name!")
            return
        else:
            cmdr = Commander(
                self.cmdr_name.get(),
                self.pilot_skill.get_value(),
                self.fighter_skill.get_value(),
                self.trader_skill.get_value(),
                self.engineer_skill.get_value(),
            )
            GAME["commander"] = cmdr
            GAME["difficulty"] = self.diff_current_value
            print(cmdr.pprint())
            self.destroy()
            self.parent.manager.build_screens()
