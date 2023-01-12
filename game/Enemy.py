import pygame
from Tile import Tile
from Projectile import shoot_ennemi
import time

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
        self.project = pygame.sprite.Group()
        self.right = False
        self.time = time.time()

    def update(self, x_shift,screen):
        self.move(x_shift)
        self.launch_projectile()
        self.project.update()
        self.project.draw(screen)

    def move (self, x_shift):
        #self.rect.x -= self.speed
        #self.rect.y += self.gravity
        self.rect.x += x_shift
        self.direction.x = -0.5
        self.apply_gravity()

        #self.jump()
        #print("up")

    def jump(self):
        self.direction.y = self.jump_speed

    def reversed(self):
        self.right = not self.right

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    def launch_projectile(self):
        if time.time() + 2 > self.time:
            shoot = shoot_ennemi(self)
            self.project.add(shoot)
            self.time = time.time() +3

    def modify_speed(self, speed):
        for shoot in self.project:
            shoot.speed = speed












