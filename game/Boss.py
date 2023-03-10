import pygame
import time
from Projectile import *
from support import import_folder

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # animation
        self.import_player_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['totaly'][self.frame_index]
        self.status = 'totaly'
        self.rect = self.image.get_rect(topleft=pos)
        # detect contact
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        # where the enemy is looking
        self.right = 0

        self.speed = 5
        self.direction = pygame.math.Vector2(0, 0)
        #self.gravity = 0.8
        self.jump_speed = -10
        self.tire = pygame.sprite.Group()
        self.time = time.time()
        self.damage = 2
        bool = True
        self.facing = 1
        self.delay = 3
        self.health = 300
        self.health_timer = 5
        self.health_timer_max = 5
        self.memory_position_x = self.rect.x
        self.memory_position_y = self.rect.y
        self.old_hp = self.health
        self.count_deplacement = 0


    def health_bar_decrease(self,damage):
        #decresing the health
        if self.health_timer <= 0:
            self.health_timer = self.health_timer_max
            self.health -= damage

    def update(self, x_shift, screen):
        self.animate()
        self.phase1(x_shift, screen)
        self.phase2(x_shift, screen)
        self.health_bar(screen)
        #self.phase3(x_shift, screen)
        self.old_hp = self.health

    def move1(self, x_shift):
        if self.facing == 1:
            self.rect.y -= self.speed
            self.rect.x += x_shift
            if self.rect.y < 100: # haut
                self.facing = 0
        elif self.facing == 0:
            self.rect.y += self.speed
            self.rect.x += x_shift
            if self.rect.y > 350: # bas
                self.facing = 1
                # self.health -= 10

    def launch_projectile1(self):
        self.delay = 3
        if self.right == 1:
            input_right = -1
        else:
            input_right = 1
        if time.time() + 2 > self.time:
            shoot = projectile_boss(self, self.rect.x, self.rect.y+8, input_right)
            self.tire.add(shoot)
            self.time = time.time() + self.delay

    def update_project(self):
        for proj in self.tire.sprites():
            proj.update()

    def phase1(self, x_shift, screen):
        if self.health > 200:
            self.move1(x_shift)
            self.launch_projectile1()
            self.update_project()
            self.tire.draw(screen)

    def move2(self, x_shift):
        if self.facing == 0:
            if self.count_deplacement != 50:
                self.rect.x += self.speed
                self.rect.x += x_shift
                self.count_deplacement += 1
            else:
                self.count_deplacement = 0
                self.facing = 1
        elif self.facing == 1:
            self.rect.y += self.speed
            self.rect.x += x_shift
            if self.rect.y > 350: # bas
                self.facing = 2
        elif self.facing == 2:
            if self.count_deplacement != 50:
                self.rect.x -= self.speed
                self.rect.x += x_shift
                self.count_deplacement += 1
            else:
                self.count_deplacement = 0
                self.facing = 3
        elif self.facing == 3:
            self.rect.y -= self.speed
            self.rect.x += x_shift
            if self.rect.y < 100: # haut
                self.facing = 0

    def launch_projectile2(self):
        self.delay = 2
        if self.right == 1:
            input_right = -1
        else:
            input_right = 1
        if time.time() + 1.6 > self.time:
            shoot = projectile_boss(self, self.rect.x, self.rect.y+8, input_right)
            shoot2 = projectile_boss(self, self.rect.x, self.rect.y+30, input_right)
            self.tire.add(shoot)
            self.tire.add(shoot2)
            self.time = time.time() + self.delay


    def phase2(self, x_shift, screen):
        if self.health <= 200:
            self.move2(x_shift)
            self.launch_projectile2()
            self.update_project()
            self.tire.draw(screen)

    def phase3(self, x_shift, screen):
        if self.health <= 100:
            self.move3(x_shift)
            self.launch_projectile3()
            self.update_project()
            self.tire.draw(screen)

    def move3(self, x_shift):

        if self.rect.y > 100 and self.facing == 0:
            self.rect.y -= self.speed
            self.rect.x += x_shift
            if self.rect.y < 100:
                self.facing = 1
        elif self.facing == 1:
            self.rect.y += self.speed
            self.rect.x += x_shift
            if self.rect.y > 400:
                self.facing = 0
                self.health -= 10

    def launch_projectile3(self):
        self.delay = 1
        if time.time() + 0.8 > self.time:
            shoot = projectile_boss(self,self.rect.x,self.rect.y+80,1)
            shoot2 = projectile_boss(self,self.rect.x,self.rect.y+80,-1)
            shoot3 = projectile_boss(self,self.rect.x,self.rect.y+40,1)
            shoot4 = projectile_boss(self,self.rect.x,self.rect.y+40,-1)
            shoot5 = projectile_boss(self,self.rect.x,self.rect.y+120,1)
            shoot6 = projectile_boss(self,self.rect.x,self.rect.y+120,-1)

            self.tire.add(shoot)
            self.tire.add(shoot2)
            self.tire.add(shoot3)
            self.tire.add(shoot4)
            self.tire.add(shoot5)
            self.tire.add(shoot6)

            self.time = time.time() + self.delay

    def import_player_assets(self):
        player_path = '../game/Resources/boss/'
        self.animations = {'idle': [], 'open': [], 'totaly': []}
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



    def health_bar(self,screen):
        # display the health bar
        pygame.draw.rect(screen, (60, 63, 60), [650, 25, 300, 25])
        pygame.draw.rect(screen, (255, 0, 0), [650, 25, self.health, 25])



