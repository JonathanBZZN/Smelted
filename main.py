from player import *
from static_objects import *
from conifg import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

# init player
player = Player()
wall = Wall()
furnace = Furnace()
collect = CollectionPoint()

# Init sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(furnace)
all_sprites.add(wall)
all_sprites.add(collect)

# init game clock
clock = pygame.time.Clock()

# game clock
while not done:
    # Set screen background
    screen.fill((255, 255, 255))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Loop through every event in the queue
    for event in pygame.event.get():
        # Quiting
        if event.type == pygame.QUIT:
            done = True

    # Update players
    pressed = pygame.key.get_pressed()
    player.update(pressed, all_sprites)

    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()
quit()
