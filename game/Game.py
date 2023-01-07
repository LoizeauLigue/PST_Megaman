import pygame
from Projectile import projectile
from Player import Player
from Setting import *



class Game:
    def __init__(self):
        self.player = Player((100, 100))