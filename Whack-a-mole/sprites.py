from pygame.sprite import *
from pygame import *
from numpy.random import randint

from settings import *
import pygame
class Mole(Sprite):
    def __init__(self, color=(0,0,0)):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/mole.gif").convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.image.fill(color,special_flags=pygame.BLEND_MULT)
        self.rect = self.image.get_rect()


    def flee(self, other_moles):
        while True:
            randX = randint(100, screen_width - self.rect.width - 100)
            randY = randint(100, screen_height - self.rect.height - 100)
            self.rect.center = (randX,randY)
            if not any(self.rect.colliderect(mole.rect) for mole in other_moles if mole != self):
                break




class Shovel(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/shovel.gif")
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.center = mouse.get_pos()