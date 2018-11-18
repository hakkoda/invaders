import cocos
from cocos.actions import *


class Player(cocos.sprite.Sprite):
    def __init__(self, layer_dimensions, resources):
        super(Player, self).__init__(resources.player)
        self.layer_width = layer_dimensions[0]
        self.layer_height = layer_dimensions[1]

        # Set starting position to be at the bottom of the screen in the middle
        self.x = self.layer_width / 2 
        self.y = 0 + self.height / 2 

        self.speed = 150
        self.velocity = 0, 0

        # Move the sprite until an edge is hit
        self.do(BoundedMove(self.layer_width, self.layer_height))

    def move(self, value):
        if value == -1.0 or value == 1.0:
            self.velocity = value * self.speed, 0
        else:
            self.velocity = 0,0
