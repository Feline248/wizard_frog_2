from pygame import *
import os

class Game(Surface):

    SCREEN_DIMENSIONS = (1500, 500)
    ICON = image.load(os.path.join(os.path.join("graphics", "characters"), "wizard-frog.png"))

    def __init__(self):
        display.set_mode(Game.SCREEN_DIMENSIONS)
        display.set_caption("Wizard Frog 2")
        display.set_icon(Game.ICON)

    def play(self):
        pass