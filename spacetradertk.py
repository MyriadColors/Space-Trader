"""
    Space Trader (PalmOS) | RPINerd, 08/07/24

    An early space strategy RPG game for PalmOS.

    This file is the start of a rewrite of the Space Trader game using Tkinter for the GUI.
"""

import tkinter as tk
from tkinter import ttk

import src.constants as c
import src.game_data as gd


def dec_difficulty() -> None:
    global diff_current_value
    diff_current_value = max(diff_current_value - 1, 0)
    if diff_current_value == 0:
        difficulty_dec["state"] = "disabled"
    difficulty_inc["state"] = "enabled"
    difficulty_current["text"] = c.Difficulty.name(diff_current_value)


def inc_difficulty() -> None:
    global diff_current_value
    diff_current_value = min(diff_current_value + 1, 4)
    if diff_current_value == 4:
        difficulty_inc["state"] = "disabled"
    difficulty_dec["state"] = "enabled"
    difficulty_current["text"] = c.Difficulty.name(diff_current_value)


window = tk.Tk()
window.title("Space Trader")
window.geometry("160x160")

# Title Bar
header = ttk.Label(window, text="New Commander", font=("Helvetica", 8))
header.pack()

# Commander name
name_frame = ttk.Frame(window)
name_label = ttk.Label(name_frame, text="Name:")
cmdr_name = tk.StringVar()
name_entry = ttk.Entry(name_frame, textvariable=cmdr_name)
name_label.pack(side="left")
name_entry.pack(side="left")

# Game difficulty selection
difficulty_frame = ttk.Frame(window)
diff_current_value = 2
difficulty_label = ttk.Label(difficulty_frame, text="Difficulty:")
difficulty_dec = ttk.Button(difficulty_frame, text="-", command=dec_difficulty)
difficulty_current = ttk.Label(
    difficulty_frame,
    text="Normal",
)
difficulty_inc = ttk.Button(difficulty_frame, text="+", command=inc_difficulty)
difficulty_label.pack()
difficulty_dec.pack()
difficulty_current.pack()
difficulty_inc.pack()

# Skill points allocation grid
points_pool = tk.IntVar(value=16)
pilot_points = tk.IntVar(value=1)
fighter_points = tk.IntVar(value=1)
trader_points = tk.IntVar(value=1)
engineer_points = tk.IntVar(value=1)

skills_frame = ttk.Frame(window)

points_label = ttk.Label(skills_frame, text="Skill Points:")
pilot_label = ttk.Label(skills_frame, text="Pilot:")
fighter_label = ttk.Label(skills_frame, text="Fighter:")
trader_label = ttk.Label(skills_frame, text="Trader:")
engineer_label = ttk.Label(skills_frame, text="Engineer:")

pilot_dec = ttk.Button(skills_frame, text="-")
pilot_inc = ttk.Button(skills_frame, text="+")
fighter_dec = ttk.Button(skills_frame, text="-")
fighter_inc = ttk.Button(skills_frame, text="+")
trader_dec = ttk.Button(skills_frame, text="-")
trader_inc = ttk.Button(skills_frame, text="+")
engineer_dec = ttk.Button(skills_frame, text="-")
engineer_inc = ttk.Button(skills_frame, text="+")

points_current = ttk.Label(skills_frame, textvariable=points_pool)
pilot_current = ttk.Label(skills_frame, textvariable=pilot_points)
fighter_current = ttk.Label(skills_frame, textvariable=fighter_points)
trader_current = ttk.Label(skills_frame, textvariable=trader_points)
engineer_current = ttk.Label(skills_frame, textvariable=engineer_points)

points_label.pack(side="left")
points_current.pack(side="left")

pilot_label.pack()
pilot_dec.pack(side="left")
pilot_current.pack(side="left")
pilot_inc.pack(side="left")

fighter_label.pack()
fighter_dec.pack(side="left")
fighter_current.pack(side="left")
fighter_inc.pack(side="left")

trader_label.pack()
trader_dec.pack(side="left")
trader_current.pack(side="left")
trader_inc.pack(side="left")

engineer_label.pack()
engineer_dec.pack(side="left")
engineer_current.pack(side="left")
engineer_inc.pack(side="left")

# Button to start the game
start_button = ttk.Button(window, text="OK", command=window.quit, width=15)

name_frame.pack()
difficulty_frame.pack()
skills_frame.pack()
start_button.pack()

window.mainloop()
