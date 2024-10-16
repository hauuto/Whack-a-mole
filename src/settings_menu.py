import pygame
import sys
import importlib
import os
from settings import screen_width, screen_height, hit_sound, main_menu_sound

pygame.init()
pygame.font.init()
pygame.mouse.set_visible(True)
# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Settings")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (98, 111, 71)
beige = (254, 250, 224)
highlight_color = (103, 70, 54)

# Fonts
font = pygame.font.Font("../assets/fonts/Lovelo Black.otf", screen_width*screen_height//(screen_width+screen_height*(screen_width-screen_height)//7))
header = pygame.font.Font("../assets/fonts/Block Berthold Regular.ttf", screen_width*screen_height//(screen_width+screen_height*(screen_width-screen_height)//15))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def settings_menu():
    global screen
    input_boxes = [
        pygame.Rect(screen_width*(3/6), screen_height*(3/10), screen_width//32, screen_width*screen_height//(screen_width+screen_height*(screen_width-screen_height)//7)),
        pygame.Rect(screen_width*(3/6), screen_height*(4/10), screen_width//32, screen_width*screen_height//(screen_width+screen_height*(screen_width-screen_height)//7)),
        pygame.Rect(screen_width*(3/6), screen_height*(5/10), screen_width//32, screen_width*screen_height//(screen_width+screen_height*(screen_width-screen_height)//7)),
        pygame.Rect(screen_width*(3/6), screen_height*(6/10), screen_width//32, screen_width*screen_height//(screen_width+screen_height*(screen_width-screen_height)//7))
    ]
    color = [beige] * 4
    active = [False] * 4
    text = [str(screen_width), str(screen_height), str(main_menu_sound.get_volume()), str(hit_sound.get_volume())]

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    if input_boxes[i].collidepoint(event.pos):
                        active[i] = not active[i]
                    else:
                        active[i] = False
                    color[i] = highlight_color if active[i] else beige
                if back_rect.collidepoint(mouse_pos):
                    return  # Exit the settings menu
                if save_rect.collidepoint(mouse_pos):
                    try:
                        new_width = int(text[0])
                        new_height = int(text[1])
                        new_music_volume = float(text[2])
                        new_sound_volume = float(text[3])

                        with open('settings.py', 'w') as f:
                            f.write(f"""
from pygame import *
from pygame.mixer import *

# Game settings

# Screen settings
screen_width = {new_width}
screen_height = {new_height}
screen_size = (screen_width, screen_height)

# Sound settings
mixer.init()
# Load sounds
hit_sound = Sound("../assets/sounds/hit.wav")
hit_sound.set_volume({new_sound_volume})

main_menu_sound = Sound("../assets/sounds/background_music.wav")
main_menu_sound.set_volume({new_music_volume})

# Font settings
font.init()
# Load fonts
""")
                        # Restart the program
                        os.execv(sys.executable, [sys.executable] + sys.argv)
                    except ValueError:
                        pass
            if event.type == pygame.KEYDOWN:
                for i in range(4):
                    if active[i]:
                        if event.key == pygame.K_RETURN:
                            active[i] = False
                            color[i] = beige
                        elif event.key == pygame.K_BACKSPACE:
                            text[i] = text[i][:-1]
                        else:
                            text[i] += event.unicode

        screen.fill(green)
        draw_text("Settings", header, beige, screen, screen.get_rect().centerx-100, screen_height*(1/10))
        draw_text("Screen Width", font, beige, screen, screen_width*(1/6), screen_height*(3/10))
        draw_text("Screen Height", font, beige, screen, screen_width*(1/6), screen_height*(4/10))
        draw_text("Music Volume", font, beige, screen, screen_width*(1/6), screen_height*(5/10))
        draw_text("Sound Volume", font, beige, screen, screen_width*(1/6), screen_height*(6/10))

        for i in range(4):
            txt_surface = font.render(text[i], True, color[i])
            width = max(200, txt_surface.get_width()+10)
            input_boxes[i].w = width
            screen.blit(txt_surface, (input_boxes[i].x+5, input_boxes[i].y+5))
            pygame.draw.rect(screen, color[i], input_boxes[i], 2)

        back_text = font.render("Back", True, beige)
        back_rect = back_text.get_rect(center = (screen.get_rect().centerx - 100, screen.get_rect().centery + 200))
        back_color = highlight_color if back_rect.collidepoint(mouse_pos) else beige
        back_text = font.render("Back", True, back_color)
        screen.blit(back_text, back_rect)

        save_text = font.render("Save", True, beige)
        save_rect = save_text.get_rect(center = (screen.get_rect().centerx + 100, screen.get_rect().centery + 200))
        save_color = highlight_color if save_rect.collidepoint(mouse_pos) else beige
        save_text = font.render("Save", True, save_color)
        screen.blit(save_text, save_rect)

        pygame.display.flip()
        pygame.display.update()

settings_menu()