import pygame
from sys import exit
from Player import Player
from Stage import Stage
width = 1480
height = 720
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Megaman')
clock = pygame.time.Clock()
Stage = Stage((width, height))
Player = Player((100, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0, 0, 0))
    Stage.display(screen)
    Player.display(screen)
    Player.update()
    #if Player.rect.colliderect(Stage.background_rect):
        #Player.des_update()
    print(Player.rect.colliderect(Stage.background_rect))
    pygame.display.update()
    clock.tick(60) #frame rate
