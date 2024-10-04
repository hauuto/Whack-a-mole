import pygame
import sys

from settings import *


pygame.init()
screen = pygame.display.set_mode(screen_size)

f = pygame.font.Font(None, 25)
while True:

    screen.fill(Color("white"))

    text = f.render("Start Game", True, (0, 0, 0))
    text_rect = text.get_rect(center = screen.get_rect().center)
    screen.blit(text, text_rect)

    pygame.display.update()