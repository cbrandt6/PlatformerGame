import pygame as py
import settings

# This file will contain all the level layouts, and will draw them when called from the main function


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

        # Initialize the level fields
        self.rectArr = []
        self.hazardArr = []
        self.levelcnt = 2
        self.endingCoords = ()
        self.spawnCoords = ()
        self.firstDraw = True

        self.lvltwo()

    def redraw(self):

        # Redraw the window
        self.DISPLAYSURF.fill(settings.BLACK)
        # This is just kinda style rectangle
        # py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, settings.WIDTH - 20, settings.HEIGHT - 20))
        if self.levelcnt == 1:
            self.lvlone()
        if self.levelcnt == 2:
            self.lvltwo()

        # If it is not the first time drawing the level, don't keep redrawing the rectangles
        if not self.firstDraw:
            for i in self.rectArr:
                # Check to see if the rectangle is the one that ends the level, and if it is paint it green
                if self.levelcnt == 1 and i.left == self.endingCoords[0] and i.top == self.endingCoords[1]:
                    py.draw.rect(self.DISPLAYSURF, settings.GREEN, i)

                # Otherwise fill it as blue
                else:
                    py.draw.rect(self.DISPLAYSURF, settings.BLUE, i)

            # Draw hazards if the array is not empty
            if self.hazardArr:
                for l in self.hazardArr:
                    py.draw.rect(self.DISPLAYSURF, settings.RED, l)

    def lvlone(self):
        # Creating rectangle objects and appending them to a list
        # They are not being drawn here

        if self.firstDraw:
            # Clear the rectangle list in case there are leftovers from something
            self.rectArr.clear()
            self.endingCoords = (1340, 50)
            self.spawnCoords = (0, settings.HEIGHT)
            # Initial height of the platforms
            y = settings.HEIGHT - 100

            for i in range(6):

                # Alternates between right and left side platforms
                if i % 2 != 0:
                    x = 150
                else:
                    x = 50
                # Rectangles are defined with the surface, color, (x, y, width, height)
                self.rectArr.append(py.Rect(x, y, 50, 8))

                # Decrement y so later rects are drawn higher
                y = y - 100

            # This is the tall barrier
            self.rectArr.append(py.Rect(275, 150, 8, settings.HEIGHT - 150))

            # Next set of platforms, leading to the end of the level
            x = 400
            y = settings.HEIGHT
            for i in range(7):
                    x += 100
                    y -= 100
                    # Rectangles are defined with the surface, color, (x, y, width, height)
                    self.rectArr.append(py.Rect(x, y, 50, 8))

            # Platform on which the ending rect is "on"
            self.rectArr.append(py.Rect(1300, 150, 100, 8))

            # Rectangle that transports player to next level
            self.rectArr.append(py.Rect(self.endingCoords[0], self.endingCoords[1], 20, 20))

            self.firstDraw = False

    def lvltwo(self):

        # If it is the first time drawing the level, clear the rectArr
        if self.firstDraw:
            self.rectArr.clear()
            self.spawnCoords = (1, 125)
            # Starting platform
            self.rectArr.append(py.Rect(0, 150, 75, 8))

            # First hazard wall
            self.hazardArr.append(py.Rect(300, 0, 8, settings.HEIGHT - 175))
            self.hazardArr.append(py.Rect(300, settings.HEIGHT - 125, 8, settings.HEIGHT - 125))

            # Platforms leading up to spiral
            y = settings.HEIGHT - 125
            for i in range(5):
                # Alternating platforms left and right
                if i % 2 == 0:
                    x = 450
                else:
                    x = 300
                # Add rect to list
                self.rectArr.append(py.Rect(x, y, 50, 8))
                # Raise the next platform
                y -= 125

            self.firstDraw = False

    def lvlthree(self):
        pass

    # return the current level
    def currlevel(self):
        return self.levelcnt

    def checkcollision(self):
        import main
        play = main.game.player

        for rect in self.rectArr:
            # The player is reached through main because it needs to be the instantiated player object
            if rect.colliderect(main.game.player.rect):
                # If it is the first level, and the player has collided with the portal rect
                # Change the level, and signify that it is the first drawing of the new level
                if self.levelcnt == 1 and rect.x == self.endingCoords[0] and rect.y == self.endingCoords[1]:
                    self.levelcnt = 2
                    self.firstDraw = True

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





