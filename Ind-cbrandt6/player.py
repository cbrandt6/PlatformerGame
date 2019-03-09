import pygame as Py
import settings

vec = Py.math.Vector2


class Player(Py.sprite.Sprite):

    def __init__(self):
        Py.sprite.Sprite.__init__(self)

        # Create player size and load image for player
        self.image = Py.Surface((settings.playerSize, settings.playerSize))
        self.rect = self.image.get_rect()
        self.image = Py.image.load('Square.png')

        self.rect = (0, 0)
        # Initialize player vectors
        self.position = vec(0, 0)
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
        self.acceleration += self.velocity * settings.FRIC

        # Add acc to velocity and velocity equation to position
        self.velocity += self.acceleration
        self.position += self.velocity + (0.5 * self.acceleration)

        # Update the postion
        self.rect = self.position
