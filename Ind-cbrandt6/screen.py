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
        self.DISPLAYSURF.fill(settings.BLACK)
        # This is just kinda style rectangle
        # py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, settings.WIDTH - 20, settings.HEIGHT - 20))
        for i in rectArr:
            py.draw.rect(self.DISPLAYSURF, settings.BLUE, i)

    def lvlone(self):

        # Creating rectangle objects and appending them to a list
        # They are not being drawn here
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
            rectArr.append(py.Rect(x, y, 50, 8))
            # Decrement y so later rects are drawn higher
            y = y - 50

            # print(rectArr[0].x)

        # This is the tall barrier
        rectArr.append(py.Rect(275, 150, 8, settings.HEIGHT - 150))

    def lvltwo(self):
        pass

    def lvlthree(self):
        pass


def checkcollision():
    global rectArr
    import main
    play = main.game.player
    for rect in rectArr:

        # The player is reached through main because it needs to be the instantiated player object
        if rect.colliderect(main.game.player.rect):

            # If there is a collision there is no need to continue through the rest of the list
            # If the player collides with the bottom of the platform, return 0, return 1 for the top
            # Return 2 for the left side, and 3 for the right side

            # Player has hit the bottom
            if play.rect.top - 1 < rect.bottom + 1 < play.rect.bottom + 1:
                play.position.y = rect.bottom + 1
                return 0
            # Player has landed on the top
            if play.rect.bottom + 1 >= rect.top - 1 > play.rect.top - 1:
                play.position.y = rect.top - settings.playerSize + 1

                return 1
            # If the right side of the player is equal to the left side of the platform
            if play.rect.right + 1 > rect.left - 1 > play.rect.left - 1:
                play.position.x = rect.left - settings.playerSize + 1
                return 2
            # If the left side of the player is equal to the right side of the platform
            if play.rect.left - 1 < rect.right + 1 < play.rect.right + 1:
                play.position.x = rect.right - 1
                return 3






