import random


class EnemyAttackManager(object):
    def __init__(self, sprite_manager):
        self.sprite_manager = sprite_manager
        self.time_interval = 0

    # Called by the scene 
    def update_attack(self, layer, player, invaders, dt):
        self.fire_enemy_missile(layer, player, invaders, dt)

    def fire_enemy_missile(self, layer, player, invaders, dt):
        rand = random.randint(0, 3)
        self.time_interval += (dt * 10.0)
        fire = False
        if self.time_interval > rand:
            fire = True
            self.time_interval = 0
        for missile_num in range(rand):
            missile_id = f"enemy_missile{missile_num}"
            if not self.is_enemy_missile_live(layer, missile_id):
                if fire:
                    missile = self.sprite_manager.create_enemy_missile(layer.width, layer.height)
                    layer.add(missile, name=missile_id)
                    row, column = self.get_attacking_invader(player, invaders)
                    if row != -1 and column != -1:
                        attacking_invader = invaders.sprites[row][column]
                        missile.fire((attacking_invader.x, attacking_invader.y))
            else:
                self.clean_up(layer, missile_id)

    def clean_up(self, layer, missile_id):
        missile = None
        if self.is_enemy_missile_live(layer, missile_id):
            missile = layer.get(missile_id)
            missile.set_cshape()
            if missile.y < missile.height:
                layer.remove(missile_id)
                missile = None
        return missile

    def is_enemy_missile_live(self, layer, missile_id):
        return missile_id in layer.children_names

    def get_attacking_invader(self, player, invaders):
        result = (-1, -1)
        range_input = self.get_bombing_range(player)
        invaders_in_range = self.get_invaders_in_range(range_input, invaders)
        if len(invaders_in_range) > 0:
            rand = random.randint(0, len(invaders_in_range)-1)
            result = invaders_in_range[rand]
        return result

    def get_bombing_range(self, player):
        x_max = player.x + 150
        x_min = player.x - 150
        return (x_min, x_max)

    def get_invaders_in_range(self, range_input, invaders):
        result = []
        for column in range(invaders.columns):
            for row in range(invaders.rows-1, -1, -1):
                sprite = invaders.sprites[row][column]
                if sprite.visible == True:
                    if sprite.x > range_input[0] and sprite.x < range_input[1]:
                        result.append( (row, column) )
                        break
        return result
