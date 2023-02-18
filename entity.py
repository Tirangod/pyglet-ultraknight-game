from pyglet.image import *
from pyglet.sprite import *
from pyglet.shapes import *
from pyglet.gl import *

from typing import List, Dict

from anim import Anim

"""
General class for characters like player, enemies, npc and other mobs
"""
class Entity:
    def __init__(self, anims: Dict[str, Anim]):
        self.anims = {name: anim.get_anim() for name, anim in anims.items()}
        
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        
        self.sprite = Sprite(list(self.anims.values())[0])
        self.grounded = False

    def draw(self):
        self.sprite.draw()

    def get_sprite(self):
        return self.sprite

    