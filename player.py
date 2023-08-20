from settings import *
import pygame

class Player:
    def __init__(self, paddle_x):
		# Set up the score variable
        self.score = 0
        self.paddle = pygame.Rect(paddle_x, screen_height/2 - paddle_height/2, paddle_width, paddle_height)
