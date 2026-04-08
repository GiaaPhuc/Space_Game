import pygame
import random
from settings import *

class Enemy:
    def __init__(self):
        self.type = random.randint(1, 3)

        # Enemy thường
        if self.type == 1:
            self.width = 40
            self.height = 40
            self.color = (255, 80, 80)
            self.speed = 1
            self.score = 1

        # Enemy nhanh
        elif self.type == 2:
            self.width = 30
            self.height = 30
            self.color = (255, 220, 80)
            self.speed = 2
            self.score = 2

        # Enemy hiếm
        else:
            self.width = 25
            self.height = 25
            self.color = (200, 80, 255)
            self.speed = 3
            self.score = 5

        self.rect = pygame.Rect(
            random.randint(0, WIDTH - self.width),
            -40,
            self.width,
            self.height
        )

    def update(self, base_speed):
        self.rect.y += base_speed + self.speed

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            border_radius=6
        )