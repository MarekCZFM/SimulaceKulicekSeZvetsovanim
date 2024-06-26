import math
import numpy as np
import pygame
from pygame.time import Clock
from ball import Ball

SIRKA, VYSKA = 1080//2, 1920//2           # Full HD bylo pro me moc :D
obrazovka = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("My balls")

kruznice = Ball(SIRKA//2, VYSKA//2, 250, "#FFFFFF", 3, np.array((0, 0)), np.array((0, 0)))
kruh = Ball(SIRKA//2, VYSKA//2, 50, "#FF0000", 0, np.array((30, 0)), np.array((0, 9.81)))
clock = Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if (kruh.check_for_collisions_with_circle(kruznice)):
        kruh.resolve_collision(kruznice)
    
    kruh.velocity = kruh.velocity + kruh.acceleration
    position = np.array((kruh.x, kruh.y))
    position = position + kruh.velocity
    kruh.x = position[0]
    kruh.y = position[1]

    # Boundary check
    if kruh.x - kruh.radius < 0 or kruh.x + kruh.radius > SIRKA:
        kruh.velocity[0] = -kruh.velocity[0]
    if kruh.y - kruh.radius < 0 or kruh.y + kruh.radius > VYSKA:
        kruh.velocity[1] = -kruh.velocity[1]

    obrazovka.fill ((0, 0, 0))
    kruznice.draw(obrazovka)
    kruh.draw(obrazovka)

    pygame.display.flip()
    clock.tick(30)