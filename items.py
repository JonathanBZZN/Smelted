import pygame
from pygame.locals import RLEACCEL


class Item(pygame.sprite.Sprite):

    def __init__(self, width, height, smeltable=False, hammerable=False):
        super(Item, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(x=0, y=0)

        # Smelting attributes
        self.smeltable = smeltable
        self.hammerable = hammerable

    def update(self, x, y, player_height, player_width):
        self.rect.x = x + (player_width / 2) - (self.surf.get_width() / 2)
        self.rect.y = y - (self.surf.get_height() * 2)


class Iron(Item):

    def __init__(self):
        super(Iron, self).__init__(50, 25, smeltable=True)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/ingot.png"), (50, 37))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)


class Steel(Item):

    def __init__(self):
        super(Steel, self).__init__(50, 25, hammerable=True)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/hot_steel.png"), (50, 37))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)
