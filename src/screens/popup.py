import tkinter as tk

from src.constants import BKG_HEX, INTERNAL_RES, SCALAR


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
