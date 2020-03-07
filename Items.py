import pygame
from pygame.locals import RLEACCEL


class Item(pygame.sprite.Sprite):

    def __init__(self, width, height, smelt_time=0, output=None, smeltable=False):
        super(Item, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(x=0, y=0)

        # Smelting attributes
        self.smelt_time = smelt_time
        self.output = output
        self.smeltable = smeltable

    def update(self, x, y, player_height, player_width):
        self.rect.x = x + (player_width / 2) - (self.surf.get_width() / 2)
        self.rect.y = y - (self.surf.get_height() * 2)


class Iron(Item):

    def __init__(self):
        super(Iron, self).__init__(50, 25, 60, Steel(), True)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/ingot.png"), (50, 37))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)


class Steel(Item):

    def __init__(self):
        super(Steel, self).__init__(50, 25)
        self.surf.fill((50, 0, 50))
