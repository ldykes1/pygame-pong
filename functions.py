import pygame
import math

class Player():
    def __init__(self, speed: int, colour: str, side: str, screen_width: int, screen_height: int) -> None:
        self.pad = 20
        self.score = 0
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.surface = pygame.Surface((10, 130))
        self.surface.fill(colour)
        self.side = side
        if self.side == "left":
            self.rect = self.surface.get_rect(midleft=(0 + self.pad, self.screen_height / 2))
        elif self.side == "right":
            self.rect = self.surface.get_rect(midright=(self.screen_width - self.pad, self.screen_height / 2))

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

    def reset(self) -> None:
        if self.side == "left":
            self.rect = self.surface.get_rect(midleft=(0 + self.pad, self.screen_height / 2))
        elif self.side == "right":
            self.rect = self.surface.get_rect(midright=(self.screen_width - self.pad, self.screen_height / 2))

class Ball():
    def __init__(self, colour: str, speed: int, screen_width: int, screen_height: int) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = speed
        self.velocity = pygame.Vector2(0, 0)
        self.surface = pygame.Surface((20, 20))
        self.surface.fill(colour)
        self.rect = self.surface.get_rect(center=(self.screen_width / 2, self.screen_height / 2))
        self.pos = pygame.Vector2(self.screen_width / 2, self.screen_height / 2)

    def set_velocity(self, angle: float) -> None:
        self.velocity = pygame.Vector2(self.speed * math.cos(angle), self.speed * math.sin(angle))

    def move(self, player_rects: list) -> None:
        self.pos += self.velocity
        self.rect.center = self.pos
        if self.rect.collideobjects(player_rects):
            self.velocity.x *= -1
            # self.velocity += pygame.Vector2(self.velocity.x * 0.1, self.velocity.y * 0.1)
        if self.rect.top < 0 or self.rect.bottom > self.screen_height:
            self.velocity.y *= -1

class Scoreboard():
    def __init__(self, colour: str, font: str, font_size: int, screen_width: int) -> None:
        self.text = "0 : 0"
        self.colour = colour
        self.dist_from_ceil = 40
        self.screen_width = screen_width
        self.font = pygame.font.SysFont(font, font_size)
        self.surface = self.font.render(self.text, False, self.colour)
        self.rect = self.surface.get_rect(center=(self.screen_width / 2, self.dist_from_ceil))

    def update(self, text: str):
        self.text = text
        self.surface = self.font.render(self.text, False, self.colour)
        self.rect = self.surface.get_rect(center=(self.screen_width / 2, self.dist_from_ceil))