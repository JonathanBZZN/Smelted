import copy

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
        self.effect = pygame.mixer.Sound("Sounds/Fire.wav")

        # Set furnace attributes
        self.inventory = []
        self.inventory_type = None
        self.current_smelt = None
        self.finished = False
        self.burn_time = 0

    def print(self, screen):
        if self.print_inventory:
            # Print the item in the inventory
            self.inventory[0].update(self.rect.x, self.rect.y + self.surf.get_height() / 2, self.surf.get_height(), self.surf.get_width())
            screen.blit(self.inventory[0].surf, self.inventory[0].rect)

    def interact(self, player):
        # First item
        if len(self.inventory) == 0 and player.inventory is not None and player.inventory.smeltable:

            # Add item in players inventory to the furnace
            self.inventory.append(player.inventory)
            self.inventory_type = player.inventory
            player.inventory = None

            # Play sounds effect
            self.effect.play()

            # Now check if the items match inputs to a recipe
            for recipe in SMELT_RECIPES:
                if isinstance(self.inventory[0], SMELT_RECIPES[recipe][0][0]) and \
                        len(self.inventory) == len(SMELT_RECIPES[recipe][0]) and self.current_smelt is None:
                    # Start smelting

                    self.burn_time = SMELT_RECIPES[recipe][1]
                    self.current_smelt = recipe
                    break

            # Update sprite
            self.surf = self.work

        elif self.current_smelt is not None and isinstance(player.inventory, type(self.inventory_type)):



            # Adding to an already smelting furnace only if it is a recipe
            for recipe in SMELT_RECIPES:
                self.inventory.append(player.inventory)
                if self.compare_inventory(self.inventory, SMELT_RECIPES[recipe][0]):
                    # Add item in players inventory to the furnace
                    player.inventory = None
                    self.burn_time = SMELT_RECIPES[recipe][1]
                    self.current_smelt = recipe
                else:
                    del self.inventory[-1]

        elif player.inventory is None and self.finished:
            # Player taking output from furnace
            self.finished = False
            self.print_inventory = False
            player.inventory = self.inventory[0]
            self.inventory_type = None
            self.inventory = []

    def compare_inventory(self, inventory, recipe):
        if len(inventory) != len(recipe):
            return False

        for i in range(len(inventory)):
            if str(inventory[i]) != recipe[i].__name__:
                return False

        return True

    def update(self):
        # Check if there is a current recipe

        if self.current_smelt is not None:
            if self.burn_time > 0:
                # Reduce burn time
                self.burn_time -= 1
            elif self.burn_time == 0:
                # Produce output and reset furnace
                self.inventory = []
                self.inventory.append(self.current_smelt())  # Inventory = a new object, which is output of smelt
                self.current_smelt = None
                self.finished = True
                # Reset furnace color
                self.surf = self.idle
                self.print_inventory = True


class Hammer(StaticObject):

    def __init__(self, x_pos, y_pos, width=100, height=75):
        super(Hammer, self).__init__(x_pos, y_pos, width, height, 15)
        self.hammer_time = 0
        self.current_recipe = None
        self.effect = pygame.mixer.Sound("Sounds/AnvilHit.wav")

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
            self.effect.play()
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
        self.inventory = None
        self.interact_cooldown = 0

        # Set table image
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/table.png"), (width, height))
        self.surf = self.surf.convert()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)
        self.effect = pygame.mixer.Sound("Sounds/Table.wav")

    def interact(self, player):
        if self.interact_cooldown != 0:
            self.interact_cooldown -= 1
            return

        if player.inventory is not None and self.inventory is None:
            self.effect.play()
            self.inventory = player.inventory
            player.inventory = None
            player.interacted = True
            self.interact_cooldown = 10
        elif player.inventory is None and self.inventory is not None:
            self.effect.play()
            player.inventory = self.inventory
            player.interacted = True
            self.inventory = None
            self.interact_cooldown = 10

    def print(self, screen):
        if self.inventory is not None:
            self.inventory.update(self.rect.x, self.rect.y + self.surf.get_height() / 2, self.surf.get_height(), self.surf.get_width())
            self.inventory.rect.move_ip(0, 20)
            screen.blit(self.inventory.surf, self.inventory.rect)


class Grinder(StaticObject):

    def __init__(self, x_pos, y_pos, width=100, height=100):
        super(Grinder, self).__init__(x_pos, y_pos, width, height, 15)
        self.grind_time = 0
        self.current_recipe = None
        self.effect = pygame.mixer.Sound("Sounds/GrindGrindGrind.wav")

        # Set grinder images
        self.idle = pygame.transform.scale(pygame.image.load("Sprites/grinder-idle.png"), (width, height))
        self.idle = self.idle.convert()
        self.idle.set_colorkey((0, 255, 0), RLEACCEL)

        self.work = pygame.transform.scale(pygame.image.load("Sprites/grinder-active.png"), (width, height))
        self.work = self.work.convert()
        self.work.set_colorkey((0, 255, 0), RLEACCEL)

        self.surf = self.idle

    def interact(self, player):

        if self.current_recipe is None and player.inventory is not None and player.inventory.grindable:
            # Player has an item to grind
            self.effect.play()
            for recipe in GRINDER_RECIPES:
                if isinstance(player.inventory, GRINDER_RECIPES[recipe][0]):
                    self.grind_time = GRINDER_RECIPES[recipe][1]
                    self.current_recipe = recipe
                    player.inventory = None
                    self.surf = self.work
                    break

        if self.current_recipe is not None and player.inventory is None:
            if self.grind_time > 0:
                # Player is grinding
                self.grind_time -= 1
            elif self.grind_time == 0:
                # Player has finished grinding
                player.inventory = self.current_recipe()
                self.current_recipe = None
                self.surf = self.idle


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
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/bin.png"), (width, height))
        self.surf = self.surf.convert()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)
        self.effect = pygame.mixer.Sound("Sounds/NomNomNom.wav")

    def interact(self, player):
        self.effect.play()
        player.inventory = None


class Wall(StaticObject):

    def __init__(self, x_pos, y_pos, width=100, height=100):
        super(Wall, self).__init__(x_pos, y_pos, width, height)
        # Set table image
        self.surf = pygame.transform.scale(pygame.image.load("Sprites/wall.png"), (width, height))
        self.surf = self.surf.convert()
        self.surf.set_colorkey((0, 255, 0), RLEACCEL)
