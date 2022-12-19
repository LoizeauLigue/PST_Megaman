import pygame
from pygame.locals import *
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 10
        self.visible = True
        self.walkRight = [pygame.image.load('Resources/megaman/walk_1.png'), pygame.image.load('Resources/megaman/walk_2.png'), pygame.image.load('Resources/megaman/walk_3.png')]
        self.walkLeft = [pygame.image.load('Resources/megaman/walk_1.png'), pygame.image.load('Resources/megaman/walk_2.png'), pygame.image.load('Resources/megaman/walk_3.png')]
        self.idle = [pygame.image.load('Resources/megaman/idle.png'),