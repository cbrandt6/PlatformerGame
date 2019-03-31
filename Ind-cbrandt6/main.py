import pygame as Py
from pygame.locals import *

from player import *
import settings
import screen


class Game:
    # Initialize game window

    def __init__(self):
        Py.init()
        # Initialize game loop variable
        self.play = True

        # Initialize the level
        # Creates a screen object
        self.level = screen.levels()

        # Create sprite group
        self.sprites = Py.sprite.Group()

        # Create the player
        # Player.__init__(self)
        self.player = Player()

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
        # print(settings.Clock.get_fps())

    # Handle game loop events
    def events(self):
        # Event handler to see if game has been closed
        for event in Py.event.get():
            if event.type == Py.QUIT:
                if self.play:
                    self.play = False
                self.run = False

    # Draw game things
    def draw(self):
        '''
        image = Py.Surface((settings.playerSize, settings.playerSize))
        image.fill(settings.BLUE)
        self.sprites.clear(self.level.DISPLAYSURF, image)
        '''
        self.level.redraw()
        self.sprites.draw(self.level.DISPLAYSURF)


    # Reset the game
    def new(self):
        # Creates new group of sprites
        self.sprites = Py.sprite.Group()
        # Creates new player
        self.player = Player()
        # Add player to sprite group
        self.sprites.add(self.player)
        # Run
        self.run()

    # Game Over screen
    def gameOver(self):
        pass


game = Game()
game.new()
Py.quit()


