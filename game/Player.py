import pygame
from Projectile import projectile
from support import import_folder
from pygame.locals import *

bullet_size = 5


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        #animation
        self.import_player_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.status = 'idle'
        self.rect = self.image.get_rect(topleft=pos)
        # detect contact
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        # where the player is looking
        self.right = True
        self.is_shooting = False
        self.is_shooting_cooldown_animation = 5
        # movement of player
        self.speed = 5
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.jump_speed = -15
        self.all_projectiles = pygame.sprite.Group()
        self.right = True

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def launch_projectile(self):
        self.all_projectiles.add(projectile(self))

    def get_input(self):
        bool = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.right = False

            print("left")
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.right = True

            print("right")
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.on_ground:
            self.jump()
            print("up")

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()

    def import_player_assets(self):
        player_path = '../game/Resources/megaman/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'idleandshoot': [], 'runandshoot': [], 'jumpandshoot': []}
        for animation in self.animations.keys():
            fullpath = player_path + animation
            self.animations[animation] = import_folder(fullpath)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        if self.right:
            self.image = animation[int(self.frame_index)]
        else:
            self.image = pygame.transform.flip(animation[int(self.frame_index)], True, False)

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

    def get_status(self):
        if self.is_shooting:
            if self.is_shooting_cooldown_animation == 0:
                self.is_shooting_cooldown_animation = 70
                self.is_shooting = False
            else:
                self.is_shooting_cooldown_animation -= 1
        if not self.on_ground:
            if self.is_shooting:
                self.status = 'jumpandshoot'
            else:
                self.status = 'jump'
        else:
            if self.direction.x != 0:
                if self.is_shooting:
                    self.status = 'runandshoot'
                else:
                    self.status = 'run'
            else:
                if self.is_shooting:
                    self.status = 'idleandshoot'
                else:
                    self.status = 'idle'
