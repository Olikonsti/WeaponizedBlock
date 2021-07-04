from GLOBAL import *

class Block:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.last_x = 0
        self.last_y = 0
        self.alive = True
        self.color = "red"
        self.id = 0
        self.name = "Blocks.Block"
        self.world.instance_array.append(self)
        if self.place_to_array(self.x, self.y) == 1:
            self.kill("SELF:SPACE")
            del self


    def update(self, tick):
        try:
            if self.world.array[self.x][self.y] == self or self.world.array[self.last_x][self.last_y] == self:
                pass
            else:
                self.kill("SELF")
        except:
            self.kill("SELF_EXCEPTION")

    def move_to(self, x, y):
        if x < 1 or y < 1 or x > self.world.arrayx - 2 or y > self.world.arrayy - 2:
            return 1

        try:
            self.world.array[x][y] = self
            try:
                self.world.array[self.last_x][self.last_y] = 0
            except:
                pass

            self.last_x = self.x
            self.last_y = self.y

            self.x = x
            self.y = y
            return 0

        except:
            return 1

    def kill(self, murder):
        self.alive = False
        try:
            self.world.array[self.x][self.y] = 0
        except:
            pass
        try:
            self.world.array[self.last_x][self.last_y] = 0
        except:
            pass
        try:
            self.world.instance_array.remove(self)
        except:
            pass


    def place_to_array(self, x, y):
        if x < 1 or y < 1 or x > self.world.arrayx - 2 or y > self.world.arrayy - 2:
            return 1

        self.world.array[x][y] = self
        return 0

    def get_info(self):
        return f"{self.name}:{self.id} with color {self.color} at ({self.x}, {self.y})"

    def print_info(self):
        print(f"\n{self.name}:{self.id} with color {self.color} at ({self.x}, {self.y})")
