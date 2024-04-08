import pygame
from enemy import Enemy
import os

class Level():

    def __init__(self, number:int, background_image:str, enemy:Enemy):
        self.number = number
        self.background_path = os.path.join(os.path.join("graphics", "backgrounds"), background_image)
        self.background = pygame.image.load(self.background_path)
        self.enemy = enemy

    def start_level(self):
        """change background and add enemies to the screen"""
        pass

    def end_level(self):
        """hide enemies, open store, and increase level counter"""