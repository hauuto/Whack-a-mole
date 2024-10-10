from pygame.sprite import *
from pygame import *
from numpy.random import randint

from settings import *

class Mole(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/mole.gif")
        self.rect = self.image.get_rect()


    def flee(self):
        randX = randint(100, screen_width-100)
        randY = randint(100, screen_height-100)
        self.rect.center = (randX,randY)




class Shovel(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/shovel.gif")
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.center = mouse.get_pos()