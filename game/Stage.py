import pygame


class Stage(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.fillbackground = pygame.Surface(pos)
        color = (244, 164, 96)
        self.fillbackground.fill(color)
        self.background = pygame.image.load('Resources/background/waterfall_1.png')
        self.background_rect = self.background.get_rect()
        self.background_x = 50
        self.background_y = 50
        super().__init__()

    def display(self, screen):
        screen.blit(self.fillbackground, (0, 0))
        screen.blit(self.background, self.background_rect)

    def collision(self):
        print(1)
