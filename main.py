from player import *
from score_board import *
from configs.config import *
from swords import *


global SCORE
SCORE = 0

black = 0, 0, 0
white = 255, 255, 255


def text_objects(text, color):
    textSurface = pygame.font.SysFont("comicsansms", 60).render(
        text, True, color
        )
    return textSurface, textSurface.get_rect()


def run():
    # Init screen and pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # run each map
    for idx, MAP in enumerate(MAPS):
        run_map(MAP, screen)
        if (idx != len(MAPS) - 1):
            run_continue(screen, True)

    run_continue(screen, False)

    # Clean up
    pygame.quit()
    quit()


def run_map(map, screen):
    done = False
    map_time = map["TIME_LIMIT"]

    # Load map
    all_sprites = pygame.sprite.Group()
    players, score, update = load_map(map, all_sprites)
    score.total_time = map_time

    # init game clock
    clock = pygame.time.Clock()

    # Load background image
    background = pygame.image.load("Sprites/floor.png")

    # game clock
    while not done:
        # Set screen background
        map_time -= 1
        score.time = map_time
        screen.blit(background, (0, 0))

        # Draw all sprites
        for entity in all_sprites:
            if isinstance(entity, Player):
                screen.blit(entity.surf, entity.rect)
                # Draw inventory if not none
                if entity.inventory is not None:
                    screen.blit(entity.inventory.surf, entity.inventory.rect)
            else:
                screen.blit(entity.surf, entity.rect)

            if isinstance(entity, StaticObject) and entity.print_inventory:
                entity.print(screen)

        # Loop through every event in the queue
        for event in pygame.event.get():
            # Quiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update players
        pressed = pygame.key.get_pressed()
        for player in players:
            player.update(pressed, all_sprites)

        # Update all objects that need to be updated
        for entity in update:
            entity.update()

        pygame.display.flip()
        clock.tick(60)

        # Check if done
        if map_time <= 0:
            done = True

    global SCORE
    SCORE = SCORE + score.score


def run_continue(screen, check):
    done = False
    # init game clock
    clock = pygame.time.Clock()

    # Load continue assets
    bg = pygame.image.load("Sprites/floor.png")
    screen.blit(bg, (0, 0))
    if check:
        textBox = pygame.image.load("Sprites/continueDialogue.png")
    else:
        textBox = pygame.image.load("Sprites/continueDialogueFinal.png")
    head = pygame.image.load("Sprites/findlaysticker-flipped.png")

    # game clock
    while not done:
        # Set screen background
        screen.blit(textBox, (SCREEN_WIDTH / 2 - 400, SCREEN_HEIGHT / 2 - 350))
        screen.blit(head, (SCREEN_WIDTH / 2 - 550, SCREEN_HEIGHT / 2 + 100))

        # Loop through every event in the queue
        for event in pygame.event.get():
            # Quiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        highscore, highscorerect = text_objects(str(SCORE), black)
        highscorerect.center = (SCREEN_WIDTH/2 - 160, SCREEN_HEIGHT/2 - 70)
        screen.blit(highscore, highscorerect)

        textCont, textContrect = text_objects("Continue!", black)
        textQuit, textQuitrect = text_objects("Quit!", black)

        if (SCREEN_WIDTH/2 + 286) > mouse[0] > (SCREEN_WIDTH/2 + 66) and SCREEN_HEIGHT/2 - 52 > mouse[1] > SCREEN_HEIGHT/2 -148:
            textCont, textContrect = text_objects("Continue!", white)
            if click[0] == 1:
                done = True

        textContrect.center = (SCREEN_WIDTH/2 + 175, SCREEN_HEIGHT/2 - 100)
        if check:
            screen.blit(textCont, textContrect)

        if (SCREEN_WIDTH/2 + 286) > mouse[0] > (SCREEN_WIDTH/2 + 66) and SCREEN_HEIGHT/2 + 66 > mouse[1] > SCREEN_HEIGHT/2 - 30:
            textQuit, textQuitrect = text_objects("Quit!", white)
            if click[0] == 1:
                pygame.quit()
                quit()

        textQuitrect.center = (SCREEN_WIDTH/2 + 180, SCREEN_HEIGHT/2 + 20)
        screen.blit(textQuit, textQuitrect)

        pygame.display.flip()
        clock.tick(60)


def load_map(map, all_sprites):
    # First load in the player 1 and  2 position
    players = []

    for i in range(1, map["PLAYERS"] + 1):
        # Create the player object
        player_str = "PLAYER_" + str(i) + "_"
        player = Player(PLAYER_CONFIGS[player_str+"CONFIG"], map[player_str+"POS"][0], map[player_str+"POS"][1])

        # Load the player into the game
        players.append(player)
        all_sprites.add(player)

    # Add score board
    score = ScoreBoard()
    score.end_points = map["END_POINTS"]
    score.difficulty = map["DIFFICULTY"]
    all_sprites.add(score)

    # Add the submit object
    end_point = EndPoint(score, map["SUBMIT_POS"][0], map["SUBMIT_POS"][1])
    all_sprites.add(end_point)

    # Add score to update
    update = [score, end_point]

    # Load in all objects
    for item in map["OBJECTS"]:
        # Create this object and add to all_sprites
        item_instance = item[0](*item[1])
        all_sprites.add(item_instance)

        # If item instance of furnace add to update
        if isinstance(item_instance, Furnace):
            update.append(item_instance)

    return players, score, update
