from GLOBAL import *
from tkinter import *
import tkinter.ttk as ttk

class Statistics(Frame):
    def __init__(self, notebook, menu):
        super().__init__(notebook)
        self.menu = menu

        self.pack(fill='both', expand=True)

        Label(self, text=f"Highscore: {Global.data['highscore']}", font="System 17").pack(pady=(5), padx=5)