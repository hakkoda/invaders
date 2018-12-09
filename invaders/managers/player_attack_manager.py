import cocos.collision_model as cm


class PlayerAttackManager(object):
    def __init__(self, sprite_manager):
        self.sprite_manager = sprite_manager

    # called by the scene
    def fire_player_missile(self, layer, player):
        if not self.is_missile_live(layer):
            missile = self.sprite_manager.create_player_missile(layer.width, layer.height)
            layer.add(missile, name="missile")
            missile.fire((player.x, player.y))

    # called by the invaders
    def update_attack(self, layer, invader):
        if self.is_missile_live(layer):
            missile = layer.get("missile")
            missile.set_cshape()
            if missile.y > layer.height:
                layer.remove("missile")
            elif invader.visible:
                invader.set_cshape()
                if missile.cshape.overlaps(invader.cshape):
                    invader.visible = False
                    missile.visible = False
                    layer.remove("missile")

    # called by the barriers
    def update_barrier_damage(self, layer, barrier_tile):
        if self.is_missile_live(layer):
            missile = layer.get("missile")
            missile.set_cshape()
            if missile.y > layer.height:
                layer.remove("missile")
            elif barrier_tile.visible == False:
                if cm.aa_rect_overlaps_circle(barrier_tile.cshape, missile.cshape):
                    barrier_tile.visible = True
                    missile.visible = False
                    layer.remove("missile")

    def is_missile_live(self, layer):
        return "missile" in layer.children_names
