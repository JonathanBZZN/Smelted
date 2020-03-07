from static_objects import StaticObject
from config import *
import random


class ScoreBoard(StaticObject):

    def __init__(self):
        super(ScoreBoard, self).__init__(SCREEN_WIDTH - 400, 0, 400, SCREEN_HEIGHT)
        self.surf.fill((100, 0, 200))
        self.score = 0
        self.order_list = []
        self.print_inventory = True

    def add_item(self):
        # Pick a random item from the end points and add to list
        item = None
        for i in END_POINTS:
            item = i
            break

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
            self.score -= item.fail_score()

    def print(self, screen):
        # Loop through each item in inventory and print
        y = 0

        for item in self.order_list:
            # Update y component
            y += 50

            # Check if y is out of bounds
            if y > self.surf.get_height() - 50:
                break
            # Else print item
            item = item.print_item
            item.update(self.rect.x, y, self.surf.get_height(), self.surf.get_width())
            screen.blit(item.surf, item.rect)


class EndPoint(StaticObject):

    def __init__(self, score_board):
        super(EndPoint, self).__init__(400, 300, 200, 200, 15)
        self.surf.fill((0, 125, 69))
        self.inventory = []
        self.score_board = score_board

    def interact(self, player):
        if player.inventory is not None and any(isinstance(player.inventory, x.object) for x in self.score_board.order_list):
            player.inventory = None


class Expected:

    def __init__(self, time, object, fail_score, succeed_score):
        self.time = time
        self.object = object
        self.print_item = object()
        self.fail_score = fail_score
        self.succeed_score = succeed_score
