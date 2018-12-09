from invaders.sprites.enemy_missile import EnemyMissile
from invaders.resources.resources import Resources
from invaders.sprites.invaders import Invaders
from invaders.sprites.player import Player
from invaders.sprites.missile import Missile
from invaders.sprites.barrier import Barrier
from invaders.sprites.barrier_damage_tile import BarrierDamageTile


class SpriteManager(object):
    def __init__(self, resources):
        self.resources = resources
        pass

    def create_enemy_missile(self, layer_width, layer_height):
        missile_image = self.resources.missile
        missile = EnemyMissile(layer_width, layer_height, missile_image)
        return missile

    def create_invaders(self, layer):
        animated_invader = self.resources.animated_invader
        invaders = Invaders(layer, animated_invader)
        return invaders

    def create_player(self, layer_width, layer_height):
        player_image = self.resources.player
        player = Player( (layer_width, layer_height), player_image )
        return player

    def create_player_missile(self, layer_width, layer_height):
        missile_image = self.resources.missile
        missile = Missile(layer_width, layer_height, missile_image)
        return missile

    def create_barriers(self, layer):
        starting_position = layer.width / 8.0
        distance_from_bottom = 80.0
        spacing = layer.width / 4.0
        barrier_image = self.resources.barrier
        barrier1 = Barrier(starting_position, distance_from_bottom, barrier_image)
        layer.add(barrier1)
        barrier2 = Barrier(starting_position + (spacing), distance_from_bottom, barrier_image)
        layer.add(barrier2)
        barrier3 = Barrier(starting_position + (2.0*spacing), distance_from_bottom, barrier_image)
        layer.add(barrier3)
        barrier4 = Barrier(starting_position + (3.0*spacing), distance_from_bottom, barrier_image)
        layer.add(barrier4)
        return [ barrier1, barrier2, barrier3, barrier4 ]

    def create_barrier_damage_columns(self, layer, barrier):
        barrier_damage_columns = []
        barrier_damage_column = None
        barrier_damage_image = self.resources.barrier_damage

        start_position_x = barrier.x - 16 - 8
        start_position_y = barrier.y - 16 - 8
        current_position_x = start_position_x
        current_position_y = start_position_y
        for column in range(4):
            barrier_damage_column = BarrierDamageColumn()
            current_position_x = start_position_x + (16 * column)
            current_position_y = start_position_y
            for tile in range(4):
                current_position_y = start_position_y + (16 * tile)
                barrier_damage_tile = BarrierDamageTile(current_position_x, current_position_y, barrier_damage_image)
                layer.add(barrier_damage_tile)
                barrier_damage_column.add_tile(barrier_damage_tile)

            barrier_damage_columns.append(barrier_damage_column)
            barrier_damage_column = None

        return barrier_damage_columns


# TODO: not sure where to put BarrierDamageColumn class
class BarrierDamageColumn(object):
    def __init__(self):
        self.barrier_damage_tiles = []

    def add_tile(self, barrier_damage_tile):
        self.barrier_damage_tiles.append(barrier_damage_tile)
