import pygame
import main as m
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

menuElements = ["menu_art.png", "menu_art_small_button.png", "sound.png", "no_sound.png"]


def text_objects(text, color):
    textSurface = pygame.font.Font("freesansbold.ttf", 60).render(
        text, True, color
        )
    return textSurface, textSurface.get_rect()


def game_intro():
    sound = True
    menuLoaded = []
    for elements in menuElements:
        menuLoaded.append(pygame.image.load(elements))

    menuRect = []
    for loaded in menuLoaded:
        menuRect.append(loaded.get_rect())

    menuRect[0].center = (width/2, height/2 - 200)
    menuRect[1].center = (width/2, height/2 + 100)
    menuRect[2].center = (25, height - 25)
    menuRect[3].center = (25, height - 25)

    while True:
        screen.fill(white)
        for x in range(3):
            if x == 2:
                if sound:
                    screen.blit(menuLoaded[2], menuRect[2])
                else:
                    screen.blit(menuLoaded[3], menuRect[3])
            else:
                screen.blit(menuLoaded[x], menuRect[x])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        textStart, textStartrect = text_objects("Start!", black)
        textQuit, textQuitrect = text_objects("Quit!", black)

        if (width/2 - 110) > mouse[0] > (width/2 - 410) and height/2 + 170 > mouse[1] > height/2 + 30:
            textStart, textStartrect = text_objects("Start!", white)
            if click[0] == 1:
                m.gameStuff()

        textStartrect.center = (width/2 - 255, height/2 + 100)
        screen.blit(textStart, textStartrect)

        if (width/2 + 410) > mouse[0] > (width/2 + 110) and height/2 + 170 > mouse[1] > height/2 + 30:
            textQuit, textQuitrect = text_objects("Quit!", white)
            if click[0] == 1:
                pygame.quit()
                quit()

        if 50 > mouse[0] > 0 and height > mouse[1] > height - 50:
            if click[0] == 1:
                if sound:
                    sound = False
                elif (not sound):
                    sound = True

        textQuitrect.center = (width/2 + 260, height/2 + 100)
        screen.blit(textQuit, textQuitrect)

        pygame.display.flip()
        clock.tick(60)


def gameplay():
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

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.update()


game_intro()
# gameplay()