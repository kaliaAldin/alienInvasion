import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown(event,ai_setting,screen, airplane,bullets):
    if event.key == pygame.K_RIGHT:
        airplane.moving_right = True
    elif event.key == pygame.K_LEFT:
        airplane.moving_left = True
    elif event.key == pygame.K_UP:
        airplane.moving_up = True
    elif event.key == pygame.K_DOWN:
        airplane.moving_down = True
    elif event.key == pygame.K_d:
        if len(bullets) < ai_setting.bullets_allowed:
            right_bullet = Bullet(ai_setting,screen,airplane ,10)

            bullets.add(right_bullet)
    elif event.key == pygame.K_a:
        if len(bullets) < ai_setting.bullets_allowed:

            left_bullet =Bullet(ai_setting,screen,airplane, dx=-20 )
            bullets.add(left_bullet)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup(event, airplane):
    if event.key == pygame.K_RIGHT:
        airplane.moving_right = False
    elif event.key == pygame.K_LEFT:
        airplane.moving_left = False
    elif event.key == pygame.K_UP:
        airplane.moving_up = False
    elif event.key == pygame.K_DOWN:
        airplane.moving_down = False



def check_events(ai_setting, screen ,airplane, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event,ai_setting , screen,airplane, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup(event, airplane)


def update_screen(ai_setting, screen, airplane ,aliens ,bullets):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    airplane.draw()
    aliens.draw(screen)
    pygame.display.flip()

def create_fleet(ai_setting, screen , aliens ):
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    available_space_x = ai_setting.screen_width  - 2 * alien_width
    number_aliens_x = int (available_space_x/(2 * alien_width))
    for alien_number in range(number_aliens_x) :
        alien = Alien(ai_setting,screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

