import pygame, sys


from settings import *

from sprites import *
from pygame.sprite import *


pygame.init()
pygame.font.init()


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
highlight_color = (103, 70, 54)
while True:

    #sound

    main_menu_sound.play()
    #


    #screen
    screen.fill(green)
    all_sprites.draw(screen)
    #

    #

    #
    game_title = header.render("Whack a Mole", True, beige)
    text_rect = game_title.get_rect(center = (screen.get_rect().centerx, screen.get_rect().centery - 150))
    screen.blit(game_title, text_rect)

    mouse_pos = pygame.mouse.get_pos()

    #
    start_game_text = f.render("START GAME", True, beige)
    start_game_rect = start_game_text.get_rect(center=screen.get_rect().center)
    start_game_color = highlight_color if start_game_rect.collidepoint(pygame.mouse.get_pos()) else beige
    start_game_text = f.render("START GAME", True, start_game_color)
    screen.blit(start_game_text, start_game_rect)
    #

    #
    setting_text = f.render("SETTING", True, beige)
    setting_rect = setting_text.get_rect(center=(screen.get_rect().centerx, screen.get_rect().centery + 50))
    setting_color = highlight_color if setting_rect.collidepoint(mouse_pos) else beige
    setting_text = f.render("SETTING", True, setting_color)
    screen.blit(setting_text, setting_rect)
    #

    #
    quit_text = f.render("QUIT", True, beige)
    quit_rect = quit_text.get_rect(center=(screen.get_rect().centerx, screen.get_rect().centery + 100))
    quit_color = highlight_color if quit_rect.collidepoint(mouse_pos) else beige
    quit_text = f.render("QUIT", True, quit_color)
    screen.blit(quit_text, quit_rect)
    #

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_game_rect.collidepoint(event.pos):
                main_menu_sound.stop()
                exec(open("Whack-a-mole.py").read())
            if setting_rect.collidepoint(event.pos):
                exec(open("settings.py").read())
            if quit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()