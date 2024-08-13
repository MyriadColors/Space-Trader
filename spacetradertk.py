"""
    Space Trader (PalmOS) | RPINerd, 08/07/24

    An early space strategy RPG game for PalmOS.

    This file is the start of a rewrite of the Space Trader game using Tkinter for the GUI.
"""

import tkinter as tk
from tkinter import ttk

import src.constants as c
import src.game_data as gd
from src.commander import Commander


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


def refill_pool() -> None:
    pts = points_pool.get()
    pts += 1
    points_pool.set(pts)


def spend_pool() -> bool:
    pts = points_pool.get()
    if pts == 0:
        return False
    pts -= 1
    points_pool.set(pts)
    return True


def dec_pilot() -> None:
    pts = pilot_points.get()
    if pts - 1 > 0:
        refill_pool()
        pts -= 1
        pilot_points.set(pts)


def inc_pilot() -> None:
    pts = pilot_points.get()
    if pts == 10:
        return
    if spend_pool():
        pts += 1
        pilot_points.set(pts)


def dec_fighter() -> None:
    pts = fighter_points.get()
    if pts - 1 > 0:
        refill_pool()
        pts -= 1
        fighter_points.set(pts)


def inc_fighter() -> None:
    pts = fighter_points.get()
    if pts == 10:
        return
    if spend_pool():
        pts += 1
        fighter_points.set(pts)


def dec_trader() -> None:
    pts = trader_points.get()
    if pts - 1 > 0:
        refill_pool()
        pts -= 1
        trader_points.set(pts)


def inc_trader() -> None:
    pts = trader_points.get()
    if pts == 10:
        return
    if spend_pool():
        pts += 1
        trader_points.set(pts)


def dec_engineer() -> None:
    pts = engineer_points.get()
    if pts - 1 > 0:
        refill_pool()
        pts -= 1
        engineer_points.set(pts)


def inc_engineer() -> None:
    pts = engineer_points.get()
    if pts == 10:
        return
    if spend_pool():
        pts += 1
        engineer_points.set(pts)


def cmdr_create():
    cmdr = Commander(
        cmdr_name.get(), pilot_points.get(), fighter_points.get(), trader_points.get(), engineer_points.get()
    )
    print(cmdr.pprint())
    window.destroy()


window = tk.Tk()
window.title("Space Trader")
window.minsize("160", "160")
window.geometry("160x160")
window.configure(bg=c.BKG_HEX)

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
difficulty_label.pack(side="left")
difficulty_dec.pack(side="left")
difficulty_current.pack(side="left")
difficulty_inc.pack(side="left")

# Skill points allocation grid
points_pool = tk.IntVar(value=16)
pilot_points = tk.IntVar(value=1)
fighter_points = tk.IntVar(value=1)
trader_points = tk.IntVar(value=1)
engineer_points = tk.IntVar(value=1)

# Skill points allocation grid
points_pool = tk.IntVar(value=16)
pilot_points = tk.IntVar(value=1)
fighter_points = tk.IntVar(value=1)
trader_points = tk.IntVar(value=1)
engineer_points = tk.IntVar(value=1)

skills_frame = ttk.Frame(window, height=55, width=80)

points_label = ttk.Label(skills_frame, text="Skill Points:", justify="left")
pilot_label = ttk.Label(skills_frame, text="Pilot:", justify="left")
fighter_label = ttk.Label(skills_frame, text="Fighter:", justify="left")
trader_label = ttk.Label(skills_frame, text="Trader:", justify="left")
engineer_label = ttk.Label(skills_frame, text="Engineer:", justify="left")

pilot_dec = ttk.Button(skills_frame, text="-", width=2, command=dec_pilot)
pilot_inc = ttk.Button(skills_frame, text="+", width=2, command=inc_pilot)
fighter_dec = ttk.Button(skills_frame, text="-", width=2, command=dec_fighter)
fighter_inc = ttk.Button(skills_frame, text="+", width=2, command=inc_fighter)
trader_dec = ttk.Button(skills_frame, text="-", width=2, command=dec_trader)
trader_inc = ttk.Button(skills_frame, text="+", width=2, command=inc_trader)
engineer_dec = ttk.Button(skills_frame, text="-", width=2, command=dec_engineer)
engineer_inc = ttk.Button(skills_frame, text="+", width=2, command=inc_engineer)

points_current = ttk.Label(skills_frame, textvariable=points_pool)
points_current.grid(row=0, column=1)
pilot_current = ttk.Label(skills_frame, textvariable=pilot_points)
pilot_current.grid(row=1, column=2)
fighter_current = ttk.Label(skills_frame, textvariable=fighter_points)
fighter_current.grid(row=2, column=2)
trader_current = ttk.Label(skills_frame, textvariable=trader_points)
trader_current.grid(row=3, column=2)
engineer_current = ttk.Label(skills_frame, textvariable=engineer_points)
engineer_current.grid(row=4, column=2)

points_label.grid(row=0, column=0, columnspan=2)
points_current.grid(row=0, column=2)

pilot_label.grid(row=1, column=0, sticky="nsew")
pilot_dec.grid(row=1, column=1, sticky="nsew")
pilot_current.grid(row=1, column=2, sticky="nsew")
pilot_inc.grid(row=1, column=3, sticky="nsew")

fighter_label.grid(row=2, column=0, sticky="nsew")
fighter_dec.grid(row=2, column=1, sticky="nsew")
fighter_current.grid(row=2, column=2, sticky="nsew")
fighter_inc.grid(row=2, column=3, sticky="nsew")

trader_label.grid(row=3, column=0)
trader_dec.grid(row=3, column=1)
trader_current.grid(row=3, column=2)
trader_inc.grid(row=3, column=3)

engineer_label.grid(row=4, column=0)
engineer_dec.grid(row=4, column=1)
engineer_current.grid(row=4, column=2)
engineer_inc.grid(row=4, column=3)

# Button to start the game
start_button = ttk.Button(window, text="OK", command=cmdr_create, width=15)

name_frame.pack(expand=True)
difficulty_frame.pack(expand=True)
skills_frame.pack(expand=True)
start_button.pack(expand=True)

window.tk.call("tk", "scaling", 4.0)

window.mainloop()
