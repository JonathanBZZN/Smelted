import pygame
from items import *

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

PLAYER_1_CONFIG = {
    "UP": pygame.K_UP,
    "DOWN": pygame.K_DOWN,
    "LEFT": pygame.K_LEFT,
    "RIGHT": pygame.K_RIGHT,
    "USE": pygame.K_RCTRL
}

PLAYER_2_CONFIG = {
    "UP": pygame.K_w,
    "DOWN": pygame.K_s,
    "LEFT": pygame.K_a,
    "RIGHT": pygame.K_d,
    "USE": pygame.K_LSHIFT
}

SMELT_RECIPES = {
    Steel: (Iron, 120)
}
