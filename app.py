import pygame
from pygame.sprite import Group
import sys
from setting import Settings
from flight import Flight
import game_function as gf

ai_setting = Settings()


def run_game():
    # initialising pygame
    pygame.init()
    # setting a display
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Game for IOF")
    airplane = Flight(ai_setting,screen)
    bullets = Group()

    while True:
        gf.check_events( ai_setting , screen , airplane ,bullets)
        airplane.update()
        bullets.update()
        gf.update_screen(ai_setting,screen,airplane ,bullets)

        pygame.display.flip()


run_game()
