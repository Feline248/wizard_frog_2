import pygame
import os

class Wizard(pygame.sprite.Sprite):
    
    def __init__(self):
        self.set_sprites()

    def set_sprites(self):
        """Defines file paths to images"""
        self.base_path = os.path.join("graphics", "characters")
        self.sitting_right = os.path.join(self.base_path, "frog_sitting_right.png")
        self.sitting_left = os.path.join(self.base_path, "frog_sitting_left.png")
        self.hopping_up_right = os.path.join(self.base_path, "frog_hopping_down_right.png")
        self.hopping_up_left = os.path.join(self.base_path, "frog_hopping_down_left.png")
        self.hopping_down_right = os.path.join(self.base_path, "frog_hopping_down_right.png")
        self.hopping_down_left = os.path.join(self.base_path, "frog_hopping_down_left.png")
        self.death = os.path.join(self.base_path, "frog_dead.png")
