import pygame
from Player import Player
from Tile import Tile
from Setting import title_size, screen_width, screen_height, level_map
from Game import Game
from Enemy import Enemy


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
        self.enemies = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * title_size
                y = row_index * title_size
                if cell == 'X':
                    self.tiles.add(Tile((x, y), title_size))
                if cell == 'P':
                    self.player.add(Player((x, y)))
                if cell == 'E':
                    self.enemies.add(Enemy((x, y), title_size))

    def scroll_x(self):
        # player_x = self.player.rect.centerx
        # direction_x = self.player.direction.x
        player_x = self.player.sprite.rect.centerx
        direction_x = self.player.sprite.direction.x
        if player_x < 475 and direction_x < 0:
            self.world_shift = 6
            self.player.sprite.speed = 0
        elif player_x > 475 and direction_x > 0:
            self.world_shift = -6
            self.player.sprite.speed = 0
        else:
            self.world_shift = 0
            self.player.sprite.speed = 5
    def ennemy_collision(self):
        for enemy in self.enemies.sprites():
            if enemy.rect.colliderect(self.player.sprite.rect):
                print("collision")
            #ecrit une fonction qui fait disparaitre le monstre si il touche un mur
    def ennemy_Wall_collision(self):
        for enemy in self.enemies.sprites():
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    #call methode reversed from ennemy
                    enemy.reversed()

                    print("collisionwall")
    def display(self, screen):
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.enemies.draw(self.display_surface)

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        self.tiles.update(self.world_shift)
        self.player.update()
        self.enemies.update(self.world_shift)
        self.scroll_x()
        # collision
        self.horizontal_collision()
        self.vertical_collision()
        self.ennemy_collision()
        self.ennemy_Wall_collision()
