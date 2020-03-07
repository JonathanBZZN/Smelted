from static_objects import *

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
    "PLAYER_1_POS": (100, 100),
    "PLAYER_2_POS": (100, 200),

    "OBJECTS": {
        Furnace: (500, 500),
        Grinder: (700, 500),
        Hammer: (300, 500),
        Table: (700, 100),
        CollectionPoint: (Iron, 200, 200)
    },

    "SUBMIT_POS": (300, 300),
    "TIME_LIMIT": 60*20,
}

MAPS = [MAP_1]

END_POINTS = {
    Iron: (2000, 100, 10),
    Steel: (2000, 200, 20),
    SharpBasicSword: (2000, 400, 20)
}
