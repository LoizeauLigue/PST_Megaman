import pygame
from Player import Player
from Tile import Tile
from Setting import title_size , screen_width, screen_height, level_map
from Game import Game

class Stage:
    def __init__(self, level_data, surface):
        self.tiles = None
        self.player = None
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * title_size
                y = row_index * title_size
                if cell == 'X':
                    self.tiles.add(Tile((x, y), title_size))
                if cell == 'P':
                    self.player = Player((x, y))
                    # self.player.add(player_sprite)
    def scroll_x(self):
       player_x = self.player.rect.centerx
       direction_x = self.player.direction.x
       if player_x < 475 and direction_x <0:
            self.world_shift = 6
            self.player.speed = 0
       elif player_x > 475 and direction_x >0:
            self.world_shift = -6
            self.player.speed = 0
       else:
            self.world_shift = 0
            self.player.speed = 5


    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.player.update()
        self.scroll_x()

        #self.player.draw(self.display_surface)




