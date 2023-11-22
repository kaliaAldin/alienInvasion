import pygame


class Flight():
    def __init__(self, ai_setting, screen):
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load("images/fighter.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.top = float(self.rect.top)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.top -= self.ai_setting.speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.top += self.ai_setting.speed_factor

        self.rect.centerx = self.center
        self.rect.top = self.top


    def draw(self):
        self.screen.blit(self.image, self.rect)


