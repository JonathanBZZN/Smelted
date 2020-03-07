import pygame
pygame.init()

size = width, height = 1600, 900
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
alt_green = 0, 255, 255
red = 255, 0, 0


screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def game_intro():
    ball = pygame.image.load("findlaysticker.png")
    ballrect = ball.get_rect()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(white)
        screen.blit(ball, ballrect)

        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Temp Menu", largeText)
        TextRect.center = (960, 440)

        screen.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        if 800+100 > mouse[0] > 800 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(screen, alt_green, (800, 550, 100, 50))
        else:
            pygame.draw.rect(screen, green, (800, 550, 100, 50))

        pygame.draw.rect(screen, red, (1000, 550, 100, 50))

        pygame.display.update()
        clock.tick(60)


# def gameplay():
#     ball = pygame.image.load("findlaysticker.png")
#     ballrect = ball.get_rect()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#         ballrect = ballrect.move(speed)
#         if ballrect.left < 0 or ballrect.right > width:
#             speed[0] = -speed[0]
#         if ballrect.top < 0 or ballrect.bottom > height:
#             speed[1] = -speed[1]
#
#         screen.fill(black)
#         screen.blit(ball, ballrect)
#         pygame.display.update()


game_intro()
# gameplay()