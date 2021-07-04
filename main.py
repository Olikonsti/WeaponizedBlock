from Window import *

try:
    Window()
except Exception as e:
    import tkinter.messagebox as msg
    msg.showerror("Weaponized Block Error", f"Program exited with code 1. Please search for 'save.pdump' in the gamefiles and delete it.\n ERROR: {e}")
print("Exited.")