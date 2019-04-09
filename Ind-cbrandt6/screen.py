import pygame as py
import settings

# This file will contain all the level layouts, and will draw them when called from the main function
rectArr = []

levelcnt = 0

class levels:

    def __init__(self):
        global levelcnt
        # Main function will not call this file to create the display surface
        # Initialize pygame
        py.init()
        # Create the display surface
        self.DISPLAYSURF = py.display.set_mode((settings.WIDTH, settings.HEIGHT), 0, 32)

        # This is the title bar caption
        py.display.set_caption(settings.TITLE)
        levelcnt = 1
        # Redraw the window
        self.DISPLAYSURF.fill(settings.BLACK)
        # This is just kinda style rectangle
        # py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, settings.WIDTH - 20, settings.HEIGHT - 20))
        self.firstDraw = True
        self.lvlone()

    def redraw(self):
        global levelcnt
        # Redraw the window
        self.DISPLAYSURF.fill(settings.BLACK)
        # This is just kinda style rectangle
        # py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, settings.WIDTH - 20, settings.HEIGHT - 20))
        if levelcnt == 1:
            self.lvlone()
        if levelcnt == 2:
            self.lvltwo()

        # If it is not the first time drawing the level, don't keep redrawing the rectangles
        if not self.firstDraw:
            for i in rectArr:
                py.draw.rect(self.DISPLAYSURF, settings.BLUE, i)

    def lvlone(self):

        # Creating rectangle objects and appending them to a list
        # They are not being drawn here

        if self.firstDraw:
            rectArr.clear()
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

            rectArr.append(py.Rect(500, settings.HEIGHT - 100, 100, 100))
            self.firstDraw = False

    def lvltwo(self):
        rectArr.clear()
        rectArr.append(py.Rect(settings.WIDTH / 4, settings.HEIGHT / 2, 20, 100))
        rectArr.append(py.Rect((settings.WIDTH / 4) * 2, settings.HEIGHT / 2, 20, 100))

    def lvlthree(self):
        pass


def checkcollision():
    global rectArr
    global levelcnt
    import main
    play = main.game.player
    for rect in rectArr:

        # The player is reached through main because it needs to be the instantiated player object
        if rect.colliderect(main.game.player.rect):
            if levelcnt == 1 and rect.x == 500 and rect.y == settings.HEIGHT - 100:
                levelcnt += 1
            # If there is a collision there is no need to continue through the rest of the list
            # If the player collides with the bottom of the platform, return 0, return 1 for the top
            # Return 2 for the left side, and 3 for the right side

            # Player has hit the bottom
            if play.rect.top - 2 < rect.bottom + 2 < play.rect.bottom + 2:
                play.position.y = rect.bottom + 2
                return 0

            # Player has landed on the top
            if play.rect.bottom + 2 >= rect.top - 2 > play.rect.top - 2:
                play.position.y = rect.top - settings.playerSize + 2

                return 1
            # If the right side of the player is equal to the left side of the platform
            if play.rect.right + 2 > rect.left - 2 > play.rect.left - 2:
                play.position.x = rect.left - settings.playerSize + 2
                return 2
            # If the left side of the player is equal to the right side of the platform
            if play.rect.left - 2 < rect.right + 2 < play.rect.right + 2:
                play.position.x = rect.right - 2
                return 3





