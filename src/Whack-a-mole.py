import sys, pygame
from pygame import *
from pygame.sprite import *
from pygame.locals import *
from settings import *
from sprites import *

pygame.init()
font.init()

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

# Hide the mouse cursor
mouse.set_visible(False)

# Move mole
delay = 1000
MOVE_MOLE = USEREVENT + 1
time.set_timer(MOVE_MOLE, delay)

# Count hit
hits = 0

# Colors
green = (98, 111, 71)
beige = (254, 250, 224)
highlight_color = (103, 70, 54)

# Fonts
f = pygame.font.Font("../assets/fonts/Lovelo Black.otf", screen_width*screen_height//(screen_width+screen_height*(screen_width-screen_height)//7))

# Add the back button
back_text = f.render("Back", True, beige)
back_rect = back_text.get_rect(topleft=(10, screen_height - 50))

# Game loop
while True:
    for ev in event.get():
        if (ev.type == QUIT) or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if (ev.type == MOUSEBUTTONDOWN):
            if back_rect.collidepoint(ev.pos):
                exec(open("main.py").read())
            for mole in moles:
                if shovel.rect.colliderect(mole.rect):
                    mole.flee(moles)
                    hit_sound.play()
                    hits += 1

                    explosion = Explosion(mole.rect.center)
                    all_sprites.add(explosion)

                    if hits % 20 == 0:
                        time.set_timer(MOVE_MOLE, delay-200)
                        new_mole = Mole(color=(randint(100,255),randint(100,255),randint(100,255)))
                        moles.append(new_mole)
                        all_sprites.add(new_mole)

        if (ev.type == MOVE_MOLE):
            for mole in moles:
                mole.flee(moles)

    screen.fill(green)
    back_color = highlight_color if back_rect.collidepoint(pygame.mouse.get_pos()) else beige
    back_text = f.render("Back", True, back_color)
    screen.blit(back_text, back_rect)
    screen.blit(f.render("Hits = " + str(hits), False, beige), (screen_width//2, 0))

    all_sprites.update()
    all_sprites.draw(screen)
    screen.blit(shovel.image, shovel.rect)
    display.update()

    pygame.time.Clock().tick(60)