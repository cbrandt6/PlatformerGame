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

    # TODO Run through array of rectangles and check them against the player sprite, you can use vector.reflect_ip
    # TODO stuff to bounce the sprite
    import main
    # print("rectArr Len = ", len(rectArr))
    for rect in rectArr:
        # print("rect.x = ", rect.x)
        # The player is reached through main because it needs to be the instantiated player object
        if rect.colliderect(main.game.player.rect):
            # print("Plat top= ", rect.top)
            # print("Play bottom= ", main.game.player.rect.bottom)
            # If there is a collision there is no need to continue through the rest of the list
            # TODO Check to see if the collision occurred on one of the sides, or the top/bottom
            # If the player collides with the bottom of the platform, return 0, return 1 for the top
            # Return 2 for the left side, and 3 for the right side

            # TODO Check the left side of the rect, right side of the player
            if rect.left - main.game.player.rect.right < 2:
                return 2
            # TODO Check the right side
            elif main.game.player.rect.left - rect.right < 2:
                return 3
            # TODO Compare the top of the rect, bottom of the player
            # Two pixel tolerance
            elif rect.top - main.game.player.rect.bottom < 2:
                return 1
            # TODO Check the bottom of the rect, top of the player
            # The player top will have the greater value
            elif main.game.player.rect.top - rect.bottom < 2:
                return 0





