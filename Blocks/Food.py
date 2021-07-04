from Blocks.Block import *

class Food(Block):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.name = "Food"
        self.color = "red"
        self.id = 3