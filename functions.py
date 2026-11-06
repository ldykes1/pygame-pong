import pygame
import math

class Player():
    def __init__(self, speed: int, color: str, side: str, screen_width: int, screen_height: int) -> None:
        self.height = 130
        self.width = 10
        self.pad = 20
        self.score = 0
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(color)
        if side == "left":
            x_pos = 0 + self.pad
            self.rect = self.surface.get_rect(midleft=(x_pos, self.screen_height / 2))
        elif side == "right":
            x_pos = self.screen_width - self.pad
            self.rect = self.surface.get_rect(midright=(x_pos, self.screen_height / 2))

    def move(self, up: bool = False, down: bool = False) -> None:
        if up == True:
            self.rect.y -= self.speed
        if down == True:
            self.rect.y += self.speed
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
        if self.rect.top < 0:
            self.rect.top = 0

    def add_point(self) -> None:
        self.score += 1

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

    def move(self, player_rects: list) -> None:
        self.pos += self.velocity
        self.rect.center = self.pos
        if self.rect.collideobjects(player_rects):
            self.velocity.x *= -1
        if self.rect.top < 0 or self.rect.bottom > self.screen_height:
            self.velocity.y *= -1

class Scoreboard():
    def __init__(self, color: str, font: str, font_size: int, screen_width: int) -> None:
        self.text = "0 : 0"
        self.color = color
        self.dist_from_ceil = 40
        self.screen_width = screen_width
        self.font = pygame.font.SysFont(font, font_size)
        self.surface = self.font.render(self.text, False, self.color)
        self.rect = self.surface.get_rect(center=(self.screen_width / 2, self.dist_from_ceil))

    def update(self, text: str):
        self.text = text
        self.surface = self.font.render(self.text, False, self.color)
        self.rect = self.surface.get_rect(center=(self.screen_width / 2, self.dist_from_ceil))
