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

        self.rect = (settings.HEIGHT - settings.playerSize, 0)
        # Initialize player vectors
        self.position = vec(0, settings.HEIGHT - settings.playerSize)
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)

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

        # Using physics equations for motion
        # Applies friction and creates a max speed

        # a = v * friction
        self.acceleration += self.velocity * settings.FRIC
        print("accel = ", self.acceleration)

        # vf = vi + at
        self.velocity += self.acceleration * settings.dt
        print("vel =", self.velocity)

        # dX = v * dt + 1/2at^2
        # Velocity was already multiplied by time
        self.position += self.velocity + (0.5 * self.acceleration * math.pow(settings.dt, 2))

        # Update the position
        self.rect = self.position
