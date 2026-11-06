import pygame
import random
import math
from functions import Player, Ball, Scoreboard


screen_width = 1280
screen_height = 720
colour_theme = "white"
game_speed = 8
game_font = "press_start_2p.ttf"

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Replica")
clock = pygame.time.Clock()

ball_angle = math.radians(random.choice([0, 180]) + random.randrange(-60,60))

player_one = Player(color=colour_theme, speed=game_speed, side="left", screen_height=screen_height, screen_width=screen_width)
player_two = Player(color=colour_theme, speed=game_speed, side="right", screen_height=screen_height, screen_width=screen_width)
ball = Ball(color=colour_theme, speed=game_speed, angle=ball_angle, screen_height=screen_height, screen_width=screen_width)
scoreboard = Scoreboard(color=colour_theme, font=game_font, font_size=60, screen_width=screen_width)

running = True
reset = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    screen.blit(player_one.surface, player_one.rect)
    screen.blit(player_two.surface, player_two.rect)
    screen.blit(ball.surface, ball.rect)
    screen.blit(scoreboard.surface, scoreboard.rect)

    ball.move(player_rects=[player_one.rect, player_two.rect])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_one.move(up=True)
    if keys[pygame.K_s]:
        player_one.move(down=True)
    if keys[pygame.K_UP]:
        player_two.move(up=True)
    if keys[pygame.K_DOWN]:
        player_two.move(down=True)

    if ball.rect.left < 0:
        player_two.add_point()
        ball.pos = ball.rect.center = pygame.Vector2(screen_width / 2, screen_height / 2)
    if ball.rect.right > screen_width:
        player_one.add_point()
        ball.pos = ball.rect.center = pygame.Vector2(screen_width / 2, screen_height / 2)

    scoreboard.update(f'{player_one.score} : {player_two.score}')

    pygame.display.update()

    dt = clock.tick(60)

pygame.quit()