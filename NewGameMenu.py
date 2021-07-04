from GLOBAL import *
from tkinter import *
import tkinter.ttk as ttk
from World import *
import time

class NewGameMenu(Frame):
    def __init__(self, window, master):
        super().__init__(master)
        self.window = window

        btn_width = 20

        Global.window.save.in_new_game_menu = True

        self.config(width=900, height=500, bg="#1f3040")
        self.pack_propagate(0)

        self.ai_snakes = Scale(self, from_=1, to=500, orient=HORIZONTAL, showvalue=True, length=200, label="AI Snakes")
        self.ai_snakes.pack(pady=5)
        self.ai_snakes.set(30)

        self.food_start = Scale(self, from_=0, to=500, orient=HORIZONTAL, showvalue=True, length=200, label="Starting Food")
        self.food_start.pack(pady=5)
        self.food_start.set(100)

        self.rocks_start = Scale(self, from_=0, to=20, orient=HORIZONTAL, showvalue=True, length=200, label="Rocks")
        self.rocks_start.pack(pady=5)
        self.rocks_start.set(5)

        self.restart_button = ttk.Button(self, text="Create New Game", width=btn_width, command=self.create_game)
        self.restart_button.pack(pady=(5, 50), padx=50)

    def create_game(self):
        Global.window.reset_save()
        Global.window.save.world = World(ai_snakes=self.ai_snakes.get(), food=self.food_start.get(), rocks=self.rocks_start.get())
        Global.window.save.in_new_game_menu = False
        self.destroy()

        Global.window.loop_tick()
        e = Label(Global.window.game_canvas, text="3", font="System 90", bg="#1f3040", width=2)
        e.pack(pady=50)

        self.update()
        time.sleep(1)
        e.config(text="2")

        self.update()
        time.sleep(1)
        e.config(text="1")
        self.update()
        time.sleep(1)
        e.destroy()



    def show(self):
        self.place(x=self.window.screenW / 2 - self["width"] / 2,
                               y=self.window.screenH / 2 - self["height"] / 2)