from GLOBAL import *

messages = []

class Screen_Message():
    def __init__(self, text, ticks, fg="white", bg="grey"):
        messages.append(self)
        self.text = text
        self.fg = fg
        self.bg = bg
        self.ticks = ticks
        self.starttick = Global.window.tick
        self.stoptick = self.starttick + self.ticks

    def update(self):
        if Global.window.tick > self.stoptick:
            messages.remove(self)