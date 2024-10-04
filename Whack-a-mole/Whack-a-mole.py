#header
import sys
import pygame

from pygame import *
from pygame.sprite import *
from pygame.locals import *

from settings import *
from sprites import *

pygame.init()

# Set up the display
screen = display.set_mode(screen_size)
display.set_caption("Whack-a-mole")

mole = Mole()
mole2 = Mole()
shovel = Shovel()

all_sprites = Group(mole, shovel)
screen.fill(Color("white"))
all_sprites.draw(screen)
display.update()

#hide the mouse cursor
mouse.set_visible(False)

# Game loop
while True:
    ev = event.wait()
    if (ev.type == QUIT) or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
        pygame.quit()
        sys.exit()

    if (ev.type == MOUSEBUTTONDOWN):
        if shovel.rect.colliderect(mole.rect):
            mole.flee()
            hit_sound.play()


    screen.fill(Color("white"))
    all_sprites.update()
    all_sprites.draw(screen)
    display.update()
