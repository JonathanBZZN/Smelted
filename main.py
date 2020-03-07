from player import *
from static_objects import *
from config import *
from swords import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

# init player
player1 = Player(PLAYER_1_CONFIG)
player2 = Player(PLAYER_2_CONFIG)
player2.rect.x = 200

furnace = Furnace()
Hammer = Hammer()
collect = CollectionPoint(Iron)
grinder = Grinder()

# Init sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(furnace)
all_sprites.add(Hammer)
all_sprites.add(collect)
all_sprites.add(grinder)

# init game clock
clock = pygame.time.Clock()

# game clock
while not done:
    # Set screen background
    screen.fill((255, 255, 255))

    # Draw all sprites
    for entity in all_sprites:
        if isinstance(entity, Player):
            screen.blit(entity.surf, entity.rect)
            # Draw inventory if not none
            if entity.inventory is not None:
                screen.blit(entity.inventory.surf, entity.inventory.rect)
        else:
            screen.blit(entity.surf, entity.rect)

    # Loop through every event in the queue
    for event in pygame.event.get():
        # Quiting
        if event.type == pygame.QUIT:
            done = True

    # Update players
    pressed = pygame.key.get_pressed()
    player1.update(pressed, all_sprites)
    player2.update(pressed, all_sprites)
    furnace.update()

    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()
quit()
