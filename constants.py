#Rachel Dahl
#List of constants to import into other files
import pygame
import os

# keys from pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)

#dimensions of window
SCREEN_DIMENSIONS = (1250, 750)

#sets default movement speed of sprites
SPEED_MULTIPLIER = 2

#generic enemy size, can be changed in Enemy class as well
ENEMY_SIZE = 100

#used to set size of health bar displays
BAR_MULTIPLIER = 20
ICON_SIZE = 35

#path to transparent image to hide sprites
TRANSPARENT = pygame.image.load(os.path.join(os.path.join("graphics", "other"), "transparent.png"))

#colors
PALE_GREEN = (155, 207, 172)
LAVENDER = (160, 132, 189)
BLOOD_ORANGE = (112, 26, 0)

