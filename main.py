from player import *
from score_board import *
from configs.config import *
from swords import *


def run():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    done = False

    # Load map
    all_sprites = pygame.sprite.Group()
    player1, player2, score, update = load_map(MAP_1, all_sprites)

    score.add_item()
    score.add_item()
    score.add_item()
    score.add_item()

    # init game clock
    clock = pygame.time.Clock()



    # Load background image
    background = pygame.image.load("Sprites/bg.png")

    # game clock
    while not done:
        # Set screen background
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
                done = True

        # Update players
        pressed = pygame.key.get_pressed()
        player1.update(pressed, all_sprites)
        player2.update(pressed, all_sprites)

        # Update all objects that need to be updated
        for entity in update:
            entity.update()

        pygame.display.flip()
        clock.tick(60)

    # Clean up
    pygame.quit()
    quit()


def load_map(map, all_sprites):
    # First load in the player 1 and  2 position
    player1 = Player(PLAYER_1_CONFIG, map["PLAYER_1_POS"][0], map["PLAYER_1_POS"][1])
    player2 = Player(PLAYER_2_CONFIG, map["PLAYER_2_POS"][0], map["PLAYER_2_POS"][1])

    # Update all_sprites to contain both players
    all_sprites.add(player1)
    all_sprites.add(player2)

    # Add score board
    score = ScoreBoard()
    all_sprites.add(score)

    # Add the submit object
    end_point = EndPoint(score, map["SUBMIT_POS"][0], map["SUBMIT_POS"][1])
    all_sprites.add(end_point)

    # Add score to update
    update = [score]

    # Load in all objects
    for item in map["OBJECTS"]:
        # Create this object and add to all_sprites
        item_instance = item(*map["OBJECTS"][item])
        all_sprites.add(item_instance)

        # If item instance of furnace add to update
        if isinstance(item_instance, Furnace):
            update.append(item_instance)

    return player1, player2, score, update
