import pygame
from pygame import mixer
from time import sleep
from level import Level
from frog import Frog
from spell import *
from constants import *
import os


class Game(pygame.Surface):

    ICON = pygame.image.load(os.path.join(os.path.join("graphics", "other"), "frog_icon.jpg"))
    SPEED_MULTIPLIER = 2

    def __init__(self):
        self.create_levels()

    def create_levels(self):
        """instantiate 5 Level objects and enemies for each"""
        self.level1 = Level(1, "swamp.png", Enemy(5, 1, "laser_butterfly.png"))

    def play(self):
        """handles actual gameplay"""

        RUNNING = True

        #set up clock and delay
        self.clock = pygame.time.Clock()
        self.animation_delay = 0

        #set level
        self.level = self.level1

        #set up display
        self.screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
        pygame.display.set_caption("Wizard Frog 2")
        pygame.display.set_icon(Game.ICON)

        #start music
        mixer.init()
        mixer.music.load(os.path.join("sound", "Eclipse.mp3"))
        mixer.music.play()

        #instantiate frog
        self.frog = Frog()

        #reset variables
        self.hopping_counter = 0
        self.spell = None
   
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

            #only update after a set number of loops
            if self.animation_delay == 7:
                self.animation_delay = 0
                self.update(pressed_keys)
                pygame.display.update()


    def hop_right(self):
        """make frog hop right 1 arbitrary unit"""

        self.hopping_counter += 1

        if self.hopping_counter >= len(self.frog.left_hopping_animation):
                self.hopping_counter = 0

        self.frog.x_pos += Game.SPEED_MULTIPLIER * self.delta_time

        self.screen.blit(self.frog.right_hopping_animation[self.hopping_counter], (self.frog.x_pos, self.frog.y_pos))
   
   
    def hop_left(self):
        """make frog hop left 1 arbitrary unit"""

        self.hopping_counter += 1

        if self.hopping_counter >= len(self.frog.left_hopping_animation):
            self.hopping_counter = 0

        self.frog.x_pos -= Game.SPEED_MULTIPLIER * self.delta_time

        self.screen.blit(self.frog.left_hopping_animation[self.hopping_counter], (self.frog.x_pos, self.frog.y_pos))
  

    def cast_spell(self, spell_type:str):
        """cast a spell"""

        #instantiate spell
        if spell_type == "bubbles":
            self.spell = Bubbles()

        # if spell_type == "fireball":
        #     self.spell = Fireball()

        # if spell_type == "shock":
        #     self.spell = Shock()
        

        #get start and end locations for spell
        self.current_enemy_x = self.level.enemy.x_pos
        self.current_frog_x = self.frog.x_pos
        self.current_enemy_y = self.level.enemy.y_pos
        self.current_frog_y = self.frog.y_pos

        self.spell_x = self.current_frog_x
        self.spell_y = self.current_frog_y
        
        




    def update(self, keys:dict):
        """update based on which keys are pressed"""

        #movement controls
        if keys[K_RIGHT]:
            self.hop_right()

        elif keys[K_LEFT]:
            self.hop_left()

        else:
            self.screen.blit(self.frog.sitting_right, (self.frog.x_pos, self.frog.y_pos))

        #move enemy
        self.level.enemy.move()
        self.screen.blit(self.level.enemy.sprite, (self.level.enemy.x_pos, self.level.enemy.y_pos,))

        #spell controls
        if keys[K_SPACE]:
            self.cast_spell("bubbles")

        if self.spell != None:
            

            #delete spell and do damage when it hits enemy
            if self.spell_x == self.level.enemy.x_pos or self.spell_y == self.level.enemy.y_pos:
                self.spell.do_damage(self.level.enemy)

            #display spell on screen
            self.screen.blit(self.spell.sprite, (self.spell_x, self.spell_y))

            
           
            
             



