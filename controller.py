from pyglet.window import key as Key
from pyglet.window import Window
from pyglet.math import Vec2
from entity import Entity

class Controller:
    def __init__(self, window: Window, entity: Entity):
        self.window = window
        self.entity = entity
        self.move_dir = Vec2()
        self.last_dir = 0

    def set_anim(self, name):
        _anims = self.entity.anims
        if name in _anims:
            self.entity.get_sprite().image = _anims[name]
        else:
            print("(Controller::set_anim): There isn`t such animation")

    def key_press(self, key):
        ...

    def key_release(self, key):
        ...

    def controll(self, dt):
        ...


class PlatformerController(Controller):
    def __init__(self, window, entity, speed=400, jump_height=100):
        super().__init__(window, entity)
        self.speed = speed
        self.jump_height = jump_height
        self.jumped = False
        self.gravity = 10
        self.move_right = False
        self.move_left = False
        self.relative_y = 0

        self.sprite = self.entity.get_sprite()

    def key_press(self, key):
        super().key_press(key)
        
        if key == Key.RIGHT:
            self.set_anim('run_right')
            self.move_dir.x = 1
            self.last_dir = 1
        elif key == Key.LEFT:
            self.set_anim('run_left')
            self.move_dir.x = -1
            self.last_dir = -1


    def key_release(self, key):
        if key == Key.RIGHT:
            self.set_anim('idle_right')
            self.move_dir.x = 0
        elif key == Key.LEFT:
            self.set_anim('idle_left')
            self.move_dir.x = 0

    def jumping(self):
        ...

    def controll(self, dt):
        super().controll(dt)

        self.jumping()

        self.entity.grounded = self.sprite.y <= 150

        self.sprite.x += self.move_dir.x * self.speed * dt
        

class AIPlatformerController(PlatformerController):
    ...