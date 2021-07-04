import random

from Blocks.Block import *

class Stone(Block):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.name = "Stone"
        colors = ["#303030", "#2e2e2e", "#3b3b3b", "#424242", "#1f1f1f"]   # very dark grey colors
        self.color = random.choice(colors)