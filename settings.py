# settings.py

import pygame

# Screen settings
screen_width = 800
screen_height = 600
bg_color = (50, 50, 50)

# Ball settings
ball_speed = [400, 400]
ball_color = (200, 200, 0)  # Yellow color
ball_size = 20

# Paddle settings
paddle_margin = 20  # Distance from wall
paddle_width = 20
paddle_height = 100
paddle_color = (210, 210, 210)
paddle_speed = 500

# Time settings
time_step = 0.02  # seconds

# Font settings
font_name = 'Arial'
font_size = 64

# Sound settings
# Initialize Pygame mixer
pygame.mixer.init()
wall_collision_sound = pygame.mixer.Sound("media/Bounce-SoundBible.com-12678623.mp3")
player_collision_sound = pygame.mixer.Sound("media/bonk-sound-effect.mp3")
