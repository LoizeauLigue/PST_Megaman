import pygame
from sys import exit


class projectile(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.image = pygame.image.load('Resources/megaman/comet.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.player = player

        self.rect.x = player.rect.x + 30
        self.rect.y = player.rect.y + 10
        self.speed = 14

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.speed
        if self.rect.x > 1000:
            self.remove()


class projectile_enemie(pygame.sprite.Sprite):
    def __init__(self,enemy):
        super().__init__()
        self.image = pygame.image.load('Resources/megaman/comet.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.enemy = enemy

        self.rect.x = enemy.rect.x + 30
        self.rect.y = enemy.rect.y + 10
        self.speed = 14

    def remove(self):
        self.enemy.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.speed









