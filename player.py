from pyglet.image import *
from pyglet.resource import image as Image
from pyglet.shapes import *
from pyglet.text import *
from pyglet import font
from pyglet.sprite import Sprite
from pyglet.window import Window
from pyglet.graphics import Batch
from pyglet.window import key as Key
from pyglet.math import *

from controller import PlatformerController
from anim import Anim
from entity import Entity
from controller import *
from background import Background
from player import *
from particles import *
from camera import Camera

class Item:
    ...

class Inventory:
    def __init__(self, window: Window):
        self.last_selected = -1
        self.selected = 0
        self.max_items = 3
        self.batch = Batch()
        self.cells = []
        self.items = []

        self.img_sel = Image('cell_selected.png')
        self.img_sel.anchor_x = self.img_sel.width / 2
        self.img_sel.anchor_y = self.img_sel.height / 2

        self.img = Image('cell.png')
        self.img.anchor_x = self.img.width / 2
        self.img.anchor_y = self.img.height / 2

        cells_padding = 10
        scale = 3.5
        abs_width = self.img.width * scale + cells_padding
        x_offset = (abs_width * self.max_items - cells_padding)//2
        for i in range(self.max_items):
            spr = Sprite(self.img, window.width // 2 - x_offset + abs_width * i, 100, batch=self.batch)
            spr.scale = scale
            self.cells.append(spr)
        

    def push_item(self, item):
        ...

    def select_item(self, index):
        self.cells[self.last_selected].image = self.img
        self.selected = index
        self.cells[index].image = self.img_sel
        self.last_selected = index

    def draw(self):
        self.batch.draw()
        

class PlayerController(PlatformerController):
    def __init__(self, window, player, speed, jump_h):
        super().__init__(window, player, speed, jump_h)

    def key_press(self, key):
        super().key_press(key)


class Player:
    def __init__(self, window):
        self.window: Window = window
        self.camera = Camera(0, 0)

        anim_speed = 0.08
        player_idle_anim = Anim('entities/knight/idle.png', rows=1, columns=10, duration=anim_speed).center_every_frame()
        player_run_anim = Anim('entities/knight/run.png', rows=1, columns=8, duration=anim_speed).center_every_frame()
        player_jump_anim = Anim('entities/knight/jump.png', rows=1, columns=3, duration=anim_speed).center_every_frame()
        player_anims = {
            'idle_left': player_idle_anim.get_flipped_x(), 
            'idle_right': player_idle_anim,
            'run_left': player_run_anim.get_flipped_x(), 
            'run_right': player_run_anim,
            'jump_left': player_jump_anim.get_flipped_x(), 
            'jump_right': player_jump_anim
        }
        self.entity = Entity(anims=player_anims)
        self.entity.get_sprite().scale = 3
        self.entity.get_sprite().position = (window.width//2, 280, 0)

        self.controller = PlayerController(window, self.entity, 700, 200)
        self.inventory = Inventory(window)

        self.particles = ParticleSystem(100, 100)

    def get_pos(self):
        v = self.entity.get_sprite()
        return (v.x, v.y)

    def draw(self):
        self.entity.draw()
        self.inventory.draw()
        self.particles.draw()


    def update(self, dt):
        self.controller.controll(dt)
        self.particles.update(dt)
        self.camera.update(dt)
        
        v = self.window.view
        if self.controller.move_dir.x != 0 and self.entity.get_sprite().x >= self.window.width/2:
            self.window.view = v.from_translation(Vec3(-self.entity.get_sprite().x + self.window.width/2 + dt, 0, 0))


    def key_press(self, key, mods):
        self.controller.key_press(key)
        
        if key == Key._1:
            self.inventory.select_item(0)
        elif key == Key._2:
            self.inventory.select_item(1)
        elif key == Key._3:
            self.inventory.select_item(2)

    def key_release(self, key, mods):
        self.controller.key_release(key)