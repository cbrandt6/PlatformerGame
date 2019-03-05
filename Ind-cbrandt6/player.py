import pygame as Py
import settings



class Player(Py.sprite.Sprite):

    def __init__(self):
        Py.sprite.Sprite.__init__(self)

        # Create player size and load image for player
        self.image = Py.Surface((settings.playerSize, settings.playerSize))
        # self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.image = Py.image.load('Square.png')

        # Initialize player velocity in x and y
        self.playerVX = 0
        self.playerVY = 0

    def update(self):

        # Player velocity depending on which keys are pressed
        self.keys = Py.key.get_pressed()

        if self.keys[Py.K_a]:
            self.playerVX = -settings.VELOCITY

        if self.keys[Py.K_d]:
            self.playerVX = settings.VELOCITY

        if self.keys[Py.K_w]:
            self.playerVY = -settings.VELOCITY

        if self.keys[Py.K_s]:
            self.playerVY = settings.VELOCITY

        # Add the velocity to the rectangle X and Y
        self.rect.x += self.playerVX * settings.Clock.get_time() / 1000  # DT
        self.rect.y += self.playerVY * settings.Clock.get_time() / 1000  # DT

        # This is the player friction
        # If the velocity is not 0 it will be decremented until it is 0
        # Player VX
        if self.playerVX > 0:
            self.playerVX -= settings.DECELERATION
        elif self.playerVX < 0:
            self.playerVX += settings.DECELERATION

        # Player VY
        if self.playerVY > 0:
            self.playerVY -= settings.DECELERATION
        elif self.playerVY < 0:
            self.playerVY += settings.DECELERATION
