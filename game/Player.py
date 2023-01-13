import pygame
from Projectile import projectile
from support import import_folder
from pygame.locals import *
import time
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
        self.press_down_true = 0
        self.timer_power_shot = 200
        self.timer_power_shot_max = 200
        # movement of player
        self.speed = 5
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.jump_speed = -15
        self.all_projectiles = pygame.sprite.Group()
        self.right = True
        self.health = 10
        self.health_timer = 50
        self.health_timer_max = 50
        self.health_timer_hitposition_right = 0
        self.max_health = 10
        self.time = time.time()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def launch_projectile(self, is_big):

        self.all_projectiles.add(projectile(self, is_big))

    def set_projectile_speed(self, speed):
        for projectile in self.all_projectiles:
            projectile.speed = speed

    def get_input(self):

        bool = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.right = False
            self.set_projectile_speed(12)

            #print("left")
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.right = True
            self.set_projectile_speed(12)

            #print("right")
        else:
            self.direction.x = 0
            self.set_projectile_speed(12)


        if keys[pygame.K_UP] and self.on_ground:
            self.jump()
            #print("up")
        if time.time() + 2 > self.time and keys[pygame.K_BACKSPACE]:
            self.health_bar_decrease(1)
            self.time = time.time() + 3
            #print("space")



    def update(self,screen):
        self.draw(screen)
        self.get_input()
        self.get_status()
        self.animate()

    def import_player_assets(self):
        player_path = '../game/Resources/megaman/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'idleandshoot': [], 'runandshoot': [], 'jumpandshoot': [], 'hurt': []}
        for animation in self.animations.keys():
            fullpath = player_path + animation
            self.animations[animation] = import_folder(fullpath)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        if self.status == 'hurt':
            if self.health_timer_hitposition_right:
                self.image = animation[int(self.frame_index)]
            else:
                self.image = pygame.transform.flip(animation[int(self.frame_index)], True, False)
        elif self.right:
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
        if self.health_timer >= 1:
            self.status = 'hurt'
            self.is_shooting_cooldown_animation = 70
            self.is_shooting = False
        else:
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

    def shooting_move(self):
        for projectile in self.all_projectiles:
            projectile.move()



    def health_bar(self,screen):
        # display the health bar
        pygame.draw.rect(screen, (60, 63, 60), [35, 25, 250, 25])
        pygame.draw.rect(screen, (111, 210, 46), [35, 25, 250 - (25* (10 - self.health)), 25])


    def health_bar_decrease(self,damage):
        #decresing the health
        if self.health_timer <= 0:
            self.health_timer = self.health_timer_max
            self.health_timer_hitposition_right = self.right
            self.health -= damage
            if self.health <= 0:
                self.close_window()

    def draw(self, screen):
        self.health_bar(screen)



    def close_window(self):
        pygame.quit()
        quit()

    def large_shoot(self):
        self.all_projectiles.add(large_projectile(self))
        self.is_shooting = True

