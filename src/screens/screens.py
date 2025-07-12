import tkinter as tk
from tkinter import ttk

import src.ui_actions as actions
from src.constants import BKG_HEX, FRG_HEX, INTERNAL_RES, SCALAR


def render_bank_account(parent, show_debt=False, position="bottom_right"):
    """
    Centralized bank account renderer function.

    Args:
        parent: The parent widget to attach the bank account display to
        show_debt: Whether to also display debt information
        position: Where to position the bank account info ("bottom_right", "grid", "inline")

    Returns:
        dict: Dictionary containing the created labels for potential updates
    """
    bank_info = {}

    if position == "grid":
        # For use in grid layouts (like CommanderInfo screen)
        if show_debt:
            bank_info["cash_label"] = ttk.Label(parent, text=actions.get_formatted_credits())
            bank_info["debt_label"] = ttk.Label(parent, text=actions.get_formatted_debt())
        else:
            bank_info["credits_label"] = ttk.Label(parent, text=actions.get_credits())

    elif position == "inline":
        # For inline display within frames
        frame = ttk.Frame(parent)
        bank_info["frame"] = frame

        if show_debt:
            cash_text = f"Cash: {actions.get_formatted_credits()}"
            debt_text = f"Debt: {actions.get_formatted_debt()}"
            bank_info["cash_label"] = ttk.Label(frame, text=cash_text)
            bank_info["debt_label"] = ttk.Label(frame, text=debt_text)
            bank_info["cash_label"].pack(side="left", padx=5)
            bank_info["debt_label"].pack(side="left", padx=5)
        else:
            bank_info["credits_label"] = ttk.Label(frame, text=actions.get_credits())
            bank_info["credits_label"].pack()

    else:  # bottom_right (default)
        # Standard bottom-right positioning for most screens
        bank_info["credits_label"] = ttk.Label(parent, text=actions.get_credits())
        bank_info["credits_label"].place(relx=1, rely=1, anchor="se")

    return bank_info


class Heading(ttk.Frame):

    def __init__(self, parent, heading: str):
        self.parent = parent
        super().__init__(parent)
        self.heading = heading
        self.create_widgets()
        self.pack()

    def create_widgets(self):

        self.heading = ttk.Label(self, text=self.heading, style="Title.TLabel")
        self.heading.pack(side="left")

        self.b = ttk.Button(
            self,
            text="B",
            width=2,
            # height=1,
            command=lambda: self.shortcut_trigger(self, "B"),
        )
        self.b.pack(side="right")
        self.s = ttk.Button(
            self,
            text="S",
            width=2,
            # height=1,
            command=lambda: self.shortcut_trigger(self, "S"),
        )
        self.s.pack(side="right")
        self.y = ttk.Button(
            self,
            text="Y",
            width=2,
            # height=1,
            command=lambda: self.shortcut_trigger(self, "Y"),
        )
        self.y.pack(side="right")
        self.w = ttk.Button(
            self,
            text="W",
            width=2,
            # height=1,
            command=lambda: self.shortcut_trigger(self, "W"),
        )
        self.w.pack(side="right")

        self.underline = tk.Canvas(self, width=INTERNAL_RES * SCALAR, height=2, bg=FRG_HEX)
        self.underline.pack(side="bottom", expand=True, fill="x")

    def shortcut_trigger(event, self, key):
        # print(f"self type: {type(self)}\nself: {self}")
        # print(f"event type: {type(event)}\nevent: {event}, key: {key}")
        # for attrib in getattr(event, "__dict__", {}):
        #     print(f"attrib: {attrib}")
        print(f"Shortcut triggered: {key}")
        self.parent.manager.go_to_screen(key)


class Screen(ttk.Frame):

    def __init__(self, parent, screen_title: str, manager) -> None:
        self.manager = manager
        self.screen_title = screen_title
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)

        self.header = Heading(self, self.screen_title)

        # Bind the game shortcut keys
        self.bind_all("<KeyPress-b>", self.change_screen)
        self.bind_all("<KeyPress-s>", self.change_screen)
        self.bind_all("<KeyPress-y>", self.change_screen)
        self.bind_all("<KeyPress-e>", self.change_screen)
        self.bind_all("<KeyPress-q>", self.change_screen)
        self.bind_all("<KeyPress-p>", self.change_screen)
        self.bind_all("<KeyPress-k>", self.change_screen)
        self.bind_all("<KeyPress-i>", self.change_screen)
        self.bind_all("<KeyPress-c>", self.change_screen)
        self.bind_all("<KeyPress-g>", self.change_screen)
        self.bind_all("<KeyPress-w>", self.change_screen)
        self.bind_all("<KeyPress-o>", self.change_screen)

        self.create_widgets()

    def change_screen(self, event):
        print(f"Changing screen to {event.keysym}")
        self.manager.go_to_screen(event.keysym.upper())

    def create_widgets(self):
        #! Placeholder id frame
        self.id_frame = ttk.Frame(self)
        ttk.Label(self.id_frame, text=self.screen_title, justify="center").pack(fill="x", expand=True)
        ttk.Label(self.id_frame, text="Not Implemented", justify="center").pack(fill="x", expand=True)
        self.id_frame.pack(fill="both", expand=True)


class Popup(ttk.Frame):

    def __init__(self, parent, title, content: ttk.Frame, height: int = INTERNAL_RES * SCALAR):
        super().__init__(parent, bg=BKG_HEX, height=height, width=INTERNAL_RES * SCALAR)
        self.pack(expand=True, fill="both")
        self.title = title
        self.content = content
        self.create_widgets()

    def create_widgets(self):
        self.title = ttk.Label(self, text=self.title)
        self.title.pack()
        self.message = ttk.Label(self, text=self.message)
        self.message.pack()
        self.ok = ttk.Button(self, text="OK", command=self.destroy)
        self.ok.pack()
