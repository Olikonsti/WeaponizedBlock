from GLOBAL import *
from tkinter import *
import tkinter.ttk as ttk
from VerticalScrolledFrame import *

class KeyBinds(Frame):
    def __init__(self, notebook, menu):
        super().__init__(notebook)
        self.menu = menu

        self.pack(fill='both', expand=True)

        self.frame = VerticalScrolledFrame(self)
        self.frame.pack(expand=True, fill=BOTH)

        Label(self.frame.interior, text=f"Gameplay", font="System 17", fg="yellow", justify=LEFT).pack(pady=(5), padx=5,anchor="w")
        Label(self.frame.interior, text=f"W, A, S, D: Change direction", font="System 17", justify=LEFT).pack(pady=(5), padx=50, anchor="w")
        Label(self.frame.interior, text=f"Space: Shoot", font="System 17", justify=LEFT).pack(pady=(5), padx=50, anchor="w")



        Label(self.frame.interior, text=f"Debugging", font="System 17", fg="yellow", justify=LEFT).pack(pady=(5), padx=5,
                                                                                            anchor="w")
        Label(self.frame.interior, text=f"Shift-T: Toggle Debug Mode", font="System 17", justify=LEFT).pack(pady=(5), padx=50,
                                                                                              anchor="w")
        Label(self.frame.interior, text=f"Shift-R: Toggle Render Mode", font="System 17", justify=LEFT).pack(pady=(5),
                                                                                                            padx=50,
                                                                                                            anchor="w")
        Label(self.frame.interior, text=f"Alt-G: Toggle God Mode", font="System 17", justify=LEFT).pack(pady=(5),
                                                                                                            padx=50,
                                                                                                            anchor="w")