from GLOBAL import *
from tkinter import *
import tkinter.ttk as ttk


class PauseMenu(Frame):
    def __init__(self, window, master):
        super().__init__(master)
        self.window = window

        btn_width = 20

        self.config(width=200, height=400, bg="#1f3040")
        self.pack_propagate(0)

        self.resume_button = ttk.Button(self, text="Resume", width=btn_width, command=lambda: window.pause_invoke(""))
        self.resume_button.pack(pady=(50, 5), padx=50)

        self.menu_button = ttk.Button(self, text="Menu", width=btn_width, style="Outline.TButton", command=lambda: Global.window.open_menu())
        self.menu_button.pack(pady=(5, 5), padx=50)

        self.restart_button = ttk.Button(self, text="New Game", style="Outline.TButton", width=btn_width, command=lambda: (window.new_game(), self.hide()))
        self.restart_button.pack(pady=(5, 50), padx=50)

    def show(self):
        self.place(x=self.window.screenW / 2 - self.window.pause_frame["width"] / 2,
                               y=self.window.screenH / 2 - self.window.pause_frame["height"] / 2)

    def hide(self):
        self.place_forget()