import pygame
from pygame.locals import RLEACCEL
from items import Item


class Sword(Item):

    def __init__(self, width, height, grindable=True):
        super(Sword, self).__init__(width, height, grindable=grindable)

    def sharpen(self):
        pass


class BasicSword(Sword):

    def __init__(self):
        super(BasicSword, self).__init__(50, 25)
        # Initial form
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/sword-1-bad.png"), (50, 50))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)


class SharpBasicSword(Sword):

    def __init__(self):
        super(SharpBasicSword, self).__init__(50, 25, grindable=False)
        # Initial form
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/sword-1-good.png"), (50, 50))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)