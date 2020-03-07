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

    def update(self, pressed, entities):
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

        old_x = self.rect.x
        new_x = self.rect.x + x
        old_y = self.rect.y
        new_y = self.rect.y + y

        # Update position
        self.rect.x = new_x
        if pygame.sprite.spritecollide(self, entities, False):
            # Changing x caused collision
            self.rect.x = old_x

        self.rect.y = new_y
        if pygame.sprite.spritecollide(self, entities, False):
            # Changing y caused collision
            self.rect.y = old_y