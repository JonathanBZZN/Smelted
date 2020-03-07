import pygame
from vector import Vector


class Wall(pygame.sprite.Sprite):

    def __init__(self):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(x=50, y=50)
