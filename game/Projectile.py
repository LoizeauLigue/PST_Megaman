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
        self.facing = 1
        self.speed = 20

    def update(self):
        self.move_shoot_ennemi()
    def move_shoot_ennemi(self):
        if self.enemy.right:
            self.image = pygame.transform.flip(self.image, False, False)
            self.rect.x += self.speed

        else:
            self.rect.x -= self.speed
            self.image = pygame.transform.flip(self.image, True, False)


class projectile(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.image = pygame.image.load('Resources/megaman/comet.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.player = player
        self.facing = player.right

        self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 2
        self.speed = 6



    def remove(self):
        self.player.all_projectiles.remove(self)


    def move(self):
        if self.facing:
            self.image = pygame.transform.flip(self.image,False ,False)
            self.rect.x += self.speed

        if not self.facing:

            self.rect.x -= self.speed
            self.image = pygame.transform.flip(self.image, True, False)
        #si le tire est trop loin du joueur alors on le supprime
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


    def remove(self):
        self.boss.tire.remove(self)


    def move(self):
        if self.facing==-1:
            self.image = pygame.transform.flip(self.image, False, False)
            self.rect.x += self.speed

        if self.facing==1:
            self.rect.x -= self.speed
            self.image = pygame.transform.flip(self.image, True, False)




    def update(self):
        self.move()


















