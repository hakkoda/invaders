

class BarrierDamageManager(object):
    def __init__(self):
        self.barrier_damage_column_list = []

    def add_barrier_damage_column(self, barrier_damage_columns):
        self.barrier_damage_column_list.append(barrier_damage_columns)

    def update_damage(self, layer, player_attack_manager, enemy_attack_manager):
        # loop through each barrier_damage_columns and pass a
        # barrier_damage_tile to the player_attack_manager to determine if a
        # collision has occurred.
        for barrier_damage_columns in self.barrier_damage_column_list:
            for barrier_damage_column in barrier_damage_columns:
                for barrier_tile in barrier_damage_column.barrier_damage_tiles:
                    player_attack_manager.update_barrier_damage(layer, barrier_tile)
                    enemy_attack_manager.update_barrier_damage(layer, barrier_tile)
