import cocos
from invaders.resources.resources import Resources
from invaders.input.joystick import JoyStick
from invaders.sprites.missile import Missile
from invaders.sprites.player import Player
from invaders.sprites.invaders import Invaders


class Main_Scene(cocos.scene.Scene):
    def __init__(self):
        super(Main_Scene, self).__init__()
        self.layer = Main_Layer()
        self.add(self.layer)


class Main_Layer(cocos.layer.Layer):
    def __init__(self):
        super(Main_Layer, self).__init__()
        self.width = self.anchor[0] * 2
        self.height = self.anchor[1] * 2
        self.resources = Resources()
        self.invaders = Invaders(self, self.resources)
        self.player = Player( (self.width, self.height), self.resources )
        self.add(self.player)
        self.joystick = JoyStick(self)
        self.schedule(self.loop)

    def loop(self, dt, *args, **kwargs):
        missile = self.get_missile()
        self.invaders.move_sprites(dt, missile)

    def is_missile_live(self):
        return "missile" in self.children_names

    def get_missile(self):
        missile = None
        if self.is_missile_live():
            missile = self.get("missile")
            missile.set_cshape()
            if missile.y > self.height:
                self.remove("missile")
                missile = None
        return missile

    def fire_missile(self):
        if not self.is_missile_live():
            missile = Missile(self.width, self.height, self.resources)
            self.add(missile, name="missile")
            missile.fire((self.player.x, self.player.y))

    def on_joyaxis_motion(self, joystick, axis, value):
        if axis == "x":
            self.player.move(value)

    def on_joybutton_press(self, joystick, button):
        if button == 0 or button == 1:
            self.fire_missile()
