import pygame


class Flight():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("images/fighter.png")
        self.image = pygame.transform.scale(self.image , (100 ,100))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def draw(self):
        self.screen.blit(self.image ,self.rect)
