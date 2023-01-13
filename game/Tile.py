import pygame
from Setting import *
from support import import_folder


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('../game/Resources/background/brick.png').convert_alpha()

        # self.image = pygame.Surface((size, size))
        # self.image.fill('grey')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Tile_mouv(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('../game/Resources/background/brick_2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.maximum = self.rect.y
        self.fase = 0

    def update(self, x_shift):
        self.rect.x += x_shift
        if self.fase == 0:
            self.rect.y -= 2
            if self.maximum - self.rect.y > 200:
                self.fase = 1
        elif self.fase == 1:
            self.rect.y += 2
            if self.maximum == self.rect.y:
                self.fase = 0

