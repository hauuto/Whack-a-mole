import sys
from random import randint
from PIL import Image

import pygame
from pygame import *
from pygame.locals import *
from pygame.sprite import *

a = 1920
b = 1080

class Mole(Sprite):
    def __init__(self):
        super().__init__()
        self.frames = self.load_gif("mole.gif")
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.animation_speed = 0.4
        self.last_update = pygame.time.get_ticks()

    def load_gif(self, filename):
        gif = Image.open(filename)
        frames = []
        try:
            while True:
                frame = gif.copy()
                frame = frame.convert("RGBA")
                frame = pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode)
                frames.append(frame)
                gif.seek(len(frames))
        except EOFError:
            pass
        return frames

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

    def flee(self):
        self.rect.x = randint(0, a - self.rect.width)
        self.rect.y = randint(0, b - self.rect.height)

class Button:
    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.Font(font, 50)
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, True, pygame.Color("white"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            return True
        return False

pygame.init()
display.set_caption("Whack-a-Mole")
screen = display.set_mode((a, b), DOUBLEBUF)

mole = Mole()
all_sprites = Group(mole)
screen.fill((255, 255, 255))

quit_button = Button("Quit", (a - 200, b - 100), None)

all_sprites.draw(screen)
quit_button.show(screen)
display.update()

while True:
    get_event = event.wait()
    if get_event.type == QUIT:
        sys.exit()
    elif get_event.type == MOUSEBUTTONDOWN:
        if quit_button.click(get_event):
            sys.exit()
        x, y = mouse.get_pos()
        if mole.rect.collidepoint(x, y):
            mole.flee()
            print("Whacked!")
            screen.fill((255, 255, 255))
            all_sprites.draw(screen)
            quit_button.show(screen)
            display.update()
        else:
            print("Missed!")

    all_sprites.update()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    quit_button.show(screen)
    display.update()