import pygame
from Projectile import projectile
from pygame.locals import *
bullet_size = 5
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill('red')

        self.rect = self.image.get_rect(topright=pos)

        self.speed = 3
        self.health = 100
        self.max_health = 100
        self.attack = 10

        self.right = False
        self.left = False
        self.all_projectiles = pygame.sprite.Group()


    def launch_projectile(self):
        self.all_projectiles.add(projectile(self))
    def get_input(self):
        self.x = 0
        self.y = 0
        bool = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x = -self.speed
            self.left = True
            self.right = False
            print("left")
        if keys[pygame.K_RIGHT]:
            self.x = self.speed
            self.right = True
            self.left = False
            print("right")
        if keys[pygame.K_UP]:
            self.y = -self.speed
            print("up")
        if keys[pygame.K_DOWN]:
            self.y = self.speed
            print("down")


        #if keys[pygame.K_SPACE]:
         #   self.launch_projectile()
          #  print("space")




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



            # Met à jour l'interface utilisateur, le jeu, etc.
            # Vous devrez mettre ceci dans votre propre boucle de jeu





