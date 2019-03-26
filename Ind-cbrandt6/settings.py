
import pygame

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
FPS = 60

# Window title
TITLE = "Extreme Platformer"

# Player size
playerSize = 20

floorYCoord = HEIGHT - playerSize - 10


# Physics attributes
ACC = 8
FRIC = -1
GRAV = -10
JUMP = 11

# Create a clock
Clock = pygame.time.Clock()

dt = 0



