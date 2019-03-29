import pygame as py
import settings
import player

# This file will contain all the level layouts, and will draw them when called from the main function
rectArr = []


class levels:

    def __init__(self):
        # Main function will not call this file to create the display surface
        # Initialize pygame
        py.init()
        # Create the display surface
        self.DISPLAYSURF = py.display.set_mode((settings.WIDTH, settings.HEIGHT), 0, 32)

        # This is the title bar caption
        py.display.set_caption(settings.TITLE)

        # Redraw the window
        self.DISPLAYSURF.fill(settings.BLACK)
        # This is just kinda style rectangle
        # py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, settings.WIDTH - 20, settings.HEIGHT - 20))
        self.lvlone()

    def redraw(self):
        # Redraw the window
        # self.DISPLAYSURF.fill(settings.BLACK)
        # This is just kinda style rectangle
        # py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, settings.WIDTH - 20, settings.HEIGHT - 20))
        self.lvlone()

    def lvlone(self):

        global rectArr
        self.DISPLAYSURF.fill(settings.BLACK)
        y = settings.HEIGHT - 50

        for i in range(14):

            # Alternates between right and left side platforms
            if i % 2 != 0:
                x = 150

            else:
                x = 50

            # Rectangles are defined with the surface, color, (x, y, width, height)
            rectArr.append(py.draw.rect(self.DISPLAYSURF, settings.BLUE, (x, y, 50, 8)))
            # Decrement y so later rects are drawn higher
            y = y - 50

            # print(rectArr[0].x)

        # This is the tall barrier
        rectArr.append(py.draw.rect(self.DISPLAYSURF, settings.BLUE, (275, 150, 8, settings.HEIGHT - 150)))

    def lvltwo(self):
        pass

    def lvlthree(self):
        pass


def checkcollision():
    global rectArr

    # TODO Run through array of rectangles and check them against the player sprite, you can use vector.reflect_ip
    # TODO stuff to bounce the sprite
    import main
    for i in range(len(rectArr) - 1):
        if rectArr[i].colliderect(main.game.player.rect):
            return i
        else:
            return -1


