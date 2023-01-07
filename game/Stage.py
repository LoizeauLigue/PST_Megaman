import pygame
from Player import Player
from Tile import Tile
from Setting import title_size
from Game import Game
class Stage:
    def __init__(self,level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * title_size
                y = row_index * title_size
                if cell == 'X':
                    self.tiles.add(Tile((x,y),title_size))
                if cell == 'P':
                    self.player = Player((x,y))
                    self.player.rect.x = x
                    self.player.rect.y = y
    def run(self):
       self.tiles.update(self.world_shift)
       self.tiles.draw(self.display_surface)
