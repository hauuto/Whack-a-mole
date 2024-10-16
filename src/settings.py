
from pygame import *
from pygame.mixer import *

# Game settings

# Screen settings
screen_width = 1200
screen_height = 900
screen_size = (screen_width, screen_height)

# Sound settings
mixer.init()
# Load sounds
hit_sound = Sound("../assets/sounds/hit.wav")
hit_sound.set_volume(0.03)

main_menu_sound = Sound("../assets/sounds/background_music.wav")
main_menu_sound.set_volume(0.03)

# Font settings
font.init()
# Load fonts
