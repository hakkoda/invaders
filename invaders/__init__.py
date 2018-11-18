from cocos.director import director
from invaders.scenes.main import Main_Scene

def run():
    window = director.init(width=550, height=500, caption="Invaders!")
    window.set_location(100, 100)
    director.run(Main_Scene())
