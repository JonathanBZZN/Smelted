import pygame
from math import sqrt


class Player:

    def __init__(self):
        self.color = (0, 128, 255)
        self.velocity = Vector()
        self.position = Vector(50, 50)

    def update(self, pressed):
        x = 0
        y = 0

        # Check keys pressed
        if pressed[pygame.K_RIGHT]:
            # Right pressed
            x += 5
        if pressed[pygame.K_LEFT]:
            # Left Pressed
            x -= 5
        if pressed[pygame.K_UP]:
            # Up pressed
            y -= 5
        if pressed[pygame.K_DOWN]:
            # Down pressed
            y += 5

        # Update position
        self.position += Vector(x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position.x, self.position.y, 60, 60))


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


