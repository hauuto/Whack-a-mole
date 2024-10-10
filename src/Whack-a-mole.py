#header
import sys, pygame

from pygame import *
from pygame.sprite import *
from pygame.locals import *

from settings import *
from sprites import *

pygame.init()

# Set up the display
screen = display.set_mode(screen_size)
display.set_caption("Whack-a-mole")

mole1 = Mole(color=(255,255,255))
shovel = Shovel()
mole2 = Mole(color=(255,255,200))

moles = [mole1]
all_sprites = Group(moles, shovel)
screen.fill(Color("white"))
all_sprites.draw(screen)
display.update()

#hide the mouse cursor
mouse.set_visible(False)



#move mole
delay = 1000
MOVE_MOLE = USEREVENT + 1
time.set_timer(MOVE_MOLE, delay)


#count hit
hits = 0

#text
f = font.Font(None, screen_width*screen_height//10000)
green = (121,134,69)
# Game loop
while True:
    ev = event.wait()
    if (ev.type == QUIT) or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
        pygame.quit()
        sys.exit()

    if (ev.type == MOUSEBUTTONDOWN):
        for mole in moles:
            if shovel.rect.colliderect(mole.rect):
                mole.flee(moles)
                hit_sound.play()
                hits += 1

                if hits % 20 ==0:
                    time.set_timer(MOVE_MOLE, delay)
                    new_mole = Mole(color=(randint(100,255),randint(100,255),randint(100,255)))
                    moles.append(new_mole)
                    all_sprites.add(new_mole)

    if (ev.type == MOVE_MOLE):
        for mole in moles:
            mole.flee(moles)


    screen.fill(Color(green))
    screen.blit(f.render("Hits = " + str(hits), False, (0,0,0)), (screen_width//2, 0))

    all_sprites.update()
    all_sprites.draw(screen)
    screen.blit(shovel.image, shovel.rect)
    display.update()
