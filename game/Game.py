import pygame
from Projectile import projectile
from Player import Player



class Game:
    def __init__(self):
        self.player = Player((0, 0))