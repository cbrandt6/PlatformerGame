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
        self.levelCnt = 1
        self.endingCoords = ()
        self.spawnCoords = ()
        self.firstDraw = True
        self.lvlone()

    def redraw(self):

        # Redraw the window
        self.DISPLAYSURF.fill(settings.BLACK)
        # print(self.firstDraw)

        if self.levelCnt == 1:
            self.lvlone()
        if self.levelCnt == 2:
            self.lvltwo()

        # If it is not the first time drawing the level, don't keep redrawing the rectangles
        if not self.firstDraw:
            for i in self.rectArr:
                # Check to see if the rectangle is the one that ends the level, and if it is paint it green
                if i.left == self.endingCoords[0] and i.top == self.endingCoords[1]:
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
        self.spawnCoords = (3, settings.HEIGHT - settings.playerSize - 10)
        self.endingCoords = (1340, 50)
        if self.firstDraw:
            # Clear the rectangle list in case there are leftovers from something
            self.rectArr.clear()

            # Initial height of the platforms
            y = settings.HEIGHT - 100

            for i in range(7):

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
            self.levelChange = False
            self.firstDraw = False

    def lvltwo(self):
        self.endingCoords = (1200, 400)
        self.spawnCoords = (5, 5)
        # If it is the first time drawing the level, clear the rectArr
        if self.firstDraw:
            self.rectArr.clear()
            self.hazardArr.clear()
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
            # Bottom part of second hazard wall
            self.hazardArr.append(py.Rect(550, y, 8, settings.HEIGHT - y))
            # Top part
            self.hazardArr.append(py.Rect(550, 0, 8, y - settings.playerSize - 30))

            # Creating the spiral
            # top platform of spiral
            self.rectArr.append(py.Rect(558, y, 800, 8))
            # bottom part of spiral
            self.rectArr.append(py.Rect(558, settings.HEIGHT - 200, settings.WIDTH - 558, 8))
            # Right wall of spiral
            self.rectArr.append(py.Rect(550 + 800, y + 8, 8, settings.HEIGHT - 450))
            self.hazardArr.append(py.Rect(1358, y + 5, 8, 453))

            # Second layer bottom of the spiral
            self.rectArr.append(py.Rect(675, settings.HEIGHT - 300, 675, 8))
            # Left side of spiral
            self.rectArr.append(py.Rect(675, y + 100, 8, 350))
            # Platforms left of spiral
            l = y + 425
            for g in range(3):
                if g % 2 == 1:
                    k = 650
                    w = 55
                else:
                    k = 550
                    w = 40

                self.rectArr.append(py.Rect(k, l, w, 8))
                l -= 100

            # Top of inside of spiral
            self.rectArr.append(py.Rect(675, y + 100, 575, 8))

            # Inner right side
            self.rectArr.append(py.Rect(1250, y + 100, 8, 250))
            self.hazardArr.append(py.Rect(1258, y + 100, 8, 258))
            # 3rd bottom
            self.rectArr.append(py.Rect(783, y + 350, 475, 8))

            # Adding hazards to the spiral
            # Hazard by the ending
            self.hazardArr.append(py.Rect(1000, 400, 8, 100))
            # Hazard along right side of screen
            self.hazardArr.append(py.Rect(settings.WIDTH - 8, y, 8, 550))
            self.hazardArr.append(py.Rect(550 + 792, y + 8, 8, settings.HEIGHT - 458))
            self.hazardArr.append(py.Rect(683, settings.HEIGHT - 330, 30, 30))
            # Ending rect for level 2
            self.rectArr.append(py.Rect(self.endingCoords[0], self.endingCoords[1], 20, 20))
            self.firstDraw = False

    def lvlthree(self):
        self.endingCoords = (20, settings.HEIGHT - 400)
        self.spawnCoords = (5, settings.HEIGHT - 105 - settings.playerSize)
        # If it is the first time drawing the level, clear the rectArr
        if self.firstDraw:
            self.rectArr.clear()
            self.hazardArr.clear()

            # Hazard along bottom
            self.hazardArr.append(py.Rect(0, settings.HEIGHT - 8, settings.WIDTH, 8))

            # Starting platform
            self.rectArr.append(py.Rect(0, settings.HEIGHT - 100, 50, 8))

            # Next platform, as well as the hazard on its side
            self.rectArr.append(py.Rect(250, settings.HEIGHT - 225, 50, 8))
            self.hazardArr.append(py.Rect(292, settings.HEIGHT - 245, 8, 20))

            # Platform with hazard on left side
            self.rectArr.append(py.Rect(400, settings.HEIGHT - 340, 50, 8))
            self.hazardArr.append(py.Rect(400, settings.HEIGHT - 350, 8, 10))

            # Platform with hazards on both ends
            self.rectArr.append(py.Rect(600, settings.HEIGHT - 200, 75, 8))
            self.hazardArr.append(py.Rect(600, settings.HEIGHT - 217, 8, 17))
            self.hazardArr.append(py.Rect(667, settings.HEIGHT - 217, 8, 17))

            # Platform where player chooses path
            self.rectArr.append(py.Rect(800, settings.HEIGHT - 300, 150, 8))

            # Right Path
            self.rectArr.append((py.Rect(1100, settings.HEIGHT - 300, 150, 8)))

            # Hazard walls
            self.hazardArr.append(py.Rect(1100, 75, 8, (settings.HEIGHT - 300) - 150))
            self.hazardArr.append(py.Rect(1250, 75, 8, (settings.HEIGHT - 300) - 150))

            # Alternating platforms
            # Platforms get smaller by 10 px
            w = 60
            h = (settings.HEIGHT - 300) - 100
            for i in range(5):
                if i % 2 == 0:
                    p = 1108
                else:
                    p = 1250 - w
                self.rectArr.append(py.Rect(p, h, w, 8))
                w -= 10
                h -= 100

            # Top platform
            self.rectArr.append(py.Rect(700, 75, 400, 8))

            # Left path
            self.rectArr.append(py.Rect(740, settings.HEIGHT - 400, 15, 8))
            self.rectArr.append(py.Rect(600, settings.HEIGHT - 500, 15, 8))
            self.hazardArr.append(py.Rect(600, settings.HEIGHT - 492, 15, 6))
            self.rectArr.append(py.Rect(400, settings.HEIGHT - 500, 15, 8))
            self.rectArr.append(py.Rect(350, settings.HEIGHT - 600, 15, 8))
            # Joining platform
            self.rectArr.append(py.Rect(450, 150, 100, 8))

            # Ending chute
            # Hazards on either side of the ending
            self.hazardArr.append(py.Rect(0, 75, 10, self.endingCoords[1] - 55))
            self.hazardArr.append(py.Rect(50, 75, 10, self.endingCoords[1] - 55))
            self.hazardArr.append(py.Rect(0, self.endingCoords[1] + 20, 60, 10))

            # Caps
            self.rectArr.append(py.Rect(0, 67, 10, 8))
            self.rectArr.append(py.Rect(50, 67, 250, 8))

            # Ending rect
            self.rectArr.append(py.Rect(self.endingCoords[0], self.endingCoords[1], 20, 20))

            self.firstDraw = False

    def lvlfour(self):
        self.endingCoords = (20, settings.HEIGHT - 400)
        self.spawnCoords = (1450, 30)
        # If it is the first time drawing the level, clear the rectArr
        if self.firstDraw:
            self.rectArr.clear()
            self.hazardArr.clear()

            # Hazard along bottom
            self.hazardArr.append(py.Rect(0, settings.HEIGHT - 8, settings.WIDTH, 8))

            # spawn platform
            self.rectArr.append(py.Rect(1430, 80, 70, 8))
            self.hazardArr.append(py.Rect(1300, 0, 8, 300))

            # Second platform
            self.rectArr.append(py.Rect(1350, 300, 150, 8))

            # third plat
            self.rectArr.append(py.Rect(1280, 330, 50, 8))
            self.hazardArr.append(py.Rect(1200, 230, 8, 110))
            self.hazardArr.append(py.Rect(1170, 250, 8, 90))
            self.hazardArr.append(py.Rect(1230, 250, 8, 90))

            # Fourth plat
            self.rectArr.append(py.Rect(1080, 330, 50, 8))
            # Hazard under third and fourth plats
            self.hazardArr.append(py.Rect(875, 338, 455, 8))

            # vertical hazard after fourth
            self.hazardArr.append(py.Rect(875, 200, 8, 138))

            # Fifth plat
            self.rectArr.append(py.Rect(825, 200, 50, 8))

            # hazard above 5th plat
            self.hazardArr.append(py.Rect(750, 150, 200, 8))
            # beside
            self.hazardArr.append(py.Rect(742, 150, 8, 258))

            # Sixth plat
            self.rectArr.append(py.Rect(750, 400, 200, 8))
            self.hazardArr.append(py.Rect(950, 408, 50, 8))
            # 7th plat
            self.rectArr.append(py.Rect(1100, 500, 40, 8))

            self.hazardArr.append(py.Rect(1025, 550, 8, 100))
            # 8th plat
            self.rectArr.append(py.Rect(900, 650, 40, 8))

            # stair case
            x = 700
            y = 650

            for i in range(5):
                self.rectArr.append(py.Rect(x, y, 20, 8))
                self.hazardArr.append(py.Rect(x - 50, y - 100, 8, 100))
                if i != 3:
                    x -= 100
                    y -= 100

                else:
                    x -= 200

            # Ending rect
            self.rectArr.append(py.Rect(self.endingCoords[0], self.endingCoords[1], 20, 20))

            self.firstDraw = False

    def lvlfive(self):
        self.hazardArr.clear()
        self.rectArr.clear()
        self.spawnCoords = (0, 0)


    # Makes the call to draw the next level when the player has collided with the ending rect
    def nextlevel(self):
        if self.levelCnt == 1:
            self.lvlone()
        elif self.levelCnt ==2:
            self.lvltwo()
        elif self.levelCnt == 3:
            self.lvlthree()
        elif self.levelCnt == 4:
            self.lvlfour()
        elif self.levelCnt == 5:
            self.lvlfive()

    def checkcollision(self):
        # -1 is no collision, -2 is the ending rectangle
        # 0-3 will represent collision with platforms, 4 is a collision with a hazard

        import main
        play = main.game.player
        collisionnumber = -1
        for rect in self.rectArr:
            # The player is reached through main because it needs to be the instantiated player object
            if rect.colliderect(main.game.player.rect):
                # If it is the first level, and the player has collided with the portal rect
                # Change the level, and signify that it is the first drawing of the new level
                # took out "self.levelcnt == 1 and" to test if it needs to be there
                if rect.x == self.endingCoords[0] and rect.y == self.endingCoords[1]:
                    # Update the level count
                    self.levelCnt += 1
                    # Indicate it is the first drawing of the level
                    self.firstDraw = True
                    # Make the call to draw the next level
                    self.nextlevel()
                    collisionnumber = 5

                # If there is a collision there is no need to continue through the rest of the list
                # If the player collides with the bottom of the platform, return 0, return 1 for the top
                # Return 2 for the left side, and 3 for the right side

                # Player has hit the bottom
                elif play.rect.top - 1 < rect.bottom + 1 < play.rect.bottom + 1:
                    play.position.y = rect.bottom + 1
                    collisionnumber = 0

                # Player has landed on the top
                elif play.rect.bottom + 1 >= rect.top - 1 > play.rect.top - 1:
                    play.position.y = rect.top - settings.playerSize + 1
                    collisionnumber = 1

                # If the right side of the player is equal to the left side of the platform
                elif play.rect.right + 1 > rect.left - 1 > play.rect.left - 1:
                    play.position.x = rect.left - settings.playerSize + 1
                    collisionnumber = 2

                # If the left side of the player is equal to the right side of the platform
                elif play.rect.left - 1 < rect.right + 1 < play.rect.right + 1:
                    play.position.x = rect.right - 1
                    collisionnumber = 3

        for rect in self.hazardArr:
            if rect.colliderect(main.game.player.rect):
                # Need to stop the player's motion otherwise they shoot downward
                main.game.player.acceleration.y = 0
                main.game.player.acceleration.x = 0
                main.game.player.velocity.y = 0
                main.game.player.velocity.x = 0
                collisionnumber = 4

        return collisionnumber

    # text_objects and message_display were taken from:
    # https://pythonprogramming.net/displaying-text-pygame-screen/

    def text_objects(self, text, font):
        textSurface = font.render(text, True, settings.WHITE)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, x ,y):
        largeText = py.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (x, y)
        self.DISPLAYSURF.blit(TextSurf, TextRect)

