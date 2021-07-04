
from GLOBAL import *
import random
from WinScreen import *

# blocks
from Blocks.Block import *
from Blocks.Snake import *
from Blocks.AI_Snake import *
from Blocks.Food import *
from Blocks.Stone import *

class World:
    def __init__(self, empty=False, ai_snakes=100, food=100, rocks=5):
        self.empty = empty
        self.arrayx = 160
        self.arrayy = 100
        self.pixel_size = 7
        self.won = False

        self.food_count = 0
        self.aisnake_count = 0

        # fill array with zeros
        self.array = [[0 for x in range(self.arrayy)] for y in range(self.arrayx)]
        self.instance_array = []


        if not self.empty:
            while self.place_block(random.randint(1, self.arrayx), random.randint(1, 2), Snake) != 0:
                pass


            for i in range(int(ai_snakes)):
                while self.place_block(random.randint(1, self.arrayx), random.randint(20, self.arrayy), AI_Snake) != 0:
                    pass

            for i in range(food):
                self.generate_food()

            for i in range(rocks):
                self.generate_stone()

    def update(self, tick):
        if not self.empty:
            if tick % 10 == 0:
                self.food_count = 0
                self.aisnake_count = 0
                for i in self.instance_array:
                    if i.name == "Food":
                        self.food_count += 1
                    elif i.name == "AI_Snake":
                        self.aisnake_count += 1
                if self.food_count < 200:
                    for i in range(3):
                        self.generate_food()

                if self.aisnake_count < 1 and not self.won:
                    self.won = True
                    Screen_Message("You Won!", 1000, fg="yellow", bg="orange")
                    Global.window.after(1500, self.win_action)


    def win_action(self):
        Global.window.new_game()
        Global.window.save.paused = True
        if Global.window.save.score > Global.data["highscore"]:
            Screen_Message("New Highscore!", 1000, bg="orange")
            Global.data["highscore"] = Global.window.save.score


    def place_block(self, x, y, Block):
        try:
            if self.array[x][y] == 0:
                Block(self, x, y)
                return 0
        except:
            pass
        return 1

    def generate_food(self):
        self.place_block(random.randint(1, self.arrayx), random.randint(1, self.arrayy), Food)

    def generate_stone(self):
        x, y = random.randint(5, self.arrayx - 5), random.randint(5, self.arrayy - 5)
        steps = random.randint(1, 8)

        x0 = x
        y0 = y

        radius = steps

        for x in range(x0 - radius, x0 + radius + 1):
            for y in range(y0 - radius, y0 + radius + 1):
                deb = radius - abs(x0 - x) - abs(y0 - y)
                if deb >=0:
                    Stone(self, x, y)


