import pygame
from Tile import Tile


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 5
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.jump_speed = -10
        self.all_projectiles = pygame.sprite.Group()
        self.right = False

    def update(self, x_shift):
       # self.rect.x += x_shift
        self.move()

    def move (self):
        #self.rect.x -= self.speed
        #self.rect.y += self.gravity
        self.direction.x = -1
        self.apply_gravity()
        self.right = False
        #self.jump()
        #print("up")

    def jump(self):
        self.direction.y = self.jump_speed

    def reversed(self):
        self.speed *= -1

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def shoot(self):
        self.all_projectiles.add(projectile(self, self.right))

