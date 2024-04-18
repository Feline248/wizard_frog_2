#Rachel Dahl
#Frog class, responsible for 
# animating the player character



import os
from constants import *

class Frog(pygame.sprite.Sprite):
    MAX_X = 1250
    MIN_X = 0
    GROUND_Y_POS = 600
    SIZE = 125
    MAX_HEALTH = 5
    MAX_MAGIC = 20
    
    def __init__(self):
        self.set_sprites()
        self.x_pos = Frog.MAX_X / 2
        self.y_pos = Frog.GROUND_Y_POS
        self.health = 5
        self.magic = 15

    def set_sprites(self):
        """Defines file paths to images and lists for animations"""

        self.base_path = os.path.join("graphics", "characters")

        self.sitting_right = pygame.image.load(os.path.join(self.base_path, "frog_sitting_right.png"))
        self.sitting_left = pygame.image.load(os.path.join(self.base_path, "frog_sitting_left.png"))
        self.hopping_up_right = pygame.image.load(os.path.join(self.base_path, "frog_hopping_down_right.png"))
        self.hopping_up_left = pygame.image.load(os.path.join(self.base_path, "frog_hopping_down_left.png"))
        self.hopping_down_right = pygame.image.load(os.path.join(self.base_path, "frog_hopping_down_right.png"))
        self.hopping_down_left = pygame.image.load(os.path.join(self.base_path, "frog_hopping_down_left.png"))
        self.death = pygame.image.load(os.path.join(self.base_path, "frog_dead.png"))

        self.sitting_right = pygame.transform.scale(self.sitting_right, (Frog.SIZE, Frog.SIZE))
        self.sitting_left = pygame.transform.scale(self.sitting_left, (Frog.SIZE, Frog.SIZE))
        self.hopping_up_right = pygame.transform.scale(self.hopping_up_right, (Frog.SIZE, Frog.SIZE))
        self.hopping_up_left = pygame.transform.scale(self.hopping_up_left, (Frog.SIZE, Frog.SIZE))
        self.hopping_down_right = pygame.transform.scale(self.hopping_down_right, (Frog.SIZE, Frog.SIZE))
        self.hopping_down_left = pygame.transform.scale(self.hopping_down_left, (Frog.SIZE, Frog.SIZE))
        self.death = pygame.transform.scale(self.death, (Frog.SIZE, Frog.SIZE))

        self.right_hopping_animation = [self.sitting_right, self.hopping_up_right, self.hopping_down_right]
        self.left_hopping_animation = [self.sitting_left, self.hopping_up_left, self.hopping_down_left]



