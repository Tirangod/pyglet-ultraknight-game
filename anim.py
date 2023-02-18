from pyglet.image import *
from pyglet.resource import image as Image

class Anim:
    def __init__(
            self, 
            path: str, 
            rows=1, 
            columns=1, 
            duration=1, 
            loop=False, 
            flip_x=False, 
            flip_y=False, 
            align_center_w=False, 
            align_center_h=False
        ):
        self.path = path
        self.rows = rows
        self.columns = columns
        self.duration = duration
        self.loop = loop
        self.flip_x = flip_x
        self.flip_y = flip_y
        self.align_center_w = align_center_w
        self.align_center_h = align_center_h
        self.anim = None

    def compose(self) -> Animation:
        image = Image(self.path, self.flip_x, self.flip_y)
        image_grid = ImageGrid(image, self.rows, self.columns)
        frames = []
        
        # Process every image from spritesheet
        for img in image_grid:
            # Align by width or/and heigth every image
            if self.align_center_w:
                img.anchor_x = img.width // 2
            if self.align_center_w:
                img.anchor_y = img.height // 2

            # Make frame from image
            frame = AnimationFrame(img, self.duration)
            frames.append(frame)

        self.anim = Animation(frames)

    def get_flipped_x(self):
        new = Anim(
            self.path, 
            self.rows, 
            self.columns, 
            self.duration, 
            self.loop, 
            True, 
            self.flip_y, 
            self.align_center_w, 
            self.align_center_h
        )
        return new

    def get_flipped_y(self):
        new = Anim(
            self.path, 
            self.rows, 
            self.columns, 
            self.duration, 
            self.loop, 
            self.flip_x, 
            True, 
            self.align_center_w, 
            self.align_center_h
        )
        return new

    def center_every_frame(self):
        self.align_center_w = True
        self.align_center_h = True
        return self

    def get_anim(self):
        self.compose()
        return self.anim