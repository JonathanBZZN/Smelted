from player import *
from StaticObjects.wall import *
from conifg import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

# init player
player = Player()
wall = Wall()

# Init sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(wall)

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
    player.update(pressed, [wall])

    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()
quit()
