import pygame
from Items import *


class StaticObject(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, interactive_border_radius=0):
        super(StaticObject, self).__init__()

        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(x=y, y=x)

        self.interactive_border = pygame.Rect(self.rect.left - interactive_border_radius,
                                              self.rect.top - interactive_border_radius,
                                              self.rect.width + 2 * interactive_border_radius,
                                              self.rect.height + 2 * interactive_border_radius)

    def interact(self, player):
        pass


class Furnace(StaticObject):

    def __init__(self):
        super(Furnace, self).__init__(300, 300, 200, 200, 15)
        self.surf.fill((255, 165, 0))
        self.inventory = None
        self.finished = False
        self.burnTime = 0

    def interact(self, player):
        if player.inventory is not None and player.inventory.smeltable and self.inventory is None:
            # Update the inventories
            self.inventory = player.inventory
            player.inventory = None

            # Set the furnace to burning
            self.surf.fill((255, 0, 0))
            self.burnTime = self.inventory.smelt_time
        elif player.inventory is None and self.finished:
            self.finished = False
            player.inventory = self.inventory
            self.inventory = None

    def update(self):
        if self.burnTime > 0:
            self.burnTime -= 1

        if self.burnTime == 0 and self.inventory is not None and not self.finished:
            self.surf.fill((255, 165, 0))
            self.inventory = self.inventory.output
            self.finished = True


class CollectionPoint(StaticObject):

    def __init__(self):
        super(CollectionPoint, self).__init__(800, 100, 100, 100, 15)
        self.surf.fill((0, 0, 255))

    def interact(self, player):
        if player.inventory is None:
            player.inventory = Iron()


class Wall(StaticObject):

    def __init__(self):
        super(Wall, self).__init__(50, 50, 50, 50)
        self.surf.fill((255, 0, 0))
