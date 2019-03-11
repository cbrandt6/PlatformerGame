import pygame as Py
from pygame.locals import *

from player import *
import settings


class Game:
    # Initialize game window
    def __init__(self):
        # Initialize game loop variable
        self.play = True

        # Initialize pygame
        Py.init()

        # Create the display surface
        self.DISPLAYSURF = Py.display.set_mode((settings.WIDTH, settings.HEIGHT), 0, 32)

        # This is the title bar caption
        Py.display.set_caption(settings.TITLE)
        # Create sprite group
        self.sprites = Py.sprite.Group()
        # Create the player
        self.player = Player.__init__(self)

    # Main game loop
    def run(self):

        self.run = True
        while self.run:

            # print("fps =", settings.Clock.get_fps())
            # Check for events
            self.events()

            # Update based on those events
            self.update()

            # Draw the new screen
            self.draw()


    # Perform game loop updates
    def update(self):
        # update sprites
        self.sprites.update()
        # Update the display
        Py.display.update()
        # Tick clock
        settings.dt = settings.Clock.tick(settings.FPS) / 1000
        # print("dt =", settings.dt)

    # Handle game loop events
    def events(self):
        # Event handler to see if game has been closed
        for event in Py.event.get():
            if event.type == Py.QUIT:
                if self.play:
                    self.play = False
                self.run = False

    # Draw game loop things
    def draw(self):
        # Redraw the window
        self.DISPLAYSURF.fill(settings.BLACK)
        # This is just kinda style rectangle
        Py.draw.rect(self.DISPLAYSURF, settings.BLUE, (10, 10, 880, 780))
        self.sprites.draw(self.DISPLAYSURF)

    # Reset the game
    def new(self):

        self.sprites = Py.sprite.Group()
        self.player = Player()
        self.sprites.add(self.player)
        self.run()

    # Game Over screen
    def gameOver(self):
        pass


game = Game()
game.new()


Py.quit()


