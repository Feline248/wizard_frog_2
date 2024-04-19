#Rachel Dahl
#Spell class, controls projectiles 
#launched by player

from abc import ABC
from enemy import Enemy, LaserButterfly
from constants import *
import pygame
import os

class Spell(ABC, pygame.sprite.Sprite):

    def __init__(self, damage:int, base_cost:int, sprite_file:str):
        self.damage = damage
        self.sprite_path = os.path.join(os.path.join("graphics", "spells"), sprite_file)
        self.sprite = pygame.image.load(self.sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (75,75))
        self.cost = base_cost           #for now these variables are equal, but base cost will be multiplied by spell level eventually

    def do_damage(self, other:Enemy):
        """damages enemy and makes spell vanish upon contact"""
        other.health -= self.damage
        self.sprite = None

    def set_coordinates(self, target:Enemy):
        """set coordinates to be used for spell movement"""
        self.current_enemy_x = target.x_pos
        self.current_enemy_y = target.y_pos



class Bubbles(Spell):

    COST = 2
    
    def __init__(self):
        Spell.__init__(self, 1, Bubbles.COST, "bubbles.png")

