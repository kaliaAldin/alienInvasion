import pygame
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

    while True:
        gf.check_events(airplane)
        airplane.update()
        gf.update_screen(ai_setting,screen,airplane)

        pygame.display.flip()


run_game()
