import pyglet


class Resources(object):
    def __init__(self):
        pyglet.resource.path = ["@invaders.resources.img"]
        pyglet.resource.reindex()
        self.animated_invader = self.get_animated_invader()
        self.player = pyglet.resource.image("player_sprite.png")
        self.missile = pyglet.resource.image("missile.png")
        self.barrier = pyglet.resource.image("barrier.png")
        self.barrier_damage = pyglet.resource.image("barrier_damage.png")

    def get_animated_invader(self):
        img = pyglet.resource.image("animated_invaders.png")
        invader_seq = pyglet.image.ImageGrid(img, 1, 2)
        animated_invader = pyglet.image.Animation.from_image_sequence(invader_seq[0:], 0.2, loop=True)
        return animated_invader 
