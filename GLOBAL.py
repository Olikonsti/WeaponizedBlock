

class GLOBAL:
    def __init__(self):
        self.version = 1.2
        self.window = None

        # data stores data forever
        self.data = {"highscore": 0,
                     "canvas_color": "#0C041E",
                     "fps": 60
                     }

Global = GLOBAL()