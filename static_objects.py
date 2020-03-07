import pygame
from items import *
from config import *


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
        self.inventory = None
        self.current_smelt = None
        self.finished = False
        self.burn_time = 0

    def interact(self, player):
        if self.inventory is None and player.inventory is not None and player.inventory.smeltable:
            # Add item in players inventory to the furnace
            self.inventory = player.inventory
            player.inventory = None

            # Now check if the items match inputs to a recipe
            for recipe in SMELT_RECIPES:
                if isinstance(self.inventory, SMELT_RECIPES[recipe][0]) and self.current_smelt is None:
                    # Start smelting
                    self.burn_time = SMELT_RECIPES[recipe][1]
                    self.current_smelt = recipe
                    break

            # Update color
            self.surf.fill((255, 0, 0))

        elif player.inventory is None and self.finished:
            # Player taking output from furnace
            self.finished = False
            player.inventory = self.inventory
            self.inventory = None

    def update(self):
        # Check if there is a current recipe
        if self.current_smelt is not None:
            if self.burn_time > 0:
                # Reduce burn time
                self.burn_time -= 1
            elif self.burn_time == 0:
                # Produce output and reset furnace
                self.inventory = self.current_smelt() # Inventory = a new object, which is output of smelt
                self.current_smelt = None
                self.finished = True
                # Reset furnace color
                self.surf.fill((255, 165, 0))


class Hammer(StaticObject):

    def __init__(self):
        super(Hammer, self).__init__(500, 300, 200, 200, 15)
        self.surf.fill((165, 165, 0))
        self.hammer_time = 0
        self.current_recipe = None

    def interact(self, player):
        if self.current_recipe is None and player.inventory is not None and player.inventory.hammerable:
            # Player has an item which can be hammered
            for recipe in HAMMER_RECIPES:
                if isinstance(player.inventory, HAMMER_RECIPES[recipe][0]):
                    # Start hammering
                    self.hammer_time = HAMMER_RECIPES[recipe][1]
                    self.current_recipe = recipe
                    player.inventory = None
                    self.surf.fill((255, 0, 0))
                    break

        if self.current_recipe is not None and player.inventory is None:
            # Player is hammering
            if self.hammer_time > 0:
                self.hammer_time -= 1
            elif self.hammer_time == 0:
                # Player finished hammering
                player.inventory = self.current_recipe()
                self.current_recipe = None
                self.surf.fill((165, 165, 0))


class CollectionPoint(StaticObject):

    def __init__(self, output):
        super(CollectionPoint, self).__init__(800, 100, 100, 100, 15)
        self.surf.fill((0, 0, 255))
        self.output = output

    def interact(self, player):
        if player.inventory is None:
            player.inventory = self.output()


class Wall(StaticObject):

    def __init__(self):
        super(Wall, self).__init__(50, 50, 50, 50)
        self.surf.fill((169, 169, 169))
