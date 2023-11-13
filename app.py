import pygame
import sys
from setting import Settings
ai_setting = Settings()
def run_game():
    #initialising pygame
    pygame.init()
    #setting a display
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")


    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_setting.bg_color)
        pygame.display.flip()



run_game()