import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Megaman')
clock = pygame.time.Clock()

# Mise du fond
background = pygame.image.load('Resources/background/map_1.png')
test_surface = pygame.Surface((100, 200))
test_surface.fill('RED')

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
    # screen.blit(test_surface, (0, 0))
    screen.blit(background, (0, 0))

    screen.blit(megaman[int(choice)], (player_x, 50))
    player_x += 1
    choice = (choice + 0.1) % 3

    pygame.display.update()
    clock.tick(60)
