from pygame import *
from pygame.mixer import *


# Game settings

# Screen settings
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)


# Sound settings
mixer.init()
# Load sounds
hit_sound = Sound("../assets/sounds/hit.wav")