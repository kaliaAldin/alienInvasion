import pygame
import  sys

pygame.init()
screen = pygame.display.set_mode((1080 , 720))
pygame.display.set_caption("Pygame eample")
running = True

screen_rect = screen.get_rect()
#screen_center = screen_rect.center[0] , screen_rect.center[1]
posX = screen_rect.centerx
posY = screen_rect.centery

image = pygame.image.load("images/fighter.png")


while running:
    gameevents = pygame.event.get()
    mousPos = pygame.mouse.get_pos()
    posX = mousPos[0]
    posY = mousPos[1]


    for event in gameevents:
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    screen.fill('Blue')
    pygame.draw.rect(screen, 'Red', [posX,posY, 50, 50])
    pygame.display.flip()