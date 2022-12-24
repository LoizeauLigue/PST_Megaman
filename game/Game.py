import pygame
from Projectile import projectile
from Player import Player
from Stage import Stage


class Game:
    def __init__(self):
        self.player = Player((100, 300))