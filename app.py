import pygame
from pygame.sprite import Group
import sys
from setting import Settings
from flight import Flight
from alien import Alien
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
    aliens = Group()
    #alien = Alien(ai_setting , screen)
    gf.create_fleet(ai_setting,screen,aliens)

    while True:
        gf.check_events( ai_setting , screen , airplane ,bullets)
        airplane.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0 :
                bullets.remove(bullet)

        gf.update_screen(ai_setting,screen,airplane,aliens ,bullets)

        pygame.display.flip()


run_game()
