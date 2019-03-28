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
        self.image = Py.image.load('Square.png').convert()
        self.rect = (0, settings.HEIGHT)

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

        # Easy fix but
        # If the player does not have a positive y acc then they are on a platform
        if self.position.y >= settings.floorYCoord:
            # print("y acc= ", self.acceleration.y)
            self.velocity.y = -settings.JUMP

    def physiccalc(self):

        # Using physics equations for motion
        # Applies friction and creates a max speed
        # -------------- X Motion --------------
        # a = v * friction
        self.acceleration.x += self.velocity.x * settings.FRIC
        # print("Xaccel = ", self.acceleration.x)

        # vf = vi + at
        self.velocity.x += self.acceleration.x * settings.dt
        # print("Xvel =", self.velocity.x)

        # dX = v * dt + 1/2at^2
        # Velocity was already multiplied by time
        self.position.x += self.velocity.x + (0.5 * self.acceleration.x * math.pow(settings.dt, 2))

        # -------------- Y Motion --------------
        # print("y pos= ", self.position.y)
        # If the y position is not on the ground or a platform continue to accelerate downwards
        if self.position.y < settings.floorYCoord:
            self.acceleration.y = -settings.GRAV
            self.velocity.y += self.acceleration.y * settings.dt
            print("y vel= ", self.velocity.y)
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

        # Update the position
        self.rect = self.position


