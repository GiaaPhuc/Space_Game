import pygame
import random

from player import Player
from enemy import Enemy
from bullet import Bullet
from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 50)

player = Player()

bullets = []
enemies = []

score = 0
spawn_timer = 0

running = True
game_over = False

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Bắn đạn
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullets.append(
                    Bullet(
                        player.rect.centerx - 2,
                        player.rect.top
                    )
                )

            # Restart
            if event.key == pygame.K_r and game_over:
                bullets.clear()
                enemies.clear()
                score = 0
                game_over = False
                player = Player()

    if not game_over:
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Spawn enemy nhanh dần
        spawn_timer += 1
        spawn_delay = max(15, 40 - score // 5)

        if spawn_timer > spawn_delay:
            enemies.append(Enemy())
            spawn_timer = 0

        # Update bullets
        for bullet in bullets[:]:
            bullet.update()

            if bullet.rect.bottom < 0:
                bullets.remove(bullet)

        # Tốc độ enemy tăng theo score
        enemy_speed = ENEMY_SPEED + score * 0.02

        # Update enemies
        for enemy in enemies[:]:
            enemy.update(enemy_speed)

            if enemy.rect.top > HEIGHT:
                enemies.remove(enemy)

        # Collision bullet vs enemy
        for enemy in enemies[:]:
            for bullet in bullets[:]:
                if enemy.rect.colliderect(bullet.rect):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score += enemy.score
                    break

        # Player collision
        for enemy in enemies:
            if enemy.rect.colliderect(player.rect):
                game_over = True

    # Draw
    screen.fill(BACKGROUND)

    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    # Score
    score_text = font.render(
        f"Score: {score}",
        True,
        TEXT_COLOR
    )

    # Hướng dẫn
    control_text = font.render(
        "SPACE: Ban | <- ->: Di chuyen | R: Restart",
        True,
        TEXT_COLOR
    )

    screen.blit(score_text, (10, 10))
    screen.blit(control_text, (10, 40))

    # Game Over
    if game_over:
        game_over_text = big_font.render(
            "GAME OVER",
            True,
            (255, 80, 80)
        )

        restart_text = font.render(
            "Nhan R de choi lai",
            True,
            TEXT_COLOR
        )

        screen.blit(
            game_over_text,
            (WIDTH//2 - 150, HEIGHT//2 - 40)
        )

        screen.blit(
            restart_text,
            (WIDTH//2 - 120, HEIGHT//2 + 20)
        )

    pygame.display.update()

pygame.quit()