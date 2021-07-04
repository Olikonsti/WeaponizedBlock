from GLOBAL import *
from tkinter import *
import tkinter.ttk as ttk
from Interface.VerticalScrolledFrame import *
from tkinter import colorchooser
from tkinter import messagebox

class Settings(Frame):
    def __init__(self, notebook, menu):
        super().__init__(notebook)
        self.menu = menu

        self.pack(fill='both', expand=True)

        self.frame = VerticalScrolledFrame(self)
        self.frame.pack(expand=True, fill=BOTH)

        self.reset_button = Button(self, text="Reset to default", bg="#1F3040", command=self.reset)
        self.reset_button.pack(anchor="e")

        Label(self.frame.interior, text=f"Background Color", font="System 17", fg="yellow", justify=LEFT).pack(pady=(5), padx=5,anchor="w")
        Button(self.frame.interior, text="Select Color", bg="#4E5D6C",
               command=self.select_color).pack(pady=(2), padx=50, anchor="w")
        self.color_label = Label(self.frame.interior, text=Global.data['canvas_color'], font="System 17", justify=LEFT); self.color_label.pack(pady=(2), padx=50,
                                                                                              anchor="w")


        Label(self.frame.interior, text=f"Maximum TPS/FPS (default: 60)", font="System 17", fg="yellow", justify=LEFT).pack(pady=(5),
                                                                                                               padx=5,
                                                                                                               anchor="w")
        self.fps = Scale(self.frame.interior, from_=2, to=198, orient=HORIZONTAL, showvalue=True, length=200, command=self.select_fps)
        self.fps.pack(pady=(2), padx=50, anchor="w")
        self.fps.set(Global.data["fps"])
        Label(self.frame.interior, text=f"(Can make the Game run faster/slower [Cheating])", font="System 17",
              justify=LEFT).pack(pady=(2), padx=50, anchor="w")

    def reset(self):
        if messagebox.askquestion("Warning", "Are you sure, you want to reset the settings to default?") == "yes":
            a = GLOBAL()
            Global.data = a.data

            self.color_label.config(text=Global.data["canvas_color"])
            Global.window.game_canvas.config(bg=Global.data["canvas_color"])
            self.fps.set(Global.data["fps"])

    def select_fps(self, event=None):
        Global.data["fps"] = self.fps.get()

    def select_color(self):
        ret = colorchooser.askcolor(color=Global.data["canvas_color"])[1]
        if ret != None:
            Global.data["canvas_color"] = ret
        self.color_label.config(text=Global.data["canvas_color"])
        Global.window.game_canvas.config(bg=Global.data["canvas_color"])