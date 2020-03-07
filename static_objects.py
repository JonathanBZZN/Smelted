from configs.recipes import *


class StaticObject(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, interactive_border_radius=0, print_inventory=False):
        super(StaticObject, self).__init__()

        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(x=x, y=y)

        self.interactive_border = pygame.Rect(self.rect.left - interactive_border_radius,
                                              self.rect.top - interactive_border_radius,
                                              self.rect.width + 2 * interactive_border_radius,
                                              self.rect.height + 2 * interactive_border_radius)

        self.print_inventory = print_inventory

    def interact(self, player):
        pass

    def print(self, screen):
        pass


class Furnace(StaticObject):
    def __init__(self, x_pos, y_pos, width=200, height=200):
        super(Furnace, self).__init__(x_pos, y_pos, width, height, 15)
        # Set furnace image
        self.idle = pygame.transform.scale(pygame.image.load("Sprites/furnace-idle.png"), (width, height))
        self.idle = self.idle.convert()
        self.idle.set_colorkey((0, 255, 0), RLEACCEL)

        self.work = pygame.transform.scale(pygame.image.load("Sprites/furnace-running.png"), (width, height))
        self.work = self.work.convert()
        self.work.set_colorkey((0, 255, 0), RLEACCEL)

        self.surf = self.idle

        # Set furnace attributes
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

            # Update sprite
            self.surf = self.work

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
                self.inventory = self.current_smelt()  # Inventory = a new object, which is output of smelt
                self.current_smelt = None
                self.finished = True
                # Reset furnace color
                self.surf = self.idle


class Hammer(StaticObject):

    def __init__(self, x_pos, y_pos, width=100, height=75):
        super(Hammer, self).__init__(x_pos, y_pos, width, height, 15)
        self.hammer_time = 0
        self.current_recipe = None

        # Set hammer image
        self.idle = pygame.transform.scale(pygame.image.load("Sprites/anvil-idle.png"), (width, height))
        self.idle = self.idle.convert()
        self.idle.set_colorkey((0, 255, 0), RLEACCEL)

        self.work = pygame.transform.scale(pygame.image.load("Sprites/anvil-running.png"), (width, height))
        self.work = self.work.convert()
        self.work.set_colorkey((0, 255, 0), RLEACCEL)

        self.surf = self.idle

    def interact(self, player):
        if self.current_recipe is None and player.inventory is not None and player.inventory.hammerable:
            # Player has an item which can be hammered
            for recipe in HAMMER_RECIPES:
                if isinstance(player.inventory, HAMMER_RECIPES[recipe][0]):
                    # Start hammering
                    self.surf = self.work
                    self.hammer_time = HAMMER_RECIPES[recipe][1]
                    self.current_recipe = recipe
                    player.inventory = None
                    break

        if self.current_recipe is not None and player.inventory is None:
            # Player is hammering
            if self.hammer_time > 0:
                self.hammer_time -= 1
            elif self.hammer_time == 0:
                # Player finished hammering
                player.inventory = self.current_recipe()
                self.current_recipe = None
                self.surf = self.idle


class Table(StaticObject):
    
    def __init__(self, x_pos, y_pos, width=100, height=100):
        super(Table, self).__init__(x_pos, y_pos, width, height, 15, print_inventory=True)
        self.surf.fill((0, 0, 0))
        self.inventory = None
        self.interact_cooldown = 0

    def interact(self, player):
        if self.interact_cooldown != 0:
            self.interact_cooldown -= 1
            return

        if player.inventory is not None and self.inventory is None:
            self.inventory = player.inventory
            player.inventory = None
            self.interact_cooldown = 7
        elif player.inventory is None and self.inventory is not None:
            player.inventory = self.inventory
            self.inventory = None
            self.interact_cooldown = 7

    def print(self, screen):
        if self.inventory is not None:
            self.inventory.update(self.rect.x, self.rect.y + self.surf.get_height() / 2, self.surf.get_height(), self.surf.get_width())
            screen.blit(self.inventory.surf, self.inventory.rect)


class Grinder(StaticObject):

    def __init__(self, x_pos, y_pos, width=100, height=100):
        super(Grinder, self).__init__(x_pos, y_pos, width, height, 15)
        self.surf.fill((255,0,255))
        self.grind_time = 0
        self.current_recipe = None

    def interact(self, player):

        if self.current_recipe is None and player.inventory is not None and player.inventory.grindable:
            # Player has an item to grind
            for recipe in GRINDER_RECIPES:
                if isinstance(player.inventory, GRINDER_RECIPES[recipe][0]):
                    self.grind_time = GRINDER_RECIPES[recipe][1]
                    self.current_recipe = recipe
                    player.inventory = None
                    self.surf.fill((255, 0, 0))
                    break

        if self.current_recipe is not None and player.inventory is None:
            if self.grind_time > 0:
                # Player is grinding
                self.grind_time -= 1
            elif self.grind_time == 0:
                # Player has finished grinding
                player.inventory = self.current_recipe()
                self.current_recipe = None
                self.surf.fill((255,0,255))


class CollectionPoint(StaticObject):

    def __init__(self, output, x_pos, y_pos, width=100, height=100):
        super(CollectionPoint, self).__init__(x_pos, y_pos, width, height, 15)
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/collection.png"), (width, height))
        self.surf = self.surf.convert()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)
        self.output = output

        # Set printing
        self.print_inventory = True
        self.print_object = output()
        self.print_object.update(self.rect.x, self.rect.y, self.surf.get_height(), self.surf.get_width())

    def interact(self, player):
        if player.inventory is None:
            player.inventory = self.output()

    def print(self, screen):
        screen.blit(self.print_object.surf, self.print_object.rect)


class Bin(StaticObject):

    def __init__(self, x_pos, y_pos, width=50, height=50):
        super(Bin, self).__init__(x_pos, y_pos, width, height, 15)
        self.surf.fill((0, 0, 0))

    def interact(self, player):
        player.inventory = None


class Wall(StaticObject):

    def __init__(self, x_pos, y_pos, width=50, height=50):
        super(Wall, self).__init__(x_pos, y_pos, width, height)
        self.surf.fill((169, 169, 169))
