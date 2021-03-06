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

        # Check if the player has collided with any of the level rectangles
        collision = self.level.checkcollision()
        # print(collision)
        # If the player collided with a platform the player will handle it
        if collision < 4:
            self.player.col = collision

        # If the player collided with a hazard respawn them at the beginning of the level
        elif collision == 4:
            self.player.position.x = self.level.spawnCoords[0]
            self.player.position.y = self.level.spawnCoords[1]
            # Increment the death count
            self.player.deathCount += 1
        elif collision == 5:
            self.player.position.x = self.level.spawnCoords[0]
            self.player.position.y = self.level.spawnCoords[1]

        # update player sprite
        self.player.update()

        # Update the display
        Py.display.flip()

        # Tick clock
        settings.dt = settings.Clock.tick_busy_loop(settings.FPS) / 1000

        # print("dt =", settings.dt)
        print(settings.Clock.get_fps())

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

        if self.level.levelCnt == 5:
            dthmsg = "You died " + str(self.player.deathCount) + " time(s)"
            self.level.message_display(dthmsg, (settings.WIDTH / 2), (settings.HEIGHT / 2) - 100)
            endmsg = "This concludes my Independent Project. Thank you for playing."
            self.level.message_display(endmsg, (settings.WIDTH / 2), (settings.HEIGHT / 2))
            exitmsg = "Press ESC to quit"
            self.level.message_display(exitmsg, (settings.WIDTH / 2), (settings.HEIGHT / 2) + 200)
        else:
            # Draws the player death count
            dth = "Death count: " + str(self.player.deathCount)
            self.level.message_display(dth, 1410, 20)
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


