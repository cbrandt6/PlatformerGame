import pygame as PY
from settings import *


class Player(PY.sprite.Sprite):

    def __init__(self):
        PY.sprite.Sprite.__init__(self)

        # Create player size and load image for player
        self.image = PY.Surface((playerSize, playerSize))
        # self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.image = PY.image.load('Square.png')

        # Initialize player velocity in x and y
        self.playerVX = 0
        self.playerVY = 0

    def update(self):

        # Player velocity depending on which keys are pressed
        self.keys = PY.key.get_pressed()

        if self.keys[PY.K_a]:
            self.playerVX = -VELOCITY

        if self.keys[PY.K_d]:
            self.playerVX = VELOCITY

        if self.keys[PY.K_w]:
            self.playerVY = -VELOCITY

        if self.keys[PY.K_s]:
            self.playerVY = VELOCITY

        # Add the velocity to the rectangle X and Y
        self.rect.x += self.playerVX
        self.rect.y += self.playerVY

        # This is the player friction
        # If the velocity is not 0 it will be decremented until it is 0
        # Player VX
        if self.playerVX > 0:
            self.playerVX -= 1
        elif self.playerVX < 0:
            self.playerVX += 1

        # Player VY
        if self.playerVY > 0:
            self.playerVY -= 1
        elif self.playerVY < 0:
            self.playerVY += 1
