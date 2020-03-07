import pygame


class Item:

    def __init__(self, surface):
        self.surf = surface


class Iron(Item):

    def __init__(self):
        super().__init__(pygame.Surface((10, 10)))
        self.surf.fill((50, 50, 50))