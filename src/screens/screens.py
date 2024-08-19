import tkinter as tk
from tkinter import ttk

from src.constants import BKG_HEX, FRG_HEX, INTERNAL_RES, SCALAR


class Heading(tk.Frame):

    def __init__(self, parent, heading: str):
        super().__init__(parent)
        self.parent = parent
        self.heading = heading
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.heading = tk.Label(self, text=self.heading, font=("Palm Pilot Bold", 16), fg=BKG_HEX, bg=FRG_HEX)
        self.heading.pack(side="left")

        self.b = tk.Button(
            self,
            text="B",
            font=("Palm Pilot Small", 14),
            fg=FRG_HEX,
            bg=BKG_HEX,
            width=2,
            height=1,
            command=lambda: self.shortcut_trigger(self, "B"),
        )
        self.b.pack(side="right")
        self.s = tk.Button(
            self,
            text="S",
            font=("Palm Pilot Small", 14),
            fg=FRG_HEX,
            bg=BKG_HEX,
            width=2,
            height=1,
            command=lambda: self.shortcut_trigger(self, "S"),
        )
        self.s.pack(side="right")
        self.y = tk.Button(
            self,
            text="Y",
            font=("Palm Pilot Small", 14),
            fg=FRG_HEX,
            bg=BKG_HEX,
            width=2,
            height=1,
            command=lambda: self.shortcut_trigger(self, "Y"),
        )
        self.y.pack(side="right")
        self.w = tk.Button(
            self,
            text="W",
            font=("Palm Pilot Small", 14),
            fg=FRG_HEX,
            bg=BKG_HEX,
            width=2,
            height=1,
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
        self.parent.change_screen(event)


class Screen(tk.Frame):

    def __init__(self, parent, screen_title: str, manager) -> None:
        self.manager = manager
        s = ttk.Style()
        s.configure("TFrame", background=BKG_HEX)
        super().__init__(parent, background=BKG_HEX, height=INTERNAL_RES * SCALAR, width=INTERNAL_RES * SCALAR)
        self.pack(expand=True, fill="both")

        self.header = Heading(self, screen_title)

        # Bind the game shortcut keys
        self.bind_all("<Escape>", self.quit)
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

    def quit(self, event):
        self.destroy()

    def change_screen(self, event):
        print(f"Changing screen to {event.keysym.upper()}")
        self.manager.go_to_screen(event.keysym.upper())

    def create_widgets(self):
        pass


class Popup(tk.Frame):

    def __init__(self, parent, title, content: tk.Frame, height: int = INTERNAL_RES * SCALAR):
        super().__init__(parent, bg=BKG_HEX, height=height, width=INTERNAL_RES * SCALAR)
        self.pack(expand=True, fill="both")
        self.title = title
        self.content = content
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, text=self.title)
        self.title.pack()
        self.message = tk.Label(self, text=self.message)
        self.message.pack()
        self.ok = tk.Button(self, text="OK", command=self.destroy)
        self.ok.pack()
