import pygame
import os
pygame.init()
pygame.font.init()

WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders game")

space = pygame.transform.scale(pygame.image.load("GD2-L6-oops-space-invaders/space.png"), (WIDTH, HEIGHT))

def Drawwindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    screen.blit(space, (0, 0))
    pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Call the Drawwindow function here
    Drawwindow(None, None, None, None, None, None)

pygame.quit()
