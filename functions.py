# Example file showing a basic pygame "game loop"
import pygame

class Player():
    def __init__(self, color, height, x_pos, y_pos):
        self.height = height
        self.width = 10
        self.speed = 10
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(color)
        self.pos = pygame.Vector2((x_pos, y_pos / 2))

    def move(self, up=False, down=False):
        if up == True:
            self.pos.y -= self.speed
        if down == True:
            self.pos.y += self.speed
        if self.pos.y > 590:
            self.pos.y = 590
        if self.pos.y < 0:
            self.pos.y = 0