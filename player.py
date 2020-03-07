import pygame
from math import sqrt
from conifg import *


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

        # Check the border
        self.borderCollisionCheck()

    def borderCollisionCheck(self):

        # Basic border collision detection
        if self.position.x < 0:
            self.position.x = 0
        if self.position.x > SCREEN_WIDTH - 60 :# width: # TODO add player attributes width, height
            self.position.x = SCREEN_WIDTH - 60
        if self.position.y < 0:
            self.position.y = 0
        if self.position.y > SCREEN_HEIGHT - 60 :# height:
            self.position.y = SCREEN_HEIGHT - 60


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position.x, self.position.y, 60, 60))


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


