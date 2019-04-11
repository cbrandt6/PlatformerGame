from player import *
from settings import *
import screen


class Game:
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

        # self.run = True
        while self.play:

            # print("fps =", settings.Clock.get_fps())
            # Check for events
            self.events()

            # Update based on those events
            self.update()

            # Draw the new screen
            self.draw()

    # Perform game loop updates
    def update(self):
        # If it is the first time entering the level or they collide with a hazard,
        # set the player position to the spawn location

        if self.level.firstDraw:
            self.player.position = self.level.spawnCoords

        # Check if the player has collided with any of the level rectangles
        collision = self.level.checkcollision()

        # If the player collided with a platform the player will handle it
        if collision < 4:
            self.player.col = collision

        # If the player collided with a hazard respawn them at the beginning of the level
        elif collision == 4:
            self.player.position.x = self.level.spawnCoords[0]
            self.player.position.y = self.level.spawnCoords[1]

        # If the level has changed spawn the player at the beginning of the level
        elif collision == -2:
            self.player.position.x = self.level.spawnCoords[0]
            self.player.position.y = self.level.spawnCoords[1]

        # update player sprite
        self.player.update()

        # Update the display
        Py.display.flip()

        # Tick clock
        settings.dt = settings.Clock.tick_busy_loop(settings.FPS) / 1000

        # print("dt =", settings.dt)
        # print(settings.Clock.get_fps())

    def events(self):
        # Event handler to see if game has been closed
        for event in Py.event.get():
            if event.type == Py.QUIT:
                if self.play:
                    self.play = False
                # self.run = False

    # Draw game things
    def draw(self):
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


