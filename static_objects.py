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