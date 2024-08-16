import tkinter as tk

from src.constants import BKG_HEX, INTERNAL_RES, SCALAR


class Screen(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BKG_HEX, height=INTERNAL_RES * SCALAR, width=INTERNAL_RES * SCALAR)
        self.pack(expand=True, fill="both")

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

    def create_widgets(self):
        pass
