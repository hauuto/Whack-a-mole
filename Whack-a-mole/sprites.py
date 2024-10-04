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
        randX = randint(0, screen_width)
        randY = randint(0, screen_height)
        self.rect.center = (randX,randY)




class Shovel(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/shovel.gif")
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.center = mouse.get_pos()