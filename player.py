import pygame
from vector import Vector
from math import sqrt
from conifg import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 128, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed, entities):
        # Remove self from entities
        entities.remove(self)
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

        # Entity collision
        self.entityCollision(entities, x, y)
        self.borderCollisionCheck()
        self.entityInteraction(entities)
        entities.add(self)

    def entityInteraction(self, entities):
        for entity in entities:
            if self.rect.colliderect(entity.interactive_border):
                print("Test")

    def entityCollision(self, entities, x, y):
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

    def borderCollisionCheck(self):

        # Basic border collision detection
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - 60:# width: # TODO add player attributes width, height
            self.rect.x = SCREEN_WIDTH - 60
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > SCREEN_HEIGHT - 60:# height:
            self.rect.y = SCREEN_HEIGHT - 60