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

    ],

    "SUBMIT_POS": (300, 300),
    "TIME_LIMIT": 60*20,

    "END_POINTS": {
        Steel: (1000, 200, 10),
    },

    "DIFFICULTY": 0.999
}

MAP_2 = {
    "PLAYER_1_POS": (275, 450),
    "PLAYER_2_POS": (775, 450),

    "OBJECTS": [
        (Table, (550,300, 100, 100)),
        (Table, (550,400, 100, 100)),
        (Table, (550,500, 100, 100)),
        (Furnace, (100,100, 225, 200)),
        (Furnace, (325,100, 225, 200)),
        (Grinder, (875, 600, 225, 200)),
        (Hammer, (650, 600, 225, 200)),
        (CollectionPoint, (Iron, 250, 700))
    ],

    "SUBMIT_POS": (900, 110),
    "TIME_LIMIT": 60*60,

    "END_POINTS": {
        Steel: (1000, 200, 10),
        BasicSword: (2000, 400, 100),
        SharpBasicSword: (2500, 500, 200)
    },

    "DIFFICULTY": 0.99
}

MAP_2["OBJECTS"].extend([(Wall, (0, x)) for x in range(0, 900, 100)])
MAP_2["OBJECTS"].extend([(Wall, (1100, x)) for x in range(0, 900, 100)])
MAP_2["OBJECTS"].extend([(Wall, (550, 600 + x)) for x in range(0, 300, 100)])
MAP_2["OBJECTS"].extend([(Wall, (550, 0 + x)) for x in range(0, 300, 100)])
MAP_2["OBJECTS"].extend([(Wall, (0 + x, 800)) for x in range(0, 1200, 100)])
MAP_2["OBJECTS"].extend([(Wall, (0 + x, 0)) for x in range(0, 1200, 100)])

MAPS = [ MAP_2]
