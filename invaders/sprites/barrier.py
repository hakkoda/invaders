import cocos
from cocos.actions import *
import cocos.collision_model as cm
import cocos.euclid as eu


class Barrier(cocos.sprite.Sprite):
    def __init__(self, x, y, barrier_image):
        super(Barrier, self).__init__(barrier_image)
        self.cshape = None
        self.x = x
        self.y = y
        
    def set_cshape(self):
        self.cshape = cm.CircleShape(eu.Vector2(self.x, self.y), 10)
