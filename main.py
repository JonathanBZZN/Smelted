import pygame
from player import *

pygame.init()
screen = pygame.display.set_mode((1600, 900))
done = False

# init player
player = Player()

# init game clock
clock = pygame.time.Clock()

# game clock
while not done:
    # Set screen background and draw player
    screen.fill((255, 255, 255))
    screen.blit(player.surf, player.rect)

    for event in pygame.event.get():
        # Quiting
        if event.type == pygame.QUIT:
            done = True

    # Get all buttons pressed
    pressed = pygame.key.get_pressed()

    # Update players
    player.update(pressed)

    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()
quit()
