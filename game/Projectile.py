import pygame
from sys import exit
import time


class shoot_ennemi(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.image = pygame.image.load('Resources/megaman/comet.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(center=enemy.rect.center)

        self.enemy = enemy
        self.time = time.time()
        self.right = enemy.right
        self.speed = 20
        if self.right == 1:
            self.image = pygame.transform.flip(self.image, False, False)
        else:
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        self.move_shoot_ennemi()

    def move_shoot_ennemi(self):
        if self.right:
            self.rect.x += self.speed

        if not self.right:
            self.rect.x -= self.speed
        # si le tire est trop loin du joueur alors on le supprime
        if self.rect.x - self.enemy.rect.x > 600 and not self.right:
            self.remove()

        if self.rect.x - self.enemy.rect.x < -600 and  self.right:
            self.remove()


class projectile(pygame.sprite.Sprite):
    def __init__(self,player, is_big):
        super().__init__()
        if is_big == 0:
            self.image = pygame.image.load('Resources/megaman/comet.png')
            self.image = pygame.transform.scale(self.image, (20, 20))
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect()
            self.rect.y = player.rect.y + 2
        else:
            self.image = pygame.image.load('Resources/megaman/comet.png')
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect = self.image.get_rect()
            self.rect.y = player.rect.y-26
        self.player = player
        self.facing = player.right
        self.is_big_projectile = is_big
        self.rect.x = player.rect.x
        self.speed = 6
        if self.facing == 1:
            self.image = pygame.transform.flip(self.image, False, False)
        else:
            self.image = pygame.transform.flip(self.image, True, False)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        if self.facing:
            self.rect.x += self.speed

        if not self.facing:
            self.rect.x -= self.speed
        # si le tire est trop loin du joueur alors on le supprime
        if self.rect.x - self.player.rect.x > 450 and self.facing:
            self.remove()

        if self.rect.x - self.player.rect.x < -450 and not self.facing:
            self.remove()


class projectile_boss(pygame.sprite.Sprite):
    def __init__(self,boss,x,y,facing):
        super().__init__()
        self.image = pygame.image.load('Resources/megaman/comet.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(center=(x,y))
        self.boss = boss
        self.time = time.time()
        self.facing = facing
        self.speed = 20
        if self.facing == 1:
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = pygame.transform.flip(self.image, False, False)

    def remove(self):
        self.boss.tire.remove(self)

    def move(self):
        if self.facing:
            self.rect.x -= self.speed

        if not self.facing:
            self.rect.x += self.speed
        # si le tire est trop loin du joueur alors on le supprime
        if self.rect.x - self.boss.rect.x > 600 and not self.facing:
            self.remove()

        if self.rect.x - self.boss.rect.x < -600 and  self.facing:
            self.remove()

    def update(self):
        self.move()













