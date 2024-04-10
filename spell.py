from abc import ABC
from enemy import Enemy, LaserButterfly
import pygame
import os

class Spell(ABC, pygame.sprite.Sprite):

    def __init__(self, damage:int, sprite_file:str):
        self.damage = damage
        self.sprite_path = os.path.join(os.path.join("graphics", "spells"), sprite_file)
        self.sprite = pygame.image.load(self.sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (75,75))

    def do_damage(self, other:Enemy):
        """damages enemy and makes spell vanish upon contact"""
        other.health -= self.damage
        self.sprite = None

    def move(self, other:Enemy):
        """move spell towards enemy"""
            if self.spell_x < self.current_enemy_x:
                self.spell_x += Game.SPEED_MULTIPLIER * self.delta_time
            if self.spell_x > self.current_enemy_x:
                self.spell_x -= Game.SPEED_MULTIPLIER * self.delta_time
            if self.spell_y < self.current_enemy_y:
                self.spell_y += Game.SPEED_MULTIPLIER * self.delta_time
            if self.spell_y > self.current_enemy_x:
                self.spell_y -= Game.SPEED_MULTIPLIER * self.delta_time



class Bubbles(Spell):
    
    def __init__(self):
        Spell.__init__(self, 3, "bubbles.png")
