from invaders.sprites.enemy_missile import EnemyMissile
from invaders.resources.resources import Resources
from invaders.sprites.invaders import Invaders
from invaders.sprites.player import Player
from invaders.sprites.missile import Missile
from invaders.sprites.barrier import Barrier


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


