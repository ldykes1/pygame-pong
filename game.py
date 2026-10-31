import pygame
from functions import Player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pong Replica")
clock = pygame.time.Clock()
running = True

SCR_HEIGHT = screen.get_height()
SCR_WIDTH = screen.get_width()

bat_1 = Player("white", 130, 0, SCR_HEIGHT)
bat_2 = Player("white", 130, SCR_WIDTH - 10, SCR_HEIGHT)

ball = pygame.Surface((20, 20))
ball.fill("white")
ball_pos = pygame.Vector2((SCR_WIDTH / 2, SCR_HEIGHT / 2))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    screen.blit(bat_1.surface, bat_1.pos)
    screen.blit(bat_2.surface, bat_2.pos)
    screen.blit(ball, ball_pos)  

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bat_1.move(up=True)
    if keys[pygame.K_s]:
        bat_1.move(down=True)
    if keys[pygame.K_UP]:
        bat_2.move(up=True)
    if keys[pygame.K_DOWN]:
        bat_2.move(down=True)

    pygame.display.update()

    dt = clock.tick(60)

pygame.quit()