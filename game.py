import pyglet
from pyglet.resource import image as Image
from pyglet.graphics import *
from pyglet.window import *
from pyglet.image import *
from pyglet.sprite import *
from pyglet.shapes import *
from pyglet.math import *
from pyglet.gl import *
from pyglet.window import key as Key

from player import Player
from background import Background


"""Window setup"""
window = Window(1900, 980)
fps = FPSDisplay(window)
#window.set_fullscreen(True)
#window.set_mouse_visible(False)
window.set_caption("UltraKnight")

pyglet.resource.path = [
    'res', 
    'res/fonts', 
    'res/sprites', 
    'res/sprites/ui',
    'res/sprites/objects'
    'res/sprites/entities', 
    'res/sprites/backgrounds',
]
pyglet.resource.reindex()

player = Player(window)
background = Background(player.entity)

def fillColor(r, g, b, a=255):
    glClearColor(r/255, g/255, b/255, a/255)

def lerp(a, b, t):
    return a + (b - a) * t

@window.event
def on_key_press(key, mods):
    player.key_press(key, mods)


@window.event
def on_key_release(key, mods):
    player.key_release(key, mods)

@window.event
def on_draw():
    # Pixel-perfect effect
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    window.clear()
    fillColor(12, 17, 34)

    background.draw()
    player.draw()

    fps.draw()


def update(dt):
    background.update(dt)
    player.update(dt)


pyglet.clock.schedule_interval(update, 1/60.)

pyglet.app.run()