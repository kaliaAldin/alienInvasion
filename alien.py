import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self , ai_setting , screen ):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load("images/baby.png")
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
    def draw(self):
        self.screen.blit(self.image , self.rect)