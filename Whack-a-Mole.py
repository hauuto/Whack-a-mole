
#header
import sys
import pygame
from numpy.random import randint
from pygame import *
from pygame.sprite import *
from pygame.locals import *
from pygame.mixer import *

#initialize
pygame.init()  #pygame initialize
pygame.mixer.init() #sound initialize



#mole setting
class mole(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("mole.gif").convert()
        self.rect = self.image.get_rect()
    def flee(self):
        self.rect.x = randint(0, screen_width - self.rect.width)
        self.rect.y = randint(0, screen_height - self.rect.height)
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        display.update()
class Shovel(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("shovel.gif").convert()
        self.rect = self.image.get_rect()
    def hit(self, target):
        return self.rect.colliderect(target)
    def update(self):
        self.rect.center = mouse.get_pos()


#sound setting
whack = Sound("hit.wav")
background = Sound("background.m4a")

#main

#Windows setting
pygame.display.set_caption("Whack-a-Mole")

#screen setting
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#create objects
mole = mole()
shovel = Shovel()

#hide the mouse cursor
mouse.set_visible(False)



#draw mole
all_sprites = RenderPlain(mole, shovel)
screen.fill((255, 255, 255)) #screen background
all_sprites.draw(screen)
display.update()

while True:
    background.play.set_volume(0.3)
    ev = event.wait()
    if (ev.type == KEYDOWN and ev.key == K_ESCAPE) or ev.type == QUIT:
        pygame.quit()
        sys.exit()
    if ev.type == MOUSEBUTTONDOWN:
        if mole.rect.collidepoint(mouse.get_pos()):
            whack.play().set_volume(0.3)
            x, y = mouse.get_pos()
            mole.flee()
        else:
            print("miss")

    all_sprites.update()
    all_sprites.draw(screen)
    display.update()
