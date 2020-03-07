import pygame
from vector import Vector
from math import sqrt
from config import *


class Player(pygame.sprite.Sprite):

    def __init__(self, controls):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 128, 255))
        self.rect = self.surf.get_rect()
        self.interactive_border = self.rect
        self.inventory = None
        self.controls = controls
        self.speed = 10

    def update(self, pressed, entities):
        # Remove self from entities
        entities.remove(self)
        x = 0
        y = 0

        # Check keys pressed
        if pressed[self.controls["RIGHT"]]:
            # Right pressed
            x += self.speed
        if pressed[self.controls["LEFT"]]:
            # Left Pressed
            x -= self.speed
        if pressed[self.controls["UP"]]:
            # Up pressed
            y -= self.speed
        if pressed[self.controls["DOWN"]]:
            # Down pressed
            y += self.speed

        # Entity collision
        self.entityCollision(entities, x, y)
        self.borderCollisionCheck()
        self.entityInteraction(entities, pressed)
        entities.add(self)

        # Display Inventory
        if self.inventory is not None:
            self.inventory.update(self.rect.x, self.rect.y, self.surf.get_height(), self.surf.get_width())

    def entityInteraction(self, entities, pressed):
        for entity in entities:
            if self.rect.colliderect(entity.interactive_border) and pressed[self.controls["USE"]]:
                entity.interact(self)

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