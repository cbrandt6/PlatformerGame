
import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Window size
HEIGHT = 800
WIDTH = 900

# Set the FPS
# Unused
FPS = 100

# Window title
TITLE = "Extreme Platformer"

# Player size
playerSize = 20

# Standard velocity
VELOCITY = 100

#Deceleration constant
DECELERATION = 10

# Create a clock
Clock = pygame.time.Clock()

# Since clock.get_time does not like to be stored in a variable,
# DT is calculated as clock.get_time() / 1000 when it is needed

