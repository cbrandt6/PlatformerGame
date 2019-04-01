import pygame as Py
import settings
import math


vec = Py.math.Vector2


class Player(Py.sprite.Sprite):

    def __init__(self):
        Py.sprite.Sprite.__init__(self)

        # Create player size and load image for player
        self.image = Py.Surface((settings.playerSize, settings.playerSize))
        self.rect = self.image.get_rect()
        self.image = Py.image.load('Square.png')


        # Initialize player vectors
        # Position is initialized so that sprite is aligned in the bottom left corner of the blue square
        self.position = vec(0, settings.HEIGHT)
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)
        self.keys = ''

    def update(self):

        # Default the acceleration to 0
        # Otherwise the sprite will oscillate when no keys are pressed
        self.acceleration = vec(0, 0)

        # Player velocity depending on which keys are pressed
        self.keys = Py.key.get_pressed()

        # Motion in the x axis
        if self.keys[Py.K_a]:
            self.acceleration.x = -settings.ACC

        if self.keys[Py.K_d]:
            self.acceleration.x = settings.ACC

        # Motion in the y axis
        if self.keys[Py.K_SPACE]:
            self.jump()

        self.physiccalc()

    def jump(self):

        import screen
        # If the player does not have a positive y acc then they are on a platform
        if self.position.y >= settings.floorYCoord or screen.checkcollision() == 1:
            # print("y acc= ", self.acceleration.y)
            self.velocity.y = -settings.JUMP

    def physiccalc(self):
        import screen
        col = screen.checkcollision()
        print(col)
        # Using physics equations for motion
        # Applies friction and creates a max speed

        # -------------- X Motion -------------- #
        # a = v * friction
        # TODO If the player hits the sides of a platform stop the x motion
        # The player has not hit the side of a platform motion as normal
        if col != 2 and col != 3:
            self.acceleration.x += self.velocity.x * settings.FRIC
            # print("Xaccel = ", self.acceleration.x)

            # vf = vi + at
            self.velocity.x += self.acceleration.x * settings.dt
            # print("Xvel =", self.velocity.x)

            # dX = v * dt + 1/2at^2
            # Velocity was already multiplied by time
            self.position.x += self.velocity.x + (0.5 * self.acceleration.x * math.pow(settings.dt, 2))
        # The player has hit the side of a platform
        # Stop the x velocity and acceleration
        elif col == 2 or col == 3:
            self.velocity.x = 0
            self.acceleration.x = 0
            if col == 2:
                self.position.x += -2
                self.acceleration.x = -1
            elif col == 3:
                self.position.x += 2
                self.acceleration.x = 1
        # -------------- X Motion -------------- #

        # -------------- Y Motion -------------- #
        # print("y pos= ", self.position.y)
        # If the y position is not on the ground or a platform continue to accelerate downwards
        # TODO If the player hit the top or bottom of the platform stop their y motion
        # col = 1 means player is on top of a plat, 0 means they have hit the bottom
        if self.position.y < settings.floorYCoord and col != 1:
            self.acceleration.y = -settings.GRAV
            self.velocity.y += self.acceleration.y * settings.dt
            # print("y vel= ", self.velocity.y)
            self.position.y += self.velocity.y + (0.5 * self.acceleration.y * math.pow(settings.dt, 2))

        else:
            # a = v * gravity
            self.acceleration.y += self.velocity.y * settings.GRAV
            # print("Yaccel = ", self.acceleration.y)

            # vf = vi + at
            self.velocity.y += self.acceleration.y * settings.dt
            # print("Yvel =", self.velocity.y)

            # dY = v * dt + 1/2at^2
            # Velocity was already multiplied by time
            self.position.y += self.velocity.y + (0.5 * self.acceleration.y * math.pow(settings.dt, 2))

        if col == 1 or col == 0:
            self.velocity.y = 0
            self.acceleration.y = 0
        # -------------- Y Motion -------------- #

        # ----- Keep Sprite within the screen ----- #
        # Keeps sprite from falling through floor
        if self.position.y > settings.floorYCoord:
            self.position.y = settings.floorYCoord
        # Keep sprite from going through the top
        if self.position.y < 0:
            self.position.y = 0

            # Keep the sprite from moving through the sides
        if self.position.x > settings.WIDTH - settings.playerSize:
            self.position.x = settings.WIDTH - settings.playerSize
        if self.position.x < 0:
            self.position.x = 0
        # ----- Keep Sprite within the screen ----- #

        # Update the position
        # Update the positions separately so self.rect remains a rectangle
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        # print(self.rect.x)


