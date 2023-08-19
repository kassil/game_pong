# main.py

import pygame
import sys
from settings import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Set up the game objects
ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30, 30)
player1 = pygame.Rect(50, screen_height/2-70, 20, 140)
player2 = pygame.Rect(screen_width-70, screen_height/2-70, 20, 140)
light_grey = (200, 200, 200)

# Set up the clock
clock = pygame.time.Clock()
accumulator = 0.0

# Set up the score variables
score1 = 0
score2 = 0
font = pygame.font.SysFont(font_name, font_size)

# Set up the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Accumulate time
    accumulator += clock.tick(60) / 1000.0  # seconds

    # Update the game state in fixed time steps
    while accumulator >= time_step:
        # Move the ball
        ball.x += ball_speed[0] * time_step
        ball.y += ball_speed[1] * time_step

        # Check for collision with the walls
        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_speed[1] *= -1
        if ball.left <= 0:
            score2 += 1
            ball_speed[0] *= -1
            ball.x = screen_width/2-15
            ball.y = screen_height/2-15
        if ball.right >= screen_width:
            score1 += 1
            ball_speed[0] *= -1
            ball.x = screen_width/2-15
            ball.y = screen_height/2-15

        # Check for collision with the players
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_speed[0] *= -1

        # Move the paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.top > 0:
            player1.y -= paddle_speed * time_step
        if keys[pygame.K_s] and player1.bottom < screen_height:
            player1.y += paddle_speed * time_step
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= paddle_speed * time_step
        if keys[pygame.K_DOWN] and player2.bottom < screen_height:
            player2.y += paddle_speed * time_step

        # Subtract time step from accumulator
        accumulator -= time_step

    # Draw the game objects
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # Draw the score
    score_text = f"{score1} : {score2}"
    score_surface = font.render(score_text, True, light_grey)
    score_rect = score_surface.get_rect(center=(screen_width/2, 50))
    screen.blit(score_surface, score_rect)

    # Update the screen
    pygame.display.flip()
