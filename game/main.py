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
                Stage.player.sprite.is_shooting = True
                Stage.player.sprite.launch_projectile()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for projectile in Stage.player.sprite.all_projectiles:
        projectile.move()
    Stage.player.sprite.all_projectiles.draw(screen)

    Stage.display(screen)
    Stage.run()
    pygame.display.update()

    clock.tick(60)  # frame rate
    screen.fill('black')
