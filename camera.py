ACCELERATION = 20.0
MAX_SPEED = 100.0
FRICTION = 0.9

# Define the camera class
class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def update(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt
        self.dx *= FRICTION
        self.dy *= FRICTION

    def move_left(self):
        self.dx -= ACCELERATION

    def move_right(self):
        self.dx += ACCELERATION

    def move_up(self):
        self.dy += ACCELERATION

    def move_down(self):
        self.dy -= ACCELERATION

    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y

    def update_target(self, x, y):
        self.target_x += x
        self.target_y += y

    def update_position(self):
        self.x = self.target_x
        self.y = self.target_y