#Rachel Dahl
#the Game class
#runs the game logic and graphics


from pygame import mixer
from time import sleep
from level import Level
from frog import Frog
from spell import *
from constants import *
from time import sleep
import os


class Game(pygame.Surface):

    ICON = pygame.image.load(os.path.join(os.path.join("graphics", "other"), "frog_icon.jpg"))

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

            if self.level.enemy.health <= 0:
                self.win_level()

            if self.frog.health <= 0:
                self.die()

            #increase magic
            if pygame.time.get_ticks() % MAGIC_DELAY == 0 and self.frog.magic <= Frog.MAX_MAGIC:
                self.frog.magic += 1

            #increment animation_delay counter
            self.animation_delay += 1

            #only update after a set number of loops
            if self.animation_delay == 7 and self.level.enemy.health > 0:
                self.animation_delay = 0
                self.update(pressed_keys)
                pygame.display.update()

            

                


    def hop_right(self):
        """make frog hop right 1 arbitrary unit"""

        self.hopping_counter += 1

        if self.hopping_counter >= len(self.frog.left_hopping_animation):
                self.hopping_counter = 0

        if self.frog.x_pos < SCREEN_DIMENSIONS[0] - Frog.SIZE:
            self.frog.x_pos += SPEED_MULTIPLIER * self.delta_time

        self.screen.blit(self.frog.right_hopping_animation[self.hopping_counter], (self.frog.x_pos, self.frog.y_pos))
   
   
    def hop_left(self):
        """make frog hop left 1 arbitrary unit"""

        self.hopping_counter += 1

        if self.hopping_counter >= len(self.frog.left_hopping_animation):
            self.hopping_counter = 0

        if self.frog.x_pos > 0:
            self.frog.x_pos -= SPEED_MULTIPLIER * self.delta_time

        self.screen.blit(self.frog.left_hopping_animation[self.hopping_counter], (self.frog.x_pos, self.frog.y_pos))


    def jump(self):
        """make frog jump up and down to dodge enemy"""
  

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
        self.spell.set_coordinates(self.level.enemy)
        self.spell.x_pos = self.frog.x_pos
        self.spell.y_pos = self.frog.y_pos
        self.frog.magic -= self.spell.cost
        
        
    def move_spell(self):
        """move spell towards enemy"""
        if self.spell.x_pos < self.spell.current_enemy_x:
            self.spell.x_pos += SPEED_MULTIPLIER * self.delta_time
        if self.spell.x_pos > self.spell.current_enemy_x:
            self.spell.x_pos -= SPEED_MULTIPLIER * self.delta_time
        if self.spell.y_pos < self.spell.current_enemy_y:
            self.spell.y_pos += SPEED_MULTIPLIER * self.delta_time
        if self.spell.y_pos > self.spell.current_enemy_y:
            self.spell.y_pos -= SPEED_MULTIPLIER * self.delta_time



    def update(self, keys:dict):
        """update based on which keys are pressed"""

        #show health bars
        self.update_bar(self.frog.sitting_right, PALE_GREEN, (SCREEN_DIMENSIONS[0] - 175, 25), HEALTH_BAR_MULTIPLIER, self.frog.health)
        self.update_bar(self.frog.sitting_left, LAVENDER, (SCREEN_DIMENSIONS[0] - 175, 75), MAGIC_BAR_MULTIPLIER, self.frog.magic)
        self.update_bar(self.level.enemy.sprite, BLOOD_ORANGE, (50, 25), HEALTH_BAR_MULTIPLIER, self.level.enemy.health)

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

        #damage frog when it touches enemy
        if self.level.enemy.x_pos <= self.frog.x_pos + self.frog.SIZE and self.level.enemy.x_pos >= self.frog.x_pos - self.frog.SIZE and self.level.enemy.y_pos <= self.frog.y_pos + self.frog.SIZE and self.level.enemy.y_pos >= self.frog.y_pos - self.frog.SIZE:
            self.frog.health -= 1


        #spell controls
        if keys[K_SPACE] or keys[K_a] and self.frog.magic >= Bubbles.COST:
            self.cast_spell("bubbles")

        if self.spell != None:
            
            self.move_spell()

            #delete spell and do damage when it hits enemy
            if self.spell.x_pos >= self.level.enemy.x_pos and self.spell.x_pos <= self.level.enemy.x_pos + self.level.enemy.size and self.spell.y_pos >= self.level.enemy.y_pos and self.spell.y_pos <= self.level.enemy.y_pos + self.level.enemy.size:
                self.spell.do_damage(self.level.enemy)
                self.screen.blit(TRANSPARENT, (self.spell.x_pos, self.spell.y_pos))
                self.spell = None

            #delete spell when it reaches original target
            elif self.spell.x_pos == self.spell.current_enemy_x and self.spell.y_pos == self.spell.current_enemy_y:
                self.spell = None
                self.screen.blit(self.spell.sprite, (self.spell.x_pos, self.spell.y_pos))

            #display spell on screen
            else:
                self.screen.blit(self.spell.sprite, (self.spell.x_pos, self.spell.y_pos))

        

            
    def win_level(self):
        """Display cutscene and store after winning.
        In the demo version, this function only shows the 
        You Won! screen"""

        ending = pygame.image.load(os.path.join(os.path.join("graphics", "other"), "DemoCompletionScreen.png"))
        self.screen.blit(ending, (0, 0))
        pygame.display.update()


    def die(self):
        """end game and display dead frog"""

        #stop music
        mixer.music.stop()

        #hide sprites
        self.screen.blit(TRANSPARENT, (self.level.enemy.x_pos, self.level.enemy.y_pos))

        if self.spell != None:
            self.screen.blit(TRANSPARENT, (self.spell.x_pos, self.spell.y_pos))

        #dead frog
        self.screen.blit(self.frog.death, (self.frog.x_pos, self.frog.y_pos))


    def update_bar(self, icon:pygame.Surface, color:tuple, top_left:tuple, multiplier:int, value:int):
        """update status bars such as health and magic levels"""

        rect = pygame.Rect(top_left[0], top_left[1], value * multiplier, BAR_THICKNESS)
        pygame.draw.rect(self.screen, color, rect)
        icon = pygame.transform.scale(icon, (ICON_SIZE, ICON_SIZE))
        self.screen.blit(icon, (top_left[0] - ICON_SIZE, top_left[1]))

           
            
             



