import pygame
from settings import *

class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/plane.png")
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2, HEIGHT - 70)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Giữ trong màn hình
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)