import cocos
from cocos.actions import *
import cocos.collision_model as cm


class Barrier(cocos.sprite.Sprite):
    def __init__(self, x, y, barrier_image):
        super(Barrier, self).__init__(barrier_image)
        self.cshape = None
        self.x = x
        self.y = y
        self.set_cshape()
        
    def set_cshape(self):
        self.cshape = cm.AARectShape((self.x, self.y), 32, 32)
