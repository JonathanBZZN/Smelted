from configs.config import *
import random


class ScoreBoard(StaticObject):

    def __init__(self):
        super(ScoreBoard, self).__init__(SCREEN_WIDTH - 400, 0, 400, SCREEN_HEIGHT)
        self.surf.fill((232, 135, 62))
        # Score text
        self.font = pygame.font.SysFont('comicsansms', 40, True)
        self.score_rect = None
        self.total_time = 0
        self.time = 0
        self.score_text = None

        # Score board attributes
        self.score = 0
        self.set_score()
        self.order_list = []
        self.print_inventory = True

    def set_score(self):
        self.score_text = self.font.render('Score: ' + str(self.score), True, (0, 0, 0))
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = (self.rect.x + (self.score_text.get_width() / 2) + 25, 80)

    def add_item(self):
        # Pick a random item from the end points and add to list
        item = random.choice(list(END_POINTS.keys()))

        # Convert item to an Expected
        item_e = Expected(END_POINTS[item][0], item, succeed_score=END_POINTS[item][1], fail_score=END_POINTS[item][2])
        self.order_list.append(item_e)

    def update(self):
        # Loop through each item in order and reduce time
        self.update_times()

        # Add an extra item
        self.add_order()

    def add_order(self):
        # If no items add item
        if len(self.order_list) == 0:
            self.add_item()
        elif len(self.order_list) < 10:
            # Use randomness to add item
            if random.random() > DIFFICULTY:
                self.add_item()

    def update_times(self):
        # Create a list of all items which were failed to be made
        drop = []

        # Loop through each list and reduce time remaining
        for item in self.order_list:
            item.time -= 1
            if item.time <= 0:
                drop.append(item)

        # Remove each item in drop from items list
        for item in drop:
            # Remove the score for each failure
            self.order_list.remove(item)
            self.score -= item.fail_score
            self.set_score()

    def print(self, screen):
        # First print the score
        screen.blit(self.score_text, self.score_rect)

        # Print time remaining
        bar_pos = (self.rect.x + 25, 25)
        bar_size = (350, 25)
        border_color = (0, 0, 0)
        DrawBar(bar_pos, bar_size, border_color, self.time / self.total_time, screen)

        # Loop through each item in inventory and print
        y = 100

        for item in self.order_list:
            # Update y component
            y += item.print_item.surf.get_height() + 20

            # Check if y is out of bounds
            if y > self.surf.get_height() - 50:
                break
            # Else print item
            item_p = item.print_item
            item_p.update(self.rect.x - (self.surf.get_width() / 2) + 50, y, self.surf.get_height(), self.surf.get_width())
            screen.blit(item_p.surf, item_p.rect)

            # Print time remaining
            time_percentage = item.time / item.start_time
            bar_pos = (item_p.rect.x + item_p.surf.get_width() + 25, y - item_p.surf.get_width() / 2)
            bar_size = (200, 20)
            border_color = (0, 0, 0)
            DrawBar(bar_pos, bar_size, border_color, time_percentage, screen)


def DrawBar(pos, size, border_c, progress, screen):
    # Set the bar color
    bar_c = (0, 128, 0)
    if progress < 0.1:
        bar_c = (216, 0, 0)
    elif progress < 0.25:
        bar_c = (255, 0, 0)
    elif progress < 0.5:
        bar_c = (255, 69, 0)
    elif progress < 0.75:
        bar_c = (128, 128, 0)

    # Draw the progess bar
    pygame.draw.rect(screen, border_c, (*pos, *size), 5)
    inner_pos = (pos[0]+3, pos[1]+3)
    inner_size = ((size[0]-6) * progress, size[1]-6)
    pygame.draw.rect(screen, bar_c, (*inner_pos, *inner_size))


class EndPoint(StaticObject):

    def __init__(self, score_board, x_pos, y_pos):
        super(EndPoint, self).__init__(x_pos, y_pos, 200, 200, 15)
        self.surf.fill((0, 125, 69))
        self.inventory = []
        self.score_board = score_board

        # Init images
        self.idle = pygame.transform.scale(pygame.image.load("Sprites/findlaysticker.png"), (200, 200))
        self.idle = self.idle.convert()
        self.idle.set_colorkey((0, 255, 0), RLEACCEL)

        self.active = pygame.transform.scale(pygame.image.load("Sprites/findlaysticker-open.png"), (200, 200))
        self.active = self.active.convert()
        self.active.set_colorkey((0, 255, 0), RLEACCEL)

        self.surf = self.idle

        self.effect = pygame.mixer.Sound("Sounds/NomNomNom.wav")

        self.counter = 0

    def interact(self, player):
        if player.inventory is not None:
            # Loop through each element in order_list
            # Set item to remove if order completed
            item_drop = None
            for item in self.score_board.order_list:
                if isinstance(player.inventory, item.object):
                    # Completed goal so add score and remove item from order
                    self.effect.play()
                    self.surf = self.active
                    self.counter = 20
                    player.inventory = None
                    self.score_board.score += item.succeed_score
                    self.score_board.set_score()
                    item_drop = item
                    break

            # Update order list if needed
            if item_drop is not None:
                self.score_board.order_list.remove(item_drop)

    def update(self):
        if self.counter != 0:
            self.counter -= 1
        else:
            self.surf = self.idle


class Expected:

    def __init__(self, time, object, fail_score, succeed_score):
        self.time = time
        self.start_time = time
        self.object = object
        self.print_item = object()
        self.fail_score = fail_score
        self.succeed_score = succeed_score
