import os
from pygame import *


class Enemy(pygame.sprite.Sprite):
    """generic enemy spawned at the start of each level"""

    DIRECTIONS = ["left", "right", "up", "down"]

    def __init__(self, starting_health:int, speed_multiplier:float, sprite_file:str):
        self.starting_health = starting_health
        self.speed_multiplier = speed_multiplier
        self.sprite_path = os.path.join(os.path.join("graphics", "characters"), sprite_file)
        self.x_position = 0
        self.y_position = 0
        self.cold = False
        self.paralyzed = False
        self.poisoned = False

    def move(self):
        pass

    def be_hurt(self):
        pass

    def die(self):
        pass


class LaserButterfly(Enemy):
    """final boss"""

    def __init__(self):
        Enemy.__init__(self, 40, 2.5, "")

    def shoot_laser(self):
        pass

    def summon_minions(self):
        pass


