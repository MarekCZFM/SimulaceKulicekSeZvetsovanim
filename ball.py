import pygame

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (255, 0, 0)  # Example color, red

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)