import pygame
from vector import Vector
from math import sqrt
from pygame.locals import RLEACCEL
from config import *


class Player(pygame.sprite.Sprite):

    def __init__(self, config):
        super(Player, self).__init__()
        # Set player sprite
        self.surf = pygame.transform.scale(pygame.image.load(config["IMG"]), (75, 100))
        self.surf = self.surf.convert()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)

        # Set player boundaries
        self.rect = self.surf.get_rect()
        self.interactive_border = self.rect

        # Init player attributes
        self.inventory = None
        self.config = config
        self.speed = config["SPEED"]

    def update(self, pressed, entities):
        # Remove self from entities
        entities.remove(self)
        x = 0
        y = 0

        # Check keys pressed
        if pressed[self.config["RIGHT"]]:
            # Right pressed
            x += self.speed
        if pressed[self.config["LEFT"]]:
            # Left Pressed
            x -= self.speed
        if pressed[self.config["UP"]]:
            # Up pressed
            y -= self.speed
        if pressed[self.config["DOWN"]]:
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
            if self.rect.colliderect(entity.interactive_border) and pressed[self.config["USE"]]:
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
        if self.rect.x > SCREEN_WIDTH - 50:# width: # TODO add player attributes width, height
            self.rect.x = SCREEN_WIDTH - 50
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > SCREEN_HEIGHT - 50:# height:
            self.rect.y = SCREEN_HEIGHT - 50