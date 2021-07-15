import pickle
import time
from tkinter import *
import tkinter.ttk as ttk
from SAVE import *
from ttkbootstrap import Style, ttk
from World import *
import sys
from imageKey import KeyBind
from GLOBAL import *
from Interface.Screen_Message import *
from Interface.PauseMenu import *
from Interface.PageMenu import *
from Interface.NewGameMenu import *
from pygame import time as pgtime
#import pygame
from PIL import Image

class Window(Tk):
    def __init__(self):
        super().__init__()
        # window config
        style = Style()
        style.theme_use('superhero')
        self.screenW = 1121
        self.screenH = 763
        self.geometry(f"{self.screenW}x{self.screenH}")
        self.resizable(False, False)
        self.title(f"Weaponized Block - {Global.version}")

        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.clock = pgtime.Clock()
        # keybinds
        self.bind("<Escape>", self.pause_invoke)
        self.bind("<T>", self.invoke_debug)
        self.bind("<R>", self.invoke_render)
        self.bind("<Alt-g>", self.invoke_godmode)
        self.KEY_W = KeyBind("w", self, self.loop_tick)
        self.KEY_A = KeyBind("a", self, self.loop_tick)
        self.KEY_S = KeyBind("s", self, self.loop_tick)
        self.KEY_D = KeyBind("d", self, self.loop_tick)

        self.KEY_E = KeyBind("Button-1", self, self.loop_tick, release="ButtonRelease-1")

        # frames
        self.game_frame = Frame(self); self.game_frame.pack(expand=True, fill=BOTH)
        self.top_bar = Frame(self.game_frame);self.top_bar.pack(fill=X)
        self.game_canvas = Canvas(self.game_frame, highlightthickness=0); self.game_canvas.pack(expand=True, fill=BOTH)
        self.pause_frame = PauseMenu(self, self.game_canvas)
        self.bottom_bar = Frame(self.game_frame);self.bottom_bar.pack(fill=BOTH, side=BOTTOM)

        # UI
        self.energy_count_label = Label(self.top_bar, text="energy_count", font="System 17", width=10, fg="yellow"); self.energy_count_label.pack(side=LEFT)
        self.snake_count_label = Label(self.top_bar, text="snake_count", font="System 17", width=9, fg="green"); self.snake_count_label.pack(side=LEFT)
        self.score_label = Label(self.top_bar, text="score", font="System 17", width=9, fg="orange"); self.score_label.pack(side=LEFT)
        self.fps_label = Label(self.top_bar, text="FPS", font="System 17", width=9, fg="white"); self.fps_label.pack(side=RIGHT)

        self.advert = Label(self.bottom_bar, text="Developed by Konstantin Ehmann; KSV", fg="grey"); self.advert.pack(side=LEFT)
        self.help_button = Button(self.bottom_bar, text="Instructions", bg="#1F3040", height=1, command=lambda: self.open_menu(tab="Instructions")); self.help_button.pack(side=RIGHT)


        Global.window = self

        self.running = True
        self.win_tick = 0
        self.tick = 0


        # save game defaults
        self.save = SAVE()
        self.save.world = World(empty=True)

        # loading save game
        try:
            self.load_game()
            self.save.paused = False
            if self.save.in_new_game_menu:
                self.new_game()
            else:
                self.pause_invoke("")
        except Exception as e:
            #messagebox.showwarning("Save Loading Error", f"Savefile not found or corrupted. Continue to start a fresh save. \nERROR: {e}")
            self.new_game()

        self.game_canvas.config(bg=Global.data["canvas_color"])

        #self.screen = pygame.display.set_mode((self.screenW, self.screenH))

        # mainloop
        while self.running:
            self.loop_tick()

    def loop_tick(self):
        if self.save.render_world:
            self.clock.tick(Global.data["fps"])
        else:
            self.clock.tick()
        self.win_tick += 1

        if self.win_tick % 3 == 0:
            self.fps_label.config(text=f"FPS: {round(self.clock.get_fps(), 2)}")
            self.score_label.config(text=f"Score: {self.save.score}")

        self.update_window()
        if not self.save.paused:
            self.update_tick()


    def update_window(self):
        self.update()
        self.render_world_to_canvas()




    def update_tick(self):
        self.tick += 1

        # update blocks
        for i in self.save.world.instance_array:
            i.update(self.tick)
        self.save.world.update(self.tick)

    def render_world_to_canvas(self):
        self.game_canvas.delete(ALL)
        """
        self.game_canvas.delete(ALL)
        pygame.display.flip()
        self.screen.fill(pygame.Color(Global.data["canvas_color"]))

        # pygame draw blocks
        for i in self.save.world.instance_array:
            pygame.draw.rect(self.screen, pygame.Color(i.color), (i.x * self.save.world.pixel_size + self.save.xoff, i.y * self.save.world.pixel_size + self.save.yoff, self.save.world.pixel_size, self.save.world.pixel_size))

        """
        if self.save.render_world:
            # draw border
            self.game_canvas.create_rectangle(self.save.xoff, self.save.yoff,
                                              self.save.world.pixel_size * self.save.world.arrayx + self.save.xoff,
                                              self.save.world.pixel_size * self.save.world.arrayy + self.save.yoff)
             # draw blocks
            for i in self.save.world.instance_array:
                self.game_canvas.create_rectangle(i.x * self.save.world.pixel_size + self.save.xoff, i.y * self.save.world.pixel_size + self.save.yoff, (i.x * self.save.world.pixel_size) + self.save.world.pixel_size + self.save.xoff, (i.y * self.save.world.pixel_size) + self.save.world.pixel_size + self.save.yoff, fill=i.color, outline="")



            if self.save.debug:
                for j in self.save.world.array:
                    for i in j:
                        if i != 0:
                            if i not in self.save.world.instance_array:
                                self.game_canvas.create_rectangle(
                                    i.x * self.save.world.pixel_size + self.save.xoff + self.save.world.pixel_size / 2,
                                    i.y * self.save.world.pixel_size + self.save.yoff + self.save.world.pixel_size / 2,
                                    (
                                            i.x * self.save.world.pixel_size) + self.save.world.pixel_size + self.save.xoff + self.save.world.pixel_size + 10,
                                    (
                                            i.y * self.save.world.pixel_size) + self.save.world.pixel_size + self.save.yoff + self.save.world.pixel_size + 10,
                                    fill=i.color, outline="", stipple="error")

                            self.game_canvas.create_rectangle(
                                i.x * self.save.world.pixel_size + self.save.xoff + self.save.world.pixel_size / 2,
                                i.y * self.save.world.pixel_size + self.save.yoff + self.save.world.pixel_size / 2, (
                                        i.x * self.save.world.pixel_size) + self.save.world.pixel_size + self.save.xoff + self.save.world.pixel_size / 2,
                                (
                                        i.y * self.save.world.pixel_size) + self.save.world.pixel_size + self.save.yoff + self.save.world.pixel_size / 2,
                                fill=i.color, outline="", stipple="gray50")

        # render messages
        y_off = 0
        for i in messages:
            y_off += 42
            message_width = 10
            for j in i.text:
                message_width += 15
            self.game_canvas.create_rectangle(self.screenW / 2 - message_width/2, y_off - 18, self.screenW / 2 + message_width/2, y_off + 18, fill=i.bg, stipple='gray12')
            self.game_canvas.create_text(self.screenW / 2, y_off, text=i.text, font="System 17", fill=i.fg)
            i.update()

    def on_exit(self):
        self.running = False
        self.save_game()

    def pause_invoke(self, event):

        if self.save.paused:
            self.save.paused = False
            self.save.in_new_game_menu = False
            self.pause_frame.hide()
            try:
                self.new_game_menu.destroy()
                del self.new_game_menu
            except:
                pass

            try:
                self.menu.destroy()
                del self.menu
            except:
                pass

        else:
            self.save.paused = True
            self.pause_frame.show()

    def new_game(self):
        self.save.paused = True
        self.new_game_menu = NewGameMenu(self, self.game_canvas)
        self.new_game_menu.show()

    def open_menu(self, tab=None):
        self.save.paused = True
        self.pause_frame.show()
        self.menu = PageMenu(self, self.game_canvas, tab=tab)

    def invoke_debug(self, event=None):
        if self.save.debug:
            Screen_Message("Debug mode deactivated", 100, bg="red")
            self.save.debug = False
        else:
            Screen_Message("Debug mode activated", 100, bg="green")
            self.save.debug = True

    def invoke_render(self, event=None):
        if self.save.render_world:
            Screen_Message("Render_world mode deactivated (toggle with 'r')", 200, bg="red")
            self.save.render_world = False
        else:
            Screen_Message("Render_world mode activated", 100, bg="green")
            self.save.render_world = True

    def invoke_godmode(self, event=None):
        self.save.godmode_used = True
        if self.save.godmode:
            Screen_Message("Godmode mode deactivated", 100, bg="green")
            self.save.godmode = False
        else:
            Screen_Message("Godmode mode activated", 100, bg="red")
            self.save.godmode = True

    def game_over(self):
        self.save.paused = True


    def reset_save(self, empty=False):
        self.save = SAVE()
        self.save.world = World(empty)
        messages.clear()


    def save_game(self):
        self.save.data = Global.data
        f = open("save.pdump", "wb")
        pickle.dump(self.save, f)
        f.close()

    def load_game(self):
        f = open("save.pdump", "rb")
        self.save = pickle.load(f)
        f.close()
        Global.data = self.save.data

