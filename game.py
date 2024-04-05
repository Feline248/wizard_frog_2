from pygame import *
from level import Level
import os

class Game(Surface):

    SCREEN_DIMENSIONS = (2376, 1134)
    ICON = image.load(os.path.join(os.path.join("graphics", "characters"), "wizard-frog.png"))

    def __init__(self):
        display.set_mode(Game.SCREEN_DIMENSIONS)
        display.set_caption("Wizard Frog 2")
        display.set_icon(Game.ICON)

    def create_levels(self):
        """instantiate 5 Level objects"""
        level1 = Level(1, "swamp.png")

    def play(self):
        pass