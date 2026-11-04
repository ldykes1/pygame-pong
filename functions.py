import pygame
import math

class Player():
    def __init__(self, speed: int, color: str, side: str, screen_width: int, screen_height: int) -> None:
        self.height = 130
        self.width = 10
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(color)
        if side == "left":
            self.x_pos = 0
            self.rect = self.surface.get_rect(midleft=(self.x_pos, self.screen_height / 2))
        elif side == "right":
            self.x_pos = self.screen_width
            self.rect = self.surface.get_rect(midright=(self.x_pos, self.screen_height / 2))

    def move(self, up: bool = False, down: bool = False) -> None:
        if up == True:
            self.rect.y -= self.speed
        if down == True:
            self.rect.y += self.speed
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
        if self.rect.top < 0:
            self.rect.top = 0

class Ball():
    def __init__(self, color: str, speed: int, angle: float, screen_width: int, screen_height: int) -> None:
        self.height = 20
        self.width = 20
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity = pygame.Vector2(speed * math.cos(angle), speed * math.sin(angle))
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(center=(self.screen_width / 2, self.screen_height / 2))
        self.pos = pygame.Vector2(self.screen_width / 2, self.screen_height / 2)

    def move(self) -> None:
        self.pos += self.velocity
        self.rect.center = self.pos
        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.velocity.x *= -1
        if self.rect.top < 0 or self.rect.bottom > self.screen_height:
            self.velocity.y *= -1