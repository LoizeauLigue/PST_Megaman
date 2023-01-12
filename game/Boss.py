import pygame
import time
from Projectile import *


class Boss(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((130, 150))
        self.image.fill('blue')
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 5
        self.direction = pygame.math.Vector2(0, 0)
        #self.gravity = 0.8
        self.jump_speed = -10
        self.tire = pygame.sprite.Group()
        self.time = time.time()
        self.damage = 2
        bool = True
        self.facing = 1
        self.delay = 3
        self.health = 300

    def update(self, x_shift, screen):
        self.phase1(x_shift,screen)
        self.phase2(x_shift,screen)
        self.phase3(x_shift,screen)



    def move1(self, x_shift):

        if self.rect.y > 100 and self.facing == 1:
            self.rect.y -= self.speed
            self.rect.x += x_shift
            print(self.facing)
            print(self.rect.y)
            if self.rect.y < 100:
                self.facing = 0
        elif self.facing == 0:
            self.rect.y += self.speed
            self.rect.x += x_shift
            if self.rect.y > 400:
                self.facing = 1
                self.health -= 50

    def launch_projectile1(self):
        self.delay = 3
        if time.time() + 2 > self.time:
            shoot = projectile_boss(self,self.rect.x,self.rect.y+80,1)

            self.tire.add(shoot)

            self.time = time.time() + self.delay

    def phase1(self,x_shift,screen):
        if self.health > 200:
            self.move1(x_shift)
            self.launch_projectile1()
            self.tire.update()
            self.tire.draw(screen)

    def move2(self, camera_x):

        if self.facing == 0:
            self.rect.x += self.speed
            if self.rect.x > 400:
                self.facing = 1
                self.health -= 50
                print(self.facing)
        elif self.facing == 1:
            self.rect.y += self.speed
            if self.rect.y > 400:
                self.facing = 2
        elif self.facing == 2:
            self.rect.x -= self.speed
            if self.rect.x < 100:
                self.facing = 3
        elif self.facing == 3:
            self.rect.y -= self.speed
            if self.rect.y < 100:
                self.facing = 0

        #self.health -= 50
        print(self.facing)


    def launch_projectile2(self):
        self.delay = 2
        if time.time() + 1.6 > self.time:
            shoot = projectile_boss(self,self.rect.x,self.rect.y+80,1)
            shoot2 = projectile_boss(self,self.rect.x,self.rect.y+80,-1)

            self.tire.add(shoot)
            self.tire.add(shoot2)

            self.time = time.time() + self.delay






    def phase2(self,x_shift,screen):
        if self.health > 100 and self.health <= 200:
            self.move2(x_shift)
            self.launch_projectile2()
            self.tire.update()
            self.tire.draw(screen)



    def phase3(self,x_shift,screen):
        if self.health <= 100:
            self.move3(x_shift)
            self.launch_projectile3()
            self.tire.update()
            self.tire.draw(screen)






    def move3(self, x_shift):
        print(self.rect.y)
        print(self.facing)

        if self.rect.y > 100 and self.facing == 0:
            self.rect.y -= self.speed
            self.rect.x += x_shift
            print(self.facing)
            print(self.rect.y)
            if self.rect.y < 100:
                self.facing = 1
        elif self.facing == 1:
            self.rect.y += self.speed
            self.rect.x += x_shift
            if self.rect.y > 400:
                self.facing = 0
                self.health -= 50


    def launch_projectile3(self):
        self.delay = 1
        if time.time() +0.8 > self.time:
            shoot = projectile_boss(self,self.rect.x,self.rect.y+80,1)
            shoot2 = projectile_boss(self,self.rect.x,self.rect.y+80,-1)
            shoot3 = projectile_boss(self,self.rect.x,self.rect.y+40,1)
            shoot4 = projectile_boss(self,self.rect.x,self.rect.y+40,-1)
            shoot5 = projectile_boss(self,self.rect.x,self.rect.y+120,1)
            shoot6 = projectile_boss(self,self.rect.x,self.rect.y+120,-1)

            self.tire.add(shoot)
            self.tire.add(shoot2)
            self.tire.add(shoot3)
            self.tire.add(shoot4)
            self.tire.add(shoot5)
            self.tire.add(shoot6)

            self.time = time.time() + self.delay











