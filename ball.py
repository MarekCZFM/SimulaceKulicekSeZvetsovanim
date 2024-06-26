import numpy as np
import math
import pygame

class Ball:
    def __init__(self, x, y, radius, color, width, velocity, acceleration):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color  # Example color, red
        self.width = width
        self.velocity = velocity
        self.acceleration = acceleration

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, self.width)

    def check_for_collisions_with_circle(self, secondBall):
        biggerBall = self if (self.radius > secondBall.radius) else secondBall
        smallerBall = self if (self.radius <= secondBall.radius) else secondBall
        x = max(self.x, secondBall.x) - min(self.x, secondBall.x)
        y = max(self.y, secondBall.y) - min(self.y, secondBall.y)
        distance = math.sqrt(x ** 2 + y ** 2)
        return biggerBall.radius - distance - biggerBall.width // 2 - smallerBall.radius - smallerBall.width // 2 <= 0

    def resolve_collision(self, secondBall):
        x_diff = self.x - secondBall.x
        y_diff = self.y - secondBall.y
        distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
        overlap = self.radius + secondBall.radius - distance

        if overlap > 0:
            # Correct positions
            correction_vector = np.array([x_diff, y_diff]) / distance * overlap
            self.x += correction_vector[0]
            self.y += correction_vector[1]

            # Calculate normal and tangent vectors
            normal = np.array([x_diff, y_diff]) / distance
            tangent = np.array([-normal[1], normal[0]])

            # Decompose velocity vectors into normal and tangential components
            self_velocity_normal = np.dot(self.velocity, normal)
            self_velocity_tangent = np.dot(self.velocity, tangent)
            secondBall_velocity_normal = np.dot(secondBall.velocity, normal)
            secondBall_velocity_tangent = np.dot(secondBall.velocity, tangent)

            # Swap the normal components
            self.velocity = tangent * self_velocity_tangent + normal * secondBall_velocity_normal
            secondBall.velocity = tangent * secondBall_velocity_tangent + normal * self_velocity_normal