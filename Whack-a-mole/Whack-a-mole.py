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
shovel = Shovel()

all_sprites = Group(mole, shovel)
moles = [mole]
screen.fill(Color("white"))
all_sprites.draw(screen)
display.update()

#hide the mouse cursor
mouse.set_visible(False)



#move mole
MOVE_MOLE = USEREVENT + 1
time.set_timer(MOVE_MOLE, 1000)


#count hit
hits = 0

#text
f = font.Font(None, 25)

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
            hits+=1
            if hits % 5 ==0:
                new_mole = Mole()
                moles.append(new_mole)
                all_sprites.add(new_mole)

    if (ev.type == MOVE_MOLE):
        for mole in moles:
            mole.flee()


    screen.fill(Color("white"))
    all_sprites.update()
    all_sprites.draw(screen)
    display.update()
