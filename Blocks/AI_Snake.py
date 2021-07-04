import random

from Blocks.Block import *
from Blocks.AI_Projectile import *

class AI_Snake(Block):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.name = "AI_Snake"
        self.color = "#ff6200"
        self.id = 2
        self.random_shoot_delay = random.randint(70, 500)

        self.change_direction()


    def change_direction(self):
        rand = random.randint(0, 3)
        if rand == 0:
            self.movement = [0, -1]
        if rand == 1:
            self.movement = [0, 1]
        if rand == 2:
            self.movement = [-1, 0]
        if rand == 3:
            self.movement = [1, 0]

    def shoot(self):
        x_dir = self.movement[0]
        y_dir = self.movement[1]
        while x_dir == 0 and y_dir == 0:
            x_dir = random.randint(-1, 1)
            y_dir = random.randint(-1, 1)
        for i in range(1):
            AI_Projectile(self.world, self.x + x_dir * (i + 2), self.y + y_dir * (i + 2), x_dir, y_dir)

    def update(self, tick):
        Block.update(self, tick)
        if tick % random.randint(1, 1000) == 0:
            self.change_direction()

        if tick % 3 == 0:
            self.move()
        if tick % self.random_shoot_delay == 0:
            self.shoot()

    def move(self):
        try:
            before_block = self.world.array[self.x + self.movement[0]][self.y + self.movement[1]]
            if before_block != 0 and before_block != self:
                Food = ["Food", "Snake"]
                if before_block.name in Food:
                    before_block.kill(self.get_info())
                    if self.move_to(self.x + self.movement[0], self.y + self.movement[1]) == 1:
                        self.change_direction()
            else:
                if self.move_to(self.x + self.movement[0], self.y + self.movement[1]) == 1:
                    self.change_direction()
        except:
            self.change_direction()