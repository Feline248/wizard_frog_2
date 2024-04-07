import pygame
from pygame import mixer
from time import sleep
from level import Level
from frog import Frog
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

        #set up clock and delay
        self.clock = pygame.time.Clock()
        self.animation_delay = 0

        #set level
        self.level = self.level1

        #set up display
        self.screen = pygame.display.set_mode(Game.SCREEN_DIMENSIONS)
        pygame.display.set_caption("Wizard Frog 2")
        pygame.display.set_icon(Game.ICON)

        #start music
        mixer.init()
        mixer.music.load(os.path.join("sound", "Eclipse.mp3"))
        mixer.music.play()

        #instantiate frog
        global frog
        frog = Frog()

        #reset variables
        self.hopping_counter = 0
   
        while(RUNNING):

            self.delta_time = self.clock.tick(60)      #set framerate

            #get input
            for event in pygame.event.get():

                if event.type == QUIT:
                    RUNNING = False
                
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    RUNNING = False

            pressed_keys = pygame.key.get_pressed()

            #update display
            
            #show background
            self.screen.blit(self.level.background, (0, 0))

            #increment animation_delay counter
            self.animation_delay += 1

            #only update after a 200 loops
            if self.animation_delay == 50:
                self.animation_delay = 0
                self.update(pressed_keys)
                pygame.display.update()


    def hop_right(self):
        """make frog hop right 1 arbitrary unit tbd"""

        self.hopping_counter += 1

        if self.hopping_counter == len(frog.left_hopping_animation):
                self.hopping_counter = 0

        frog.x_pos += 0.4 * self.delta_time
        self.screen.blit(frog.right_hopping_animation[self.hopping_counter], (frog.x_pos, frog.y_pos))
   
   
    def hop_left(self):
        """make frog hop left 1 arbitrary unit tbd"""

        self.hopping_counter += 1
        if self.hopping_counter == len(frog.left_hopping_animation):
            self.hopping_counter = 0

        frog.x_pos -= 0.4 * self.delta_time
        self.screen.blit(frog.left_hopping_animation[self.hopping_counter], (frog.x_pos, frog.y_pos))
  

    def update(self, keys:dict):

        if keys[K_RIGHT]:
            self.hop_right()

        if keys[K_LEFT]:
            self.hop_left()



