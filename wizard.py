import pygame
import os

class Wizard(pygame.sprite.Sprite):
    MAX_X = 1250
    MIN_X = 0
    GROUND_Y_POS = 650
    
    def __init__(self):
        self.set_sprites()
        self.x_pos = Wizard.MAX_X / 2
        self.y_pos = Wizard.GROUND_Y_POS

    def set_sprites(self):
        """Defines file paths to images"""
        self.base_path = os.path.join("graphics", "characters")
        self.sitting_right = pygame.image.load(os.path.join(self.base_path, "frog_sitting_right.png"))
        self.sitting_left = pygame.image.load(os.path.join(self.base_path, "frog_sitting_left.png"))
        self.hopping_up_right = pygame.image.load(os.path.join(self.base_path, "frog_hopping_down_right.png"))
        self.hopping_up_left = pygame.image.load(os.path.join(self.base_path, "frog_hopping_down_left.png"))
        self.hopping_down_right = pygame.image.load(os.path.join(self.base_path, "frog_hopping_down_right.png"))
        self.hopping_down_left = pygame.image.load(os.path.join(self.base_path, "frog_hopping_down_left.png"))
        self.death = pygame.image.load(os.path.join(self.base_path, "frog_dead.png"))

    def hop_right(self):
        """make frog hop right 1 arbitrary unit tbd"""
        self.x_pos += 1

    def hop_left(self):
        pass

    def hop_up(self):
        pass

    def cast_spell(self):
        pass

