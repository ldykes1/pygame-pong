import pygame
import random
import math
from functions import Player, Ball

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Replica")
clock = pygame.time.Clock()

colour_theme = "white"
game_speed = 8

player_one = Player(color=colour_theme, speed=game_speed, side="left", screen_height=screen_height, screen_width=screen_width)
player_two = Player(color=colour_theme, speed=game_speed, side="right", screen_height=screen_height, screen_width=screen_width)

ball_angle = math.radians(random.choice([0, 180]) + random.randrange(-60,60))
ball = Ball(color=colour_theme, speed=game_speed, angle=ball_angle, screen_height=screen_height, screen_width=screen_width)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    screen.blit(player_one.surface, player_one.rect)
    screen.blit(player_two.surface, player_two.rect)
    screen.blit(ball.surface, ball.rect)

    ball.move()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_one.move(up=True)
    if keys[pygame.K_s]:
        player_one.move(down=True)
    if keys[pygame.K_UP]:
        player_two.move(up=True)
    if keys[pygame.K_DOWN]:
        player_two.move(down=True)

    pygame.display.update()

    dt = clock.tick(60)

pygame.quit()