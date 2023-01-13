import pygame
from sys import exit
from Stage import Stage
from Game import Game
from Setting import *
from Player import Player

width = 1000
height = 720
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Megaman')
clock = pygame.time.Clock()
Stage = Stage(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Stage.player.sprite.press_down_true = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if Stage.player.sprite.health_timer < 1 and Stage.player.sprite.press_down_true == 1:
                    Stage.player.press_down_true = 0
                    # type of shot
                    if Stage.player.sprite.timer_power_shot >= 1:
                        Stage.player.sprite.is_shooting = True
                        Stage.player.sprite.launch_projectile(0)
                    else:
                        Stage.player.sprite.is_shooting = True
                        Stage.player.sprite.launch_projectile(1)
                    Stage.player.sprite.timer_power_shot = Stage.player.sprite.timer_power_shot_max
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if Stage.player.sprite.press_down_true == 1:
        if Stage.player.sprite.timer_power_shot > 0:
            Stage.player.sprite.timer_power_shot -= 1
    for projectile in Stage.player.sprite.all_projectiles:
        projectile.move()
    screen.fill('black')
    background_image = pygame.image.load('../game/Resources/background/background.png').convert_alpha()
    for i in range(45):
        for j in range(11):
            background_rect = background_image.get_rect(topleft=(j*94, i * 16))
            screen.blit(background_image, background_rect)
    Stage.player.sprite.all_projectiles.draw(screen)
    Stage.display(screen)
    Stage.run(screen)
    pygame.display.update()

    clock.tick(60)  # frame rate
