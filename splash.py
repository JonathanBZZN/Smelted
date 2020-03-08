import pygame
import main
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

menuElements = ["Sprites/menu_art.png", "Sprites/menu_art_small_button.png", "Sprites/sound.png", "Sprites/no_sound.png", "Sprites/bg.png"]


def text_objects(text, color):
    textSurface = pygame.font.SysFont("comicsansms", 60).render(
        text, True, color
        )
    return textSurface, textSurface.get_rect()


def game_intro():
    lastTime = 0
    sound = True
    menuLoaded = []
    for elements in menuElements:
        menuLoaded.append(pygame.image.load(elements))

    menuRect = []
    for loaded in menuLoaded:
        menuRect.append(loaded.get_rect())

    menuRect[0].center = (width/2, height/2 - 200)
    menuRect[1].center = (width/2, height/2 + 100)
    menuRect[2].center = (50, height - 50)
    menuRect[3].center = (50, height - 50)

    # start music
    pygame.mixer.music.load("Music/ingame.mp3")
    pygame.mixer.music.play(-1)

    while True:
        screen.blit(menuLoaded[4], (0, 0))
        for x in range(2):
            screen.blit(menuLoaded[x], menuRect[x])
        if sound:
            screen.blit(menuLoaded[2], menuRect[2])
        else:
            screen.blit(menuLoaded[3], menuRect[3])
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
                introPage()
                gameplay()



        textStartrect.center = (width/2 - 255, height/2 + 100)
        screen.blit(textStart, textStartrect)

        if (width/2 + 410) > mouse[0] > (width/2 + 110) and height/2 + 170 > mouse[1] > height/2 + 30:
            textQuit, textQuitrect = text_objects("Quit!", white)
            if click[0] == 1:
                pygame.quit()
                quit()

        if 100 > mouse[0] > 0 and height > mouse[1] > height - 100:
            if (pygame.time.get_ticks() - lastTime > 180):
                if click[0] == 1:
                    if sound:
                        sound = False
                        pygame.mixer.music.pause()
                    elif not sound:
                        sound = True
                        pygame.mixer.music.unpause()
                    lastTime = pygame.time.get_ticks()

        textQuitrect.center = (width/2 + 260, height/2 + 100)
        screen.blit(textQuit, textQuitrect)

        pygame.display.flip()
        clock.tick(60)


def introPage():
    infoAsset = pygame.image.load("Sprites/infopg.png")
    done = False
    while not done:
        screen.blit(infoAsset, (0, 0))
        # Loop through every event in the queue
        for event in pygame.event.get():
            # Quiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                done = True
        pygame.display.flip()
        clock.tick(60)


def gameplay():
    main.run()


if __name__ == "__main__":
    game_intro()