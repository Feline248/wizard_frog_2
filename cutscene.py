#Rachel Dahl
#controls cutscene animations


import pygame
from abc import ABC, abstractclassmethod

class Cutscene(ABC):

    def __init__(self):
        pass

    @abstractclassmethod
    def run_animation(self):
        raise NotImplementedError

        