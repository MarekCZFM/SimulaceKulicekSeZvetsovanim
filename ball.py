import math
import pygame

class Ball:
    def __init__(self, x, y, radius, color, width, velocity, acceleration):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color  # Example color, red
        self.width = width
        self.acceleration = acceleration
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width)

    def check_for_collisions_with_circle(self, secondBall):
        biggerBall = max([self, secondBall], key=radius)
        smallerBall = min([self, secondBall], key=radius)
        x = max(self.x, secondBall.x) - min(self.x, secondBall.x)
        y = max(self.y, secondBall.y) - min(self.y, secondBall.y)
        distance = math.sqrt(x ** 2 + y ** 2)
        return biggerBall.radius - biggerBall.width // 2 - smallerBall.radius - smallerBall.width // 2 <= 0