import pygame
from items import *
from swords import *

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

BACKGROUND_COLOUR = (255, 255, 255)

PLAYER_1_CONFIG = {
    "UP": pygame.K_UP,
    "DOWN": pygame.K_DOWN,
    "LEFT": pygame.K_LEFT,
    "RIGHT": pygame.K_RIGHT,
    "USE": pygame.K_RCTRL,
    "IMG": "Sprites/graham-1.png",
    "SPEED": 10
}

PLAYER_2_CONFIG = {
    "UP": pygame.K_w,
    "DOWN": pygame.K_s,
    "LEFT": pygame.K_a,
    "RIGHT": pygame.K_d,
    "USE": pygame.K_LSHIFT,
    "IMG": "Sprites/graham-2.png",
    "SPEED": 10
}

MAP_1 = {

}

SMELT_RECIPES = {
    Steel: (Iron, 120)
}

HAMMER_RECIPES = {
    BasicSword: (Steel, 60)
}

GRINDER_RECIPES = {
    BasicSword: (BasicSword, 100)
}
