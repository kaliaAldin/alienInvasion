import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_setting , screen , flight ,dx):
        super(Bullet,self).__init__()
        self.screen = screen
        #self.rect = pygame.Rect(0,0,ai_setting.bullet_width , ai_setting.bullet_height)
        self.image = pygame.image.load("images/missile.png")
        self.image = pygame.transform.scale(self.image,(ai_setting.bullet_width, ai_setting.bullet_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = flight.rect.centerx + dx
        self.rect.top = flight.rect.top
        self.y = float(self.rect.y)
        #self.color = ai_setting.bullet_color
        self.bullet_speed_factor = ai_setting.bullet_speed_factor
    def update(self, *args, **kwargs):
        self.y -= self.bullet_speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
       # pygame.draw.rect(self.screen,self.color,self.rect)
       self.screen.blit(self.image, self.rect)