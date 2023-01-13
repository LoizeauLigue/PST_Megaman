import pygame
from Tile import Tile
from Projectile import shoot_ennemi
from support import import_folder
import time


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # animation
        self.import_player_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['classic'][self.frame_index]
        self.status = 'classic'
        self.rect = self.image.get_rect(topleft=pos)
        # detect contact
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        # where the enemy is looking
        # self.right = 0
        # movement of enemy
        self.speed = 5
        self.health = 10
        self.health_timer = 10
        self.health_timer_max = 10
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.jump_speed = -10
        self.project = pygame.sprite.Group()
        self.right = False
        self.time = time.time()

    def update(self, x_shift, screen):
        self.move(x_shift)
        self.launch_projectile()
        self.update_project()
        self.project.draw(screen)
        self.animate()

    def update_project(self):
        for proj in self.project.sprites():
            proj.update()

    def move(self, x_shift):
        # self.rect.x -= self.speed
        # self.rect.y += self.gravity
        self.rect.x += x_shift
        self.direction.x = -0.5
        self.apply_gravity()

        # self.jump()
        # print("up")

    def jump(self):
        self.direction.y = self.jump_speed

    def reversed(self):
        self.right = not self.right

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def launch_projectile(self):
        if time.time() + 2 > self.time:
            shoot = shoot_ennemi(self)
            self.project.add(shoot)
            self.time = time.time() + 3

    def modify_speed(self, speed):
        for shoot in self.project:
            shoot.speed = speed

    def import_player_assets(self):
        player_path = '../game/Resources/hoohoo/'
        self.animations = {'classic': []}
        for animation in self.animations.keys():
            fullpath = player_path + animation
            self.animations[animation] = import_folder(fullpath)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        if self.right:
            self.image = pygame.transform.flip(animation[int(self.frame_index)], True, False)
        else:
            self.image = animation[int(self.frame_index)]

        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)
    def health_bar_decrease(self,damage):
        #decresing the health
        if self.health_timer <= 0:
            self.health_timer = self.health_timer_max
            self.health -= damage