
import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Game")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
