import pygame as py
import settings
import player

# This file will contain all the level layouts, and will draw them when called from the main function
DISPLAYSURF = ''

# This array holds all the rectangles of the levels



class levels:

    def __init__(self):
        # Main function will not call this file to create the display surface
        # Initialize pygame
        py.init()

        self.rectArr = []
        # Create the display surface
        self.DISPLAYSURF = py.display.set_mode((settings.WIDTH, settings.HEIGHT), 0, 32)

        # This is the title bar caption
        py.display.set_caption(settings.TITLE)

        # Redraw the window
        self.DISPLAYSURF.fill(settings.BLACK)
        # This is just kinda style rectangle
        py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, settings.WIDTH - 20, settings.HEIGHT - 20))

    def redraw(self):
        # Redraw the window
        # self.DISPLAYSURF.fill(settings.BLACK)
        # This is just kinda style rectangle
        # py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, settings.WIDTH - 20, settings.HEIGHT - 20))
        self.lvlone()

    def lvlone(self):
        self.DISPLAYSURF.fill(settings.BLACK)

        y = settings.HEIGHT - 50

        for i in range(14):
            # Call the sprite constructor
            py.sprite.Sprite.__init__(self)
            image = py.Surface([50, 8])
            image.fill(settings.BLUE)

            rect = image.get_rect()
            # Alternates between right and left side platforms
            if i % 2 != 0:
                rect.x = 150

            else:
                rect.x = 50
            rect.y = y
            # Rectangles are defined with the surface, color, (x, y, width, height)
            self.rectArr.append(rect)
            # Decrement y so later rects are drawn higher
            y = y - 50

        # This is the tall barrier
        image = py.Surface([8, settings.HEIGHT-150])
        image.fill(settings.BLUE)
        rectTall = image.get_rect()
        rect.x = 275
        rect.y = 150
        self.rectArr.append(rectTall)

    def lvltwo(self):
        pass

    def lvlthree(self):
        pass

    def checkcollision(self):
        # TODO Run through array of rectangles and check them against the player sprite, you can use vector.reflect_ip
        # TODO stuff to bounce the sprite
        for i in range(len(self.rectArr) - 1):
            if self.rectArr[i].colliderect(player):
                return i
            else:
                return -1


