import cocos
from cocos.actions import *
import cocos.collision_model as cm
import cocos.euclid as eu


class EnemyMissile(cocos.sprite.Sprite):
    def __init__(self, layer_width, layer_height, resources):
        super(EnemyMissile, self).__init__(resources.missile)
        self.speed = -200
        self.velocity = 0, 0
        self.do(BoundedMove(layer_width, layer_height+self.height))
        self.cshape = None
        
    def set_cshape(self):
        self.cshape = cm.CircleShape(eu.Vector2(self.x, self.y), 15)

    def fire(self, start_position):
        self.x = start_position[0]
        self.y = start_position[1]
        self.cshape = cm.CircleShape(eu.Vector2(self.x, self.y), 5)
        self.velocity = 0, self.speed
