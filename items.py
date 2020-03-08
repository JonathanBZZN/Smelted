import pygame
from pygame.locals import RLEACCEL


class Item(pygame.sprite.Sprite):

    def __init__(self, width, height, smeltable=False, hammerable=False, grindable=False):
        super(Item, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(x=0, y=0)

        # Smelting attributes
        self.smeltable = smeltable
        self.hammerable = hammerable
        self.grindable = grindable

    def update(self, x, y, player_height, player_width):
        self.rect.x = x + (player_width / 2) - (self.surf.get_width() / 2)
        self.rect.y = y - (self.surf.get_height())
HotPlat

class Iron(Item):

    def __init__(self):
        super(Iron, self).__init__(50, 25, smeltable=True)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/ingot.png"), (50, 37))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)

    def __str__(self):
        return "Iron"


class Steel(Item):

    def __init__(self):
        super(Steel, self).__init__(50, 25, hammerable=True)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/hot_steel.png"), (50, 37))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)


    def __str__(self):
        return "Steel"


class BigSteel(Item):

    def __init__(self):
        super(BigSteel, self).__init__(50, 25, hammerable=True)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/table.png"), (50, 37))
    
    def __str__(self):
        return "BigSteel"

class GoldIngot(Item):

    def __init__(self):
        super(GoldIngot, self).__init__(50, 25, smeltable=True)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/gold-ore.png"), (50, 37))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)


class HotGold(Item):

    def __init__(self):
        super(HotGold, self).__init__(50, 25, hammerable=True)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/hot-gold.png"), (50, 37))

        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)
        

class PlatIngot(Item):

    def __init__(self):
        super(PlatIngot, self).__init__(50, 25, smeltable=True)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/plat-ore.png"), (50, 37))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)


class HotPlat(Item):

    def __init__(self):
        super(HotPlat, self).__init__(50, 25, hammerable=True)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/hot-plat.png"), (50, 37))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)

