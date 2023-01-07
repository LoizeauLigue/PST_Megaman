import pygame
from sys import exit
from Stage import Stage
from Game import Game
from Setting import *

width = 1000
height = 720
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Megaman')
clock = pygame.time.Clock()
#Stage = Stage((width, height))
game = Game()
Stage = Stage(level_map, screen)
#game.player.add(Stage.player)




while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            game.player.launch_projectile()
      if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    #Stage.display(screen)

    for projectile in game.player.all_projectiles:
           projectile.move()
    game.player.all_projectiles.draw(screen)
    game.player.display(screen)
    game.player.update()
    Stage.run()

    #if game.player.rect.colliderect(Stage.background_rect):
      #  game.player.des_update()
    #print(Player.rect.colliderect(Stage.background_rect))
    pygame.display.update()


    clock.tick(60) #frame rate
    screen.fill('black')
