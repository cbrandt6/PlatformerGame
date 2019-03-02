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

        self.playerX = self.rect.x
        self.playerY = self.rect.y

    def update(self):
        self.keys = PY.key.get_pressed()

        if self.keys[PY.K_a]:
            self.playerVX = -5

        if self.keys[PY.K_d]:
            self.playerVX = 5

        if self.keys[PY.K_w]:
            self.playerVY = -5

        if self.keys[PY.K_s]:
            self.playerVY = 5

        self.rect.x += self.playerVX
        self.rect.y += self.playerVY
