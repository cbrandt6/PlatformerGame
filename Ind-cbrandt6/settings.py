import pygame as Py

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Window size
HEIGHT = 900
WIDTH = 1500

# Set the FPS

FPS = 144

# Window title
TITLE = "Extreme Platformer"

# Player size
playerSize = 20

floorYCoord = HEIGHT - playerSize


# Physics attributes
ACC = 5.9
FRIC = -1
GRAV = -7
JUMP = 3.5

# Create a clock
Clock = Py.time.Clock()

dt = 0



