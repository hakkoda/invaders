import pyglet


class JoyStick(object):
    def __init__(self, layer):
        joysticks = pyglet.input.get_joysticks()
        if joysticks: 
            self.joystick = joysticks[0]
            self.joystick.on_joyaxis_motion = layer.on_joyaxis_motion
            self.joystick.on_joybutton_press = layer.on_joybutton_press
            self.joystick.open()
