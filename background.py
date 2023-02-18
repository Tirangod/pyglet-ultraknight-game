from pyglet.graphics import Batch, Group
from pyglet.sprite import Sprite
from pyglet.resource import image as Image

class Background:
    def __init__(self, player):
        self.batch = Batch()

        self.bg = Group(0) 
        self.player_order = Group(1)
        self.fr = Group(2)
        self.layers = [Image('layer' + str(11 - i) + '.png') for i in range(10)]
        self.sprites = []
        
        player.get_sprite().batch = self.batch
        player.get_sprite().group = self.player_order

        img0 = Image('layer0.png')
        img1 = Image('layer1.png')

        for i in range(5):
            
            layer1 = Sprite(img1, batch=self.batch, group=self.fr)
            layer1.scale = 2
            layer1.y = 100
            layer0 = Sprite(img0, batch=self.batch, group=self.fr)
            layer0.scale = 2
            layer0.y = 100

            for img in self.layers:
                spr = Sprite(img, batch=self.batch, group=self.bg)
                spr.scale = 2
                spr.y = 100
                spr.x = i * spr.width
                self.sprites.append(spr)
                
            self.sprites.append(player.get_sprite())
            self.sprites.append(layer0)
            self.sprites.append(layer1)

        decor1 = Sprite(Image('objects/Obj-Statue.png'), batch=self.batch, group=self.bg)
        decor1.x = 100
        decor1.y = 225
        decor1.scale = 6
        decor0 = Sprite(Image('objects/Obj-Hanging-Flag-02.png'), batch=self.batch, group=self.bg)
        decor0.x = 265
        decor0.y = 300
        decor0.scale = 3
        self.sprites.append(decor1)
        self.sprites.append(decor0)
        
        
    def draw(self):
        self.batch.draw()

    def update(self, dt):
        #parallalx
        ...