import pygame
from Player import Player
from Tile import Tile
from Tile import Tile_mouv
from Setting import title_size, screen_width, screen_height, level_map
from Game import Game
from Enemy import Enemy
from Projectile import projectile
from Boss import Boss


class Stage:
    def __init__(self, level_data, surface):
        self.tiles = None
        self.player = None
        self.enemies = None
        self.boss = None
        self.tiles_mouv = None
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.boss = pygame.sprite.Group()
        self.tiles_mouv = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * title_size
                y = row_index * title_size
                if cell == 'X':
                    self.tiles.add(Tile((x, y), title_size))
                if cell == 'P':
                    self.player.add(Player((x, y)))
                if cell == 'E':
                    self.enemies.add(Enemy((x, y)))
                if cell == 'B':
                    self.boss.add(Boss((x, y), title_size))
                if cell == 'C':
                    self.tiles_mouv.add(Tile_mouv((x, y)))

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

    def display(self, screen):
        self.tiles.draw(self.display_surface)
        self.tiles_mouv.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.enemies.draw(self.display_surface)
        self.boss.draw(self.display_surface)

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def horizontal_collision_enemy(self):
        for sprite_enemy in self.enemies.sprites():
            sprite_enemy.rect.x += sprite_enemy.direction.x * sprite_enemy.speed
            for sprite_tiles in self.tiles.sprites():
                if sprite_tiles.rect.colliderect(sprite_enemy.rect):
                    if sprite_enemy.direction.x < 0:
                        sprite_enemy.rect.left = sprite_tiles.rect.right
                        sprite_enemy.on_left = True
                        self.current_x = sprite_enemy.rect.left
                    elif sprite_enemy.direction.x > 0:
                        sprite_enemy.rect.right = sprite_tiles.rect.left
                        sprite_enemy.on_right = True
                        self.current_x = sprite_enemy.rect.right
            if sprite_enemy.on_left and (sprite_enemy.rect.left < self.current_x or sprite_enemy.direction.x >= 0):
                sprite_enemy.on_left = False
            if sprite_enemy.on_right and (sprite_enemy.rect.right > self.current_x or sprite_enemy.direction.x <= 0):
                sprite_enemy.on_right = False

    def vertical_collision_enemy(self):
        for sprite_enemy in self.enemies.sprites():
            sprite_enemy.apply_gravity()
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(sprite_enemy.rect):
                    if sprite_enemy.direction.y > 0:
                        sprite_enemy.rect.bottom = sprite.rect.top
                        sprite_enemy.direction.y = 0
                        sprite_enemy.on_ground = True
                    elif sprite_enemy.direction.y < 0:
                        sprite_enemy.rect.top = sprite.rect.bottom
                        sprite_enemy.direction.y = 0
                        sprite_enemy.on_ceiling = True
            if sprite_enemy.on_ground and sprite_enemy.direction.y < 0 or sprite_enemy.direction.y > 1:
                sprite_enemy.on_ground = False
            if sprite_enemy.on_ceiling and sprite_enemy.direction.y > 0:
                sprite_enemy.on_ceiling = False

    def collision_enemy_player(self):
        player = self.player.sprite
        if player.health_timer >= 1:
            player.health_timer -= 1
        if player.health_timer <= 0:
            for sprite_enemy in self.enemies.sprites():
                if player.rect.colliderect(sprite_enemy.rect):
                    player.health_bar_decrease(1)
                for sprite_projectile in sprite_enemy.project.sprites():
                    if player.rect.colliderect(sprite_projectile.rect):
                        player.health_bar_decrease(1)
                        sprite_enemy.project.remove(sprite_projectile)
            for sprite_enemy in self.boss.sprites():
                if player.rect.colliderect(sprite_enemy.rect):
                    player.health_bar_decrease(2)
                for sprite_projectile in sprite_enemy.tire.sprites():
                    if player.rect.colliderect(sprite_projectile.rect):
                        player.health_bar_decrease(2)
                        sprite_enemy.tire.remove(sprite_projectile)

    def collision_player_enemy(self):
        player = self.player.sprite
        for sprite_enemy in self.enemies.sprites():
            #print(sprite_enemy.health)
            if sprite_enemy.health_timer >= 1:
                sprite_enemy.health_timer -= 1
            if sprite_enemy.health_timer <= 0:
                for sprite_projectile in player.all_projectiles.sprites():
                    if sprite_enemy.rect.colliderect(sprite_projectile.rect):
                        if sprite_projectile.is_big_projectile == 1:
                            sprite_enemy.health_bar_decrease(3)
                        else:
                            sprite_enemy.health_bar_decrease(1)
                        player.all_projectiles.remove(sprite_projectile)
                if sprite_enemy.health <= 0:
                    self.enemies.remove(sprite_enemy)

    def collision_player_boss(self):
        player = self.player.sprite
        for sprite_enemy in self.boss.sprites():
            print(sprite_enemy.health)
            if sprite_enemy.health_timer >= 1:
                sprite_enemy.health_timer -= 1
            if sprite_enemy.health_timer <= 0:
                for sprite_projectile in player.all_projectiles.sprites():
                    if sprite_enemy.rect.colliderect(sprite_projectile.rect):
                        if sprite_projectile.is_big_projectile == 1:
                            sprite_enemy.health_bar_decrease(3)
                        else:
                            sprite_enemy.health_bar_decrease(1)
                        player.all_projectiles.remove(sprite_projectile)
                if sprite_enemy.health <= 0:
                    # animation dead
                    self.enemies.remove(sprite_enemy)

    def collision_projectile_tile(self):
        for sprite in self.tiles.sprites():
            for sprite_enemy in self.enemies.sprites():
                for sprite_projectile in sprite_enemy.project.sprites():
                    if sprite_projectile.rect.colliderect(sprite.rect):
                        sprite_enemy.project.remove(sprite_projectile)
            for player in self.player.sprites():
                for sprite_projectile in player.all_projectiles.sprites():
                    if sprite_projectile.rect.colliderect(sprite.rect):
                        player.all_projectiles.remove(sprite_projectile)
            for boss in self.boss.sprites():
                for sprite_projectile in boss.tire.sprites():
                    if sprite_projectile.rect.colliderect(sprite.rect):
                        boss.tire.remove(sprite_projectile)

    def vertical_collision_mouv_tile(self):
        player = self.player.sprite
        for sprite in self.tiles_mouv.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
    def run(self, screen):
        self.tiles.update(self.world_shift)
        self.tiles_mouv.update(self.world_shift)
        self.player.update(screen)
        self.enemies.update(self.world_shift, screen)
        self.boss.update(self.world_shift, screen)
        self.scroll_x()
        # collision
        self.horizontal_collision()
        self.vertical_collision()
        self.vertical_collision_mouv_tile()
        self.horizontal_collision_enemy()
        self.vertical_collision_enemy()
        self.collision_enemy_player()
        self.collision_player_enemy()
        self.collision_player_boss()
        self.collision_projectile_tile()
        for sprite_boss in self.boss.sprites():
            if sprite_boss.health <= 0:
                self.boss.remove(sprite_boss)



