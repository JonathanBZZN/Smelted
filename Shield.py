from items import *


class Shield(Item):

    def __init__(self, width, height):
        super(Shield, self).__init__(width, height)

class SteelShield(Shield):

    def __init__(self):
        super(SteelShield, self).__init__(50, 50)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/shield.png"), (50, 50))
        self.surf = self.surf.convert()
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)

