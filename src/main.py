import pygame, sys


from settings import *


pygame.init()
pygame.font.init()
from sprites import *
from pygame.sprite import *

screen = pygame.display.set_mode(screen_size)
display.set_caption("Main Menu")

f = pygame.font.Font("../assets/fonts/Lovelo Black.otf",screen_width*screen_height//14000)
header = pygame.font.Font("../assets/fonts/Block Berthold Regular.ttf",screen_width*screen_height//6000)


all_sprites = Group()
log = Log()
mountain = Mountain()
mole = main_menu_Mole()
all_sprites.add(mountain, log, mole)
#color
green = (98,111,71)
beige = (254, 250, 224)
while True:
    screen.fill(green)
    all_sprites.draw(screen)
    #

    #
    game_title = header.render("Whack a Mole", True, beige)
    text_rect = game_title.get_rect(center = (screen.get_rect().centerx, screen.get_rect().centery - 150))
    screen.blit(game_title, text_rect)
    #
    start_game_text = f.render("START GAME", True, beige)
    text_rect = start_game_text.get_rect(center = screen.get_rect().center)
    screen.blit(start_game_text, text_rect)
    #

    #
    setting_text = f.render("SETTING", True, beige)
    text_rect = setting_text.get_rect(center = (screen.get_rect().centerx, screen.get_rect().centery + 50))
    screen.blit(setting_text, text_rect)
    #

    #
    quit_text = f.render("QUIT", True, beige)
    text_rect = quit_text.get_rect(center = (screen.get_rect().centerx, screen.get_rect().centery + 100))
    screen.blit(quit_text, text_rect)
    #

    pygame.display.update()
    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        sys.exit()
