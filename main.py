import pygame
import random
import os

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

# Load ships
ship_folder = "assets/ships"
ships = []

for file in os.listdir(ship_folder):
    img = pygame.image.load(os.path.join(ship_folder, file))
    ships.append(img)

selected_ship = 0
game_state = "menu"

player = Player(ships[selected_ship])

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

        # MENU
        if game_state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_ship = (selected_ship - 1) % len(ships)

                if event.key == pygame.K_RIGHT:
                    selected_ship = (selected_ship + 1) % len(ships)

                if event.key == pygame.K_RETURN:
                    player = Player(ships[selected_ship])
                    game_state = "game"

        # GAME
        if game_state == "game":
            if event.type == pygame.KEYDOWN:

                # Shoot
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
                    player = Player(ships[selected_ship])

                # Change ship
                if event.key == pygame.K_c and game_over:
                    game_state = "menu"
                    game_over = False

    if game_state == "game" and not game_over:
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Spawn enemy
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

        # Enemy speed
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

    # MENU
    if game_state == "menu":

        title = big_font.render(
            "Select Ship",
            True,
            TEXT_COLOR
        )

        screen.blit(
            title,
            (WIDTH//2 - 140, 100)
        )

        ship = pygame.transform.scale(
            ships[selected_ship],
            (80, 80)
        )

        screen.blit(
            ship,
            (WIDTH//2 - 40, HEIGHT//2 - 40)
        )

        help_text = font.render(
            "<- -> Chon | ENTER Play",
            True,
            TEXT_COLOR
        )

        screen.blit(
            help_text,
            (WIDTH//2 - 170, HEIGHT - 100)
        )

    # GAME
    if game_state == "game":

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

        control_text = font.render(
            "SPACE: Ban | <- ->: Di chuyen",
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

            change_text = font.render(
                "Nhan C de doi may bay",
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

            screen.blit(
                change_text,
                (WIDTH//2 - 150, HEIGHT//2 + 60)
            )

    pygame.display.update()

pygame.quit()