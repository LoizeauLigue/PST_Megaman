import pygame
from Tile import Tile


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 5
        self.gravity = 4

    def update(self, x_shift):
       # self.rect.x += x_shift
        self.move()

    def move (self):
        self.rect.x -= self.speed
        self.rect.y += self.gravity



    def reversed(self):
        self.speed *= -1


    def shoot(self):
        self.all_projectiles.add(projectile(self, self.right))

