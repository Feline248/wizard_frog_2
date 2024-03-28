from abc import ABC
import os

class Spell(ABC):

    def __init__(self, damage:int, sprite_file:str):
        self.damage = damage
        self.sprite_path = os.path.join(os.path.join("graphics", "spells"), sprite_file)


class Bubbles(Spell):
    pass