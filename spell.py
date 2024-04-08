from abc import ABC
from enemy import Enemy, LaserButterfly
import pygame
import os

class Spell(ABC, pygame.sprite.Sprite):

    def __init__(self, damage:int, sprite_file:str):
        self.damage = damage
        self.sprite_path = os.path.join(os.path.join("graphics", "spells"), sprite_file)
        self.sprite = pygame.image.load(self.sprite_path)

    def do_damage(self, other:Enemy):
        """damages enemy and makes spell vanish upon contact"""
        other.health -= self.damage
        #TODO add way for spell to disappear



class Bubbles(Spell):
    
    def __init__(self):
        Spell.__init__(self, 3, "bubbles.png")
