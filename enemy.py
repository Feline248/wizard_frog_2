#Rachel Dahl
#Enemy and LaserButterfly classes
#control enemies fought in-game

import os
import pygame
from random import choice, randint
from constants import *


class Enemy(pygame.sprite.Sprite):
    """generic enemy spawned at the start of each level"""

    DIRECTIONS = ["left", "right", "up", "down"]
    BASE_DISTANCE = 35

    def __init__(self, starting_health:int, speed_multiplier:float, sprite_file:str):
        #base stats
        self.health = starting_health
        self.speed_multiplier = speed_multiplier
        self.size = ENEMY_SIZE
        #graphics
        self.sprite_path = os.path.join(os.path.join("graphics", "characters"), sprite_file)
        self.sprite = pygame.image.load(self.sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (self.size, self.size))
        #location
        self.x_pos = randint(0, SCREEN_DIMENSIONS[0] - self.size)
        self.y_pos = randint(0, SCREEN_DIMENSIONS[1] - self.size)
        #status effects
        self.cold = False
        self.paralyzed = False
        self.poisoned = False

    def move(self):
        """move in a randomly selected direction as long as 
        coordinates don't exceed screen dimensions"""

        self.move_direction = choice(Enemy.DIRECTIONS)
        self.distance = Enemy.BASE_DISTANCE * self.speed_multiplier

        if self.move_direction == "up" and self.y_pos > 0:
            self.y_pos -= self.distance

        #since coordinates are by top left corner, the size of the sprite is subtracted so nothing can go offscreen
        if self.move_direction == "down" and self.x_pos < SCREEN_DIMENSIONS[0] - self.size: 
            self.y_pos += self.distance

        if self.move_direction == "left" and self.x_pos > 0:
            self.x_pos -= self.distance

        if self.move_direction == "right" and self.y_pos < SCREEN_DIMENSIONS[1] - self.size:
            self.x_pos += self.distance


    def die(self):
        pass


class LaserButterfly(Enemy):
    """final boss"""

    def __init__(self):
        Enemy.__init__(self, 40, 2.5, "laser_butterfly.png")

    def shoot_laser(self):
        pass

    def summon_minions(self):
        pass


