import pygame
from player import *
from conifg import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

# init player
player = Player()
x_change = 0

# init game clock
clock = pygame.time.Clock()

# game clock
while not done:
    # Set screen background
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        # Quiting
        if event.type == pygame.QUIT:
            done = True

    # Get all buttons pressed
    pressed = pygame.key.get_pressed()

    # Update players
    player.update(pressed)
    player.draw(screen)

    pygame.display.update()
    clock.tick(60)

# Clean up
pygame.quit()
quit()
