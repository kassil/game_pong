# main.py

import pygame
import sys
from settings import *
from player import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kevin's Game of Pong")

# Set up the game objects
ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30, 30)
players = (
    Player(paddle_margin),
    Player(screen_width - paddle_margin - paddle_width)
)
light_grey = (200, 200, 200)

# Set up the clock
clock = pygame.time.Clock()
accumulator = 0.0

# Set up the font
font = pygame.font.SysFont(font_name, font_size)

# Move the ball
def move_ball():
    ball.x += ball_speed[0] * time_step
    ball.y += ball_speed[1] * time_step

    # Check for collision with the walls
    if ball.top < 0 or ball.bottom >= screen_height:
        ball_speed[1] *= -1
        wall_collision_sound.play()
    if ball.left < 0:
        scored(1)
    elif ball.right >= screen_width:
        scored(0)

    # Check for collision with the players
    if ball.colliderect(players[0].paddle) or ball.colliderect(players[1].paddle):
        player_collision_sound.play()
        ball_speed[0] *= -1
        if ball.left < players[0].paddle.right and ball_speed[0] < 0:
            # Calculate the angle between the ball's center and the point of impact on the paddle
            y_distance = ball.centery - players[0].paddle.centery
            max_distance = players[0].paddle.height / 2
            angle = y_distance / max_distance
            ball_speed[1] = angle * ball_speed[0]
            ball.left = players[0].paddle.right
        if ball.right > players[1].paddle.left and ball_speed[0] > 0:
            # Calculate the angle between the ball's center and the point of impact on the paddle
            y_distance = ball.centery - players[1].paddle.centery
            max_distance = players[1].paddle.height / 2
            angle = y_distance / max_distance
            ball_speed[1] = angle * ball_speed[0]
            ball.right = players[1].paddle.left

# Move the paddles
def move_paddles():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and players[0].paddle.top > 0:
        players[0].paddle.y -= paddle_speed * time_step
    if keys[pygame.K_s] and players[0].paddle.bottom < screen_height:
        players[0].paddle.y += paddle_speed * time_step
    if keys[pygame.K_UP] and players[1].paddle.top > 0:
        players[1].paddle.y -= paddle_speed * time_step
    if keys[pygame.K_DOWN] and players[1].paddle.bottom < screen_height:
        players[1].paddle.y += paddle_speed * time_step

# Assign a point to player p and move the ball to the centre of the field.
def scored(p):
    players[p].score += 1
    ball_speed[0] *= -1
    ball.x = screen_width/2 - ball_size
    ball.y = screen_height/2 - ball_size
    wall_collision_sound.play()

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
        move_ball()
        move_paddles()

        # Subtract time step from accumulator
        accumulator -= time_step

    # Draw the game objects
    screen.fill(bg_color)
    for player in players:
        pygame.draw.rect(screen, paddle_color, player.paddle)
    pygame.draw.circle(screen, ball_color, ball.center, ball_size)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # Draw the score
    score_text = f"{players[0].score} : {players[1].score}"
    score_surface = font.render(score_text, True, light_grey)
    score_rect = score_surface.get_rect(center=(screen_width/2, 50))
    screen.blit(score_surface, score_rect)

    # Update the screen
    pygame.display.flip()
