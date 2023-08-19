# settings.py

import pygame

# Screen settings
screen_width = 800
screen_height = 600
bg_color = (50, 50, 50)

# Ball settings
ball_speed = [400, 400]

# Paddle settings
paddle_speed = 800

# Time settings
time_step = 0.02  # seconds

# Font settings
font_name = 'Arial'
font_size = 64

# Sound settings
# Initialize Pygame mixer
pygame.mixer.init()
wall_collision_sound = pygame.mixer.Sound("Bounce-SoundBible.com-12678623.mp3")
player_collision_sound = pygame.mixer.Sound("bonk-sound-effect.mp3")
