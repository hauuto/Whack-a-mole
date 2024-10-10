import pygame
import sys

from settings import *


pygame.init()
pygame.font.init()


screen = pygame.display.set_mode(screen_size)
display.set_caption("Main Menu")


f = pygame.font.Font(None, 25)
title = pygame.font.Font()
while True:

    screen.fill(Color("white"))
    #
    start_game_text = f.render("Start Game", True, (0, 0, 0))
    text_rect = start_game_text.get_rect(center = screen.get_rect().center)
    screen.blit(start_game_text, text_rect)
    #

    #
    setting_text = f.render("Setting", True, (0, 0, 0))
    text_rect = setting_text.get_rect(center = (screen.get_rect().centerx, screen.get_rect().centery + 50))
    screen.blit(setting_text, text_rect)
    #

    #
    quit_text = f.render("Quit", True, (0, 0, 0))
    text_rect = quit_text.get_rect(center = (screen.get_rect().centerx, screen.get_rect().centery + 100))
    screen.blit(quit_text, text_rect)
    #

    pygame.display.update()
    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        sys.exit()
