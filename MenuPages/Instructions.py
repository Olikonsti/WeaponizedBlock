from GLOBAL import *
from tkinter import *
import tkinter.ttk as ttk
from VerticalScrolledFrame import *

class Instructions(Frame):
    def __init__(self, notebook, menu):
        super().__init__(notebook)
        self.menu = menu

        self.pack(fill='both', expand=True)

        self.frame = VerticalScrolledFrame(self)
        self.frame.pack(expand=True, fill=BOTH)

        Label(self.frame.interior, text=f"How to Play", font="System 17", fg="yellow", justify=LEFT).pack(pady=(5), padx=5,anchor="w")
        Label(self.frame.interior, text=f"Move around in the map, collect food (the red dots)\nand kill AI_Snakes by either eating them or shooting them", font="System 17", justify=LEFT).pack(pady=(5), padx=50, anchor="w")
        Button(self.frame.interior, text="See Key Binds", bg="#4E5D6C", command=lambda: self.menu.select_tab("Key Binds")).pack(pady=(5), padx=50, anchor="w")


        Label(self.frame.interior, text=f"How to Win", font="System 17", fg="yellow", justify=LEFT).pack(pady=(5), padx=5,
                                                                                            anchor="w")
        Label(self.frame.interior, text=f"Kill all other AI_Snakes to win (orange blocks)", font="System 17", justify=LEFT).pack(pady=(5), padx=50,
                                                                                              anchor="w")
