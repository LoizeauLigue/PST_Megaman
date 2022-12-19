import pygame
from sys import exit
#from Player import Player
width = 800
height = 400
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Megaman')
clock = pygame.time.Clock()

# Mise du fond
fillbackground = pygame.Surface((width, height))
color = (244, 164, 96)
fillbackground.fill(color)

background = pygame.image.load('Resources/background/map_1.png')

life = pygame.Surface((15, 30))
life.fill('RED')


# Joueur
megaman_basic1 = pygame.image.load('Resources/megaman/idle.png')
megaman_basic2 = pygame.image.load('Resources/megaman/idle_2.png')
megaman_walk1 = pygame.image.load('Resources/megaman/walk_1.png')
megaman_walk2 = pygame.image.load('Resources/megaman/walk_2.png')
megaman_walk3 = pygame.image.load('Resources/megaman/walk_3.png')
megaman = [megaman_walk1, megaman_walk2, megaman_walk3]
player_x = 50
choice = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(fillbackground, (0, 0))
    screen.blit(background, (0, 0))
    screen.blit(life, (3, 1))
    screen.blit(megaman[int(choice)], (player_x, 50))
    player_x += 1
    choice = (choice + 0.15) % 3
    if player_x > 800:
        player_x = 0

    pygame.display.update()
    clock.tick(60) #frame rate
