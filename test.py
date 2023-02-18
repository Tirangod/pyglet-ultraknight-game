import pyglet
import pytweening

window = pyglet.window.Window()

# Create a sprite with an initial position
sprite = pyglet.sprite.Sprite(pyglet.resource.image('res/sprites/ui/cell.png'))
sprite.position = (0, 0, 0)

# Define the target position
target_position = (200, 200)

# Define the duration of the transition in seconds
duration = 15.0

# Define the easing function
easing_func = pytweening.easeInOutQuad

# Define the time elapsed since the start of the transition
elapsed_time = 0.0

# Define the update function
def update(dt):
    global elapsed_time

    # Update the elapsed time
    elapsed_time += dt

    # Calculate the interpolation factor
    t = min(1.0, elapsed_time / duration)

    # Calculate the new position using the easing function
    x = easing_func(t) * target_position[0] + (1 - easing_func(t)) * sprite.position[0]
    y = easing_func(t) * target_position[1] + (1 - easing_func(t)) * sprite.position[1]

    # Set the new position
    sprite.position = (x, y, 0)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

# Schedule the update function to be called every frame
pyglet.clock.schedule(update)

# Start the Pyglet event loop
pyglet.app.run()