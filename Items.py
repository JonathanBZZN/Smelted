import pygame


class Item(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super(Item, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(x=0, y=0)

    def update(self, x, y, player_height, player_width):
        self.rect.x = x + (player_width / 2) - (self.surf.get_width() / 2)
        self.rect.y = y - (self.surf.get_height() * 2)


class Smeltable(Item):

    def __init__(self, width, height, smelt_time, output):
        super(Smeltable, self).__init__(width, height)
        self.smelt_time = smelt_time
        self.output = output


class Iron(Smeltable):

    def __init__(self):
        super(Iron, self).__init__(50, 25, 60, Steel())
        self.surf.fill((0, 255, 0))


class Steel(Item):

    def __init__(self):
        super(Steel, self).__init__(50, 25)
        self.surf.fill((50, 0, 50))
