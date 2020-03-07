from static_objects import StaticObject
from config import *
import random


class ScoreBoard(StaticObject):

    def __init__(self):
        super(ScoreBoard, self).__init__(SCREEN_WIDTH - 400, 0, 400, SCREEN_HEIGHT)
        self.surf.fill((232, 135, 62))
        # Score text
        self.font = pygame.font.SysFont('comicsansms', 40, True)
        self.score_rect = None
        self.score_text = None

        # Score board attributes
        self.score = 0
        self.set_score()
        self.order_list = []
        self.print_inventory = True

    def set_score(self):
        self.score_text = self.font.render('Score: ' + str(self.score), True, (0, 0, 0))
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = (self.rect.x + (self.score_text.get_width() / 2) + 25, 40)

    def add_item(self):
        # Pick a random item from the end points and add to list
        item = random.choice(list(END_POINTS.keys()))

        # Convert item to an Expected
        item_e = Expected(END_POINTS[item][0], item, succeed_score=END_POINTS[item][1], fail_score=END_POINTS[item][2])
        self.order_list.append(item_e)

    def update(self):
        # Loop through each item in order and reduce time
        self.update_times()

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

        # Loop through each item in inventory and print
        y = 50

        for item in self.order_list:
            # Update y component
            y += item.print_item.surf.get_height() + 20

            # Check if y is out of bounds
            if y > self.surf.get_height() - 50:
                break
            # Else print item
            item = item.print_item
            item.update(self.rect.x - (self.surf.get_width() / 2) + 50, y, self.surf.get_height(), self.surf.get_width())
            screen.blit(item.surf, item.rect)

            # Print time remaining


class EndPoint(StaticObject):

    def __init__(self, score_board, x_pos, y_pos):
        super(EndPoint, self).__init__(x_pos, y_pos, 200, 200, 15)
        self.surf.fill((0, 125, 69))
        self.inventory = []
        self.score_board = score_board

    def interact(self, player):
        if player.inventory is not None:
            # Loop through each element in order_list
            # Set item to remove if order completed
            item_drop = None
            for item in self.score_board.order_list:
                if isinstance(player.inventory, item.object):
                    # Completed goal so add score and remove item from order
                    player.inventory = None
                    self.score_board.score += item.succeed_score
                    self.score_board.set_score()
                    item_drop = item
                    break

            # Update order list if needed
            if item_drop is not None:
                self.score_board.order_list.remove(item_drop)


class Expected:

    def __init__(self, time, object, fail_score, succeed_score):
        self.time = time
        self.start_time = time
        self.object = object
        self.print_item = object()
        self.fail_score = fail_score
        self.succeed_score = succeed_score
