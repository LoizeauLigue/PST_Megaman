import pygame
from Tile import Tile
from Projectile import projectile_enemie


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 4
        self.all_projectiles = pygame.sprite.Group()

    def update(self, x_shift):
       # self.rect.x += x_shift
       for projectile_enemie in self.all_projectiles:
           projectile_enemie.move()
           self.launch_projectile()
           print("shoot2")

       self.move()

    def move (self):
        self.direction.x += 1
        self.rect.y += self.gravity

    def launch_projectile(self):
        self.all_projectiles.add(projectile_enemie(self))
        print("shoot")

    def reversed(self):
        pass


    def shoot(self):
        self.all_projectiles.add(projectile(self, self.right))

