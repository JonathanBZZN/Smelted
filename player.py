import pygame
from vector import Vector
from math import sqrt


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 128, 255))
        self.rect = self.surf.get_rect()

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

        self.rect.move_ip(x, y)