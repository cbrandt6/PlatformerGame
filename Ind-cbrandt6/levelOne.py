import pygame as py
import settings

# This file will contain all the level layouts, and will draw them when called from the main function
DISPLAYSURF = ''
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
        py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, settings.WIDTH - 20, settings.HEIGHT - 20))

    def redraw(self):
        # Redraw the window
        self.DISPLAYSURF.fill(settings.BLACK)
        # This is just kinda style rectangle
        py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, settings.WIDTH - 20, settings.HEIGHT - 20))

    def lvlone(self):
        pass

    def lvltwo(self):
        pass

    def lvlthree(self):
        pass



