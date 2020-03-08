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

    "OBJECTS": [
        (Furnace, (500, 500)),
        (Grinder, (700, 500)),
        (Hammer, (300, 500)),
        (Table, (700, 100)),
        (CollectionPoint, (Iron, 200, 200))
    ],

    "SUBMIT_POS": (300, 300),
    "TIME_LIMIT": 60*20,
}

MAP_2 = {
    "PLAYER_1_POS": (275, 450),
    "PLAYER_2_POS": (775, 450),

    "OBJECTS": [
        (Wall, (0,0,100,900)),
        (Wall, (1100,0,100,900)),
        (Wall, (550,0,100,300)),
        (Wall, (550,600,100,300)),
        (Wall, (0, 800, 1200, 100)),
        (Wall, (0, 0, 1200, 100)),
        (Table, (550,300, 100, 100)),
        (Table, (550,400, 100, 100)),
        (Table, (550,500, 100, 100)),
        (Furnace, (100,100, 225, 200)),
        (Furnace, (325,100, 225, 200)),
        (Grinder, (875, 600, 225,200)),
        (Hammer, (650, 600, 225,200)),
        (CollectionPoint, (Iron, 250, 700))
    ],

    "SUBMIT_POS": (900, 110),
    "TIME_LIMIT": 60*20,
}

MAPS = [MAP_2]

END_POINTS = {
    Iron: (2000, 100, 10),
    Steel: (2000, 200, 20),
    SharpBasicSword: (2000, 400, 20)
}
