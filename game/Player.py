import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = 5
        self.x = 0
        self.y = 0
        super().__init__()

    def get_input(self):
        self.x = 0
        self.y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x = -self.speed
            print("left")
        if keys[pygame.K_RIGHT]:
            self.x = self.speed
            print("right")
        if keys[pygame.K_UP]:
            self.y = -self.speed
            print("up")
        if keys[pygame.K_DOWN]:
            self.y = self.speed
            print("down")

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.get_input()
        self.rect.x += self.x
        self.rect.y += self.y

    def des_update(self):
        if self.x:
            self.rect.x -= self.x
            self.x = 0
        if self.y:
            self.rect.y -= self.y
            self.y = 0
