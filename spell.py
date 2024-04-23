#Rachel Dahl
#Spell class, controls projectiles 
#launched by player

from abc import ABC
from enemy import Enemy, LaserButterfly
from frog import Frog
from constants import *
import pygame
import os

class Spell(ABC, pygame.sprite.Sprite):

    def __init__(self, damage:int, base_cost:int, sprite_file:str, target:Enemy|Frog, caster:Frog|Enemy):
        self.damage = damage
        self.sprite_path = os.path.join(os.path.join("graphics", "spells"), sprite_file)
        self.sprite = pygame.image.load(self.sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (75, 75))
        self.cost = base_cost           #for now these variables are equal, but base cost will be multiplied by spell level eventually
        self.x_pos = caster.x_pos
        self.y_pos = caster.y_pos
        self.set_coordinates(target)


    def do_damage(self, other:Enemy):
        """damages enemy and makes spell vanish upon contact"""
        other.health -= self.damage
        self.sprite = None


    def set_coordinates(self, target:Enemy):
        """set coordinates to be used for spell movement"""
        self.target_x = target.x_pos
        self.target_y = target.y_pos


    def move_spell(self, delta_time):
        """move spell towards enemy"""
        if self.x_pos < self.target_x:
            self.x_pos += SPEED_MULTIPLIER * delta_time
        if self.x_pos > self.target_x:
          self.x_pos -= SPEED_MULTIPLIER * delta_time
        if self.y_pos < self.target_y:
          self.y_pos += SPEED_MULTIPLIER * delta_time
        if self.y_pos > self.target_y:
            self.y_pos -= SPEED_MULTIPLIER * delta_time
        


class Bubbles(Spell):

    COST = 2
    
    def __init__(self, target:Enemy, caster:Frog):
        Spell.__init__(self, 1, Bubbles.COST, "bubbles.png", target, caster)

