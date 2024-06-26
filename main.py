import math
import pygame
from pygame.time import Clock
from ball import Ball

SIRKA, VYSKA = 1080//2, 1920//2           # Full HD bylo pro me moc :D
obrazovka = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("My balls")

kruznice = Ball(SIRKA//2, VYSKA//2, 250, "#FFFFFF", 3, (0, 3))
clock = Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    kruznice.draw(obrazovka)

    pygame.display.flip()
    clock.tick(30)