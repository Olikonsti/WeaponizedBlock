from Blocks.Block import *
from Blocks.Projectile import *
from Interface.Screen_Message import *
import random


class Snake(Block):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.name = "Snake"
        self.color = "#00d93a"
        self.id = 1
        self.energy = 1
        self.k_e_clicked = False
        rand = random.randint(0, 3)
        self.movement = [1, 0]

    def kill(self, murder):
        if not Global.window.save.godmode:
            Block.kill(self, murder)
            Screen_Message("You Died", 500, fg="#ff1100", bg="darkred")
            Global.window.after(1500, lambda: (Global.window.new_game(), ))
        else:
            pass

    def update(self, tick):
        Block.update(self, tick)
        self.check_keys()
        if tick % 4 == 0:
            self.move()
            Global.window.energy_count_label.config(text=f"Energy: {self.energy}")
            Global.window.snake_count_label.config(text=f"Snakes: {self.world.aisnake_count}")

    def check_keys(self):
        if Global.window.KEY_W.clicked:
            self.movement = [0, -1]
        if Global.window.KEY_S.clicked:
            self.movement = [0, 1]
        if Global.window.KEY_A.clicked:
            self.movement = [-1, 0]
        if Global.window.KEY_D.clicked:
            self.movement = [1, 0]

        if not Global.window.KEY_E.clicked:
            self.k_e_clicked = False
        if Global.window.KEY_E.clicked:
            if not self.k_e_clicked:
                self.k_e_clicked = True
                if self.energy > 0:
                    x_dir = self.movement[0]
                    y_dir = self.movement[1]
                    while x_dir == 0 and y_dir == 0:
                        x_dir = random.randint(-1, 1)
                        y_dir = random.randint(-1, 1)
                    self.energy -= 0.5
                    Screen_Message("-0.5 Energy", 70, fg="yellow")
                    for i in range(2):
                        Projectile(self.world, self.x + x_dir * (i+2), self.y + y_dir * (i+2), x_dir, y_dir)
                        if y_dir == 1 or y_dir == -1:
                            Projectile(self.world, self.x + (x_dir + 1) * (i + 1), self.y + (y_dir) * (i + 1), x_dir, y_dir)
                            Projectile(self.world, self.x + (x_dir - 1) * (i + 1), self.y + (y_dir) * (i + 1), x_dir, y_dir)
                        if x_dir == 1 or x_dir == -1:
                            Projectile(self.world, self.x + (x_dir) * (i + 1), self.y + (y_dir + 1) * (i + 1), x_dir,y_dir)
                            Projectile(self.world, self.x + (x_dir) * (i + 1), self.y + (y_dir - 1) * (i + 1), x_dir,y_dir)

                else:
                    Screen_Message("You need Energy to fire", 100)




    def move(self):
        try:
            before_block = self.world.array[self.x + self.movement[0]][self.y + self.movement[1]]
            if before_block != 0 and before_block != self:
                Food = ["Food", "Snake", "AI_Snake"]
                if before_block.name in Food:
                    before_block.kill(self.get_info())
                    self.move_to(self.x + self.movement[0], self.y + self.movement[1])

                    Screen_Message("+1 Energy", 70, fg="yellow")
                    if before_block.name == "AI_Snake":
                        Screen_Message("Enemy eaten", 100, bg="green")
                        Global.window.save.score += 100
                        self.energy += 10
                        Screen_Message("+10 Energy", 100, fg="yellow", bg="orange")
                    else:
                        self.energy += 1
                        Global.window.save.score += 1
            else:
                self.move_to(self.x + self.movement[0], self.y + self.movement[1])

        except:
            pass
