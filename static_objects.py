import pygame


class Furnace(pygame.sprite.Sprite):

    def __init__(self):
        super(Furnace, self).__init__()
        self.surf = pygame.Surface((200, 200))
        self.surf.fill((255, 165, 0))
        self.rect = self.surf.get_rect(x=300, y=300)


class Wall(pygame.sprite.Sprite):

    def __init__(self):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(x=50, y=50)