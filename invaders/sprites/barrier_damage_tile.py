import cocos
from cocos.actions import *
import cocos.collision_model as cm


class BarrierDamageTile(cocos.sprite.Sprite):
    def __init__(self, x, y, barrier_damage_image):
        super(BarrierDamageTile, self).__init__(barrier_damage_image)
        self.cshape = None
        self.x = x
        self.y = y
        self.visible = False   
        self.set_cshape()
        self.damage_states = DamageStates()
        self.damage_state = self.damage_states.NO_DAMAGE

        self.opacity = 255
        #self.opacity = 128
        
    def set_cshape(self):
        self.cshape = cm.AARectShape((self.x, self.y), 8, 8)

    def get_damage_state(self):
        return self.damage_state

    def update_damage_state(self, source):
        if source == "PLAYER":
            self.damage_state = self.damage_states.DESTROYED
            self.visible = True
        if source == "INVADER":
            if self.damage_state == self.damage_states.ENEMY_DAMAGE:
                self.damage_state = self.damage_states.DESTROYED
                self.visible = True
            else:
                self.damage_state = self.damage_states.ENEMY_DAMAGE

class DamageStates(object):
    def __init__(self):
        self.DESTROYED = "DESTROYED"
        self.ENEMY_DAMAGE = "ENEMY_DAMAGE"
        self.NO_DAMAGE = "NO_DAMAGE"
