from GLOBAL import *
from tkinter import *
import tkinter.ttk as ttk
from World import *

from MenuPages.KeyBinds import *
from MenuPages.Statistics import *
from MenuPages.Instructions import *
from MenuPages.Settings import *

class PageMenu(Frame):
    def __init__(self, window, master, tab=None):
        super().__init__(master)
        self.window = window
        btn_width = 20

        self.config(width=900, height=600, bg="#1f3040")
        self.pack_propagate(0)

        self.back_button = ttk.Button(self, text="<- Back", width=btn_width, command=self.close)
        self.back_button.pack(anchor=NW, side=TOP,pady=(5), padx=5)


        self.show()

        self.notebook = ttk.Notebook(self)

        pages = {"Statistics": Statistics, "Instructions": Instructions, "Key Binds": KeyBinds, "Settings": Settings}
        self.pages_indexes = []

        for name, instance in pages.items():
            self.pages_indexes.append(name)
            self.notebook.add(instance(self.notebook, self), text=name)

        self.notebook.pack(expand=True, fill=BOTH)

        if tab != None:
            self.select_tab(tab)

    def select_tab(self, name):
        self.notebook.select(self.pages_indexes.index(name))

    def close(self):
        self.destroy()



    def show(self):
        self.place(x=self.window.screenW / 2 - self["width"] / 2,
                               y=self.window.screenH / 2 - self["height"] / 2)