from GLOBAL import *
from tkinter import *
import tkinter.ttk as ttk

class WinScreen(Frame):
    def __init__(self, window, master):
        super().__init__(master)
        self.window = window

        btn_width = 20

        self.config(width=400, height=600, bg="#1f3040")
        self.pack_propagate(0)

        Label(self, text="You Won!").pack()

        self.restart_button = ttk.Button(self, text="New Game", style="Outline.TButton", width=btn_width, command=lambda: (Global.window.reset_save(), self.destroy()))
        self.restart_button.pack(pady=(5, 50), padx=50)


    def show(self):
        self.place(x=self.window.screenW / 2 - self["width"] / 2,
                               y=self.window.screenH / 2 - self["height"] / 2)