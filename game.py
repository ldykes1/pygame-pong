import pygame
import random
import math
from functions import Player, Ball, Scoreboard

screen_width = 1280
screen_height = 720
colour_theme = "white"
game_speed = 15
game_font = "press_start_2p.ttf"

pygame.init()
screen = pygame.display.set_mode(size=(screen_width, screen_height))
pygame.display.set_caption("Pong Replica")
clock = pygame.time.Clock()

player_one = Player(colour=colour_theme, speed=game_speed, side="left", screen_height=screen_height, screen_width=screen_width)
player_two = Player(colour=colour_theme, speed=game_speed, side="right", screen_height=screen_height, screen_width=screen_width)
ball = Ball(colour=colour_theme, speed=game_speed, screen_height=screen_height, screen_width=screen_width)
scoreboard = Scoreboard(colour=colour_theme, font=game_font, font_size=60, screen_width=screen_width)

def fill_screen() -> None:
    """
    This function fills the screen with black pixels
    and 'blits' (draws) each surface onto the screen.
    """
    screen.fill("black")
    screen.blit(player_one.surface, player_one.rect)
    screen.blit(player_two.surface, player_two.rect)
    screen.blit(ball.surface, ball.rect)
    screen.blit(scoreboard.surface, scoreboard.rect)

running = True
reset = True
dt = 0
while running:

    dt += clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if reset:
        ball.reset()
        player_one.reset()
        player_two.reset()
        fill_screen()

        font = pygame.font.SysFont(name=game_font, size=40)
        instruction_surface = font.render(f"PRESS ENTER TO START", False, colour_theme)
        instruction_rect = instruction_surface.get_rect(center=(screen_width / 2, screen_height - 50))

        if int(dt / 1000) % 2 == 0:
            screen.blit(instruction_surface, instruction_rect)

        if keys[pygame.K_RETURN]:
            reset = False
    else:

        fill_screen()

        ball.move(player_rects=[player_one.rect, player_two.rect])

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
            reset = True
        if ball.rect.right > screen_width:
            player_one.add_point()
            reset = True

        scoreboard.update(f'{player_one.score} : {player_two.score}')

    pygame.display.update()

pygame.quit()