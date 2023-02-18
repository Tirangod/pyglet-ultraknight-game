import pyglet
import math
import random

class Particle:
    def __init__(self, path, x, y, speed, angle, lifetime):
        self.sprite = pyglet.sprite.Sprite(pyglet.resource.image(path))
        self.sprite.x = x
        self.sprite.y = y
        self.dx = speed * math.cos(math.radians(angle))
        self.dy = speed * math.sin(math.radians(angle))
        self.lifetime = lifetime
    
    def update(self, dt):
        self.sprite.x += self.dx * dt
        self.sprite.y += self.dy * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.sprite.delete()

# Define the particle system class
class ParticleSystem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.batch = pyglet.graphics.Batch()
        
    def emit(self, count, speed, lifetime, path):
        for i in range(count):
            particle = Particle(path, self.x, self.y, speed, random.randint(0, 360), lifetime)
            self.particles.append(particle)
            particle.sprite.batch = self.batch
        
    def update(self, dt):
        for particle in self.particles:
            particle.update(dt)
        self.particles = [p for p in self.particles if p.lifetime > 0]
    
    def draw(self):
        self.batch.draw()