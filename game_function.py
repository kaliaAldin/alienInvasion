import sys
import pygame


def check_keydown(event, airplane):
    if event.key == pygame.K_RIGHT:
        airplane.moving_right = True
    elif event.key == pygame.K_LEFT:
        airplane.moving_left = True
    elif event.key == pygame.K_UP:
        airplane.moving_up = True
    elif event.key == pygame.K_DOWN:
        airplane.moving_down = True


def check_keyup(event, airplane):
    if event.key == pygame.K_RIGHT:
        airplane.moving_right = False
    elif event.key == pygame.K_LEFT:
        airplane.moving_left = False
    elif event.key == pygame.K_UP:
        airplane.moving_up = False
    elif event.key == pygame.K_DOWN:
        airplane.moving_down = False



def check_events(airplane):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, airplane)

        elif event.type == pygame.KEYUP:
            check_keyup(event, airplane)


def update_screen(ai_setting, screen, airplane):
    screen.fill(ai_setting.bg_color)
    airplane.draw()
