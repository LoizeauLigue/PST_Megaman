import pygame
from Projectile import projectile
from pygame.locals import *
bullet_size = 5


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill('red')

        self.rect = self.image.get_rect(topleft=pos)

        self.speed = 5
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.jump_speed = -10
        self.all_projectiles = pygame.sprite.Group()
        self.right = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def launch_projectile(self):
        self.all_projectiles.add(projectile(self))

    def get_input(self):
        bool = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.right = False

            print("left")
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.right = True

            print("right")
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.jump()
            print("up")

    def update(self):
        self.get_input()










