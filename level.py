from pygame import *

class Level():

    def __init__(self, number:int, background_image:str):
        self.number = number
        self.background_path = os.path.join(os.path.join("graphics", "backgrounds"), background_image)
        self.background = image.load(self.background_path)

    def start_level(self):
        """change background and add enemies to the screen"""
        pass

    def end_level(self):
        """hide enemies, open store, and increase level counter"""