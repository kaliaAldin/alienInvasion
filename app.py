import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (255,0,0)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
        screen.fill(bg_color)


run_game()