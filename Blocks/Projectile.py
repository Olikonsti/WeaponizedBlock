import random
from Interface.Screen_Message import *
from Blocks.Block import *

class Projectile(Block):
    def __init__(self, world, x, y, x_dir, y_dir):
        super().__init__(world, x, y)
        self.name = "Projectile"
        self.color = "#ffff08"
        self.id = 7

        self.movement = [x_dir, y_dir]

    def update(self, tick):
        Block.update(self, tick)

        self.move()

    def move(self):
        try:
            before_block = self.world.array[self.x + self.movement[0]][self.y + self.movement[1]]
            if before_block != 0 and before_block != self:
                Food = ["Food", "Snake", "AI_Snake", "Projectile", "AI_Projectile", "Stone"]

                if before_block.name in Food:
                    before_block.kill(self.get_info())
                    if before_block.name == "AI_Snake":
                        Screen_Message("Enemy killed", 75, bg="green")
                        Global.window.save.score += 10
                    if self.move_to(self.x + self.movement[0], self.y + self.movement[1]) == 1:
                        self.kill("SELF")
                    if before_block.name == "Stone":
                        self.kill("SELF")

            else:
                if self.move_to(self.x + self.movement[0], self.y + self.movement[1]) == 1:
                    self.kill("SELF")


        except:
            pass