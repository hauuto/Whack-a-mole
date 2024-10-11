from pygame.sprite import *
from pygame import *
from numpy.random import randint

from settings import *
import pygame
class Mole(Sprite):
    def __init__(self, color=(0,0,0)):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/mole.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width//10, screen_height//10))
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



class main_menu_Mole(Sprite):
    def __init__(self, color=(255,255,255)):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/mole.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width//4, screen_height//4))
        self.image.fill(color,special_flags=pygame.BLEND_MULT)
        self.rect = self.image.get_rect()
        self.rect.center = (2.3/3*screen_width, 1.8/3*screen_height)
class Shovel(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/shovel.gif").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = mouse.get_pos()
        self.rect.move_ip(0, 10)


class Log(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/log.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width//5, screen_height//5))
        self.rect = self.image.get_rect()
        self.rect.center = (1.5/6*screen_width, 2.2/3*screen_height)



class Mountain(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/mountain.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width//3.5, screen_height//4))
        self.rect = self.image.get_rect()
        self.rect.center = (1/6*screen_width, 1.7/3*screen_height)

class Explosion(Sprite):
    def __init__(self, center):
        Sprite.__init__(self)
        self.image = image.load("../assets/images/explosion.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width//10, screen_height//10))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == 6:
                self.kill()
            else:
                center = self.rect.center
                self.image = image.load("../assets/images/explosion.png".format(self.frame)).convert_alpha()
                self.image = pygame.transform.scale(self.image, (screen_width//10, screen_height//10))
                self.rect = self.image.get_rect()
                self.rect.center = center