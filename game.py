import pygame
from pygame import mixer
from level import Level
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

class Game(pygame.Surface):

    SCREEN_DIMENSIONS = (1250, 750)
    ICON = pygame.image.load(os.path.join(os.path.join("graphics", "other"), "frog_icon.jpg"))


    def __init__(self):
        self.create_levels()


    def create_levels(self):
        """instantiate 5 Level objects"""
        self.level1 = Level(1, "swamp.png")


    def play(self):
        """handles actual gameplay"""
        RUNNING = True

        #set level
        self.level = self.level1

        #set up display
        screen = pygame.display.set_mode(Game.SCREEN_DIMENSIONS)
        pygame.display.set_caption("Wizard Frog 2")
        pygame.display.set_icon(Game.ICON)

        #start music
        mixer.init()
        mixer.music.load(os.path.join("sound", "Eclipse.mp3"))
        mixer.music.play()
   
        while(RUNNING):

            #get input
            for event in pygame.event.get():

                if event.type == QUIT:
                    RUNNING = False
                
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    RUNNING = False
                
            #gameplay

            #update display
            screen.blit(self.level.background, (0, 0))
            pygame.display.update()
