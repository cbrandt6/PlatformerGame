
import settings
import math


vec = settings.Py.math.Vector2


class Player(settings.Py.sprite.Sprite):

    def __init__(self):
        settings.Py.sprite.Sprite.__init__(self)

        # Create player size and load image for player
        self.image = settings.Py.Surface((settings.playerSize, settings.playerSize))
        self.rect = self.image.get_rect()
        self.image = settings.Py.image.load('Square.png')

        # Initialize player vectors
        # Position is initialized so that sprite is aligned in the bottom left corner of the blue square
        self.position = vec(0, settings.HEIGHT)
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)
        self.keys = ''
        self.col = ''
        self.onPlat = False
        self.deathCount = 0

    def update(self):

        # Default the acceleration to 0
        # Otherwise the sprite will oscillate when no keys are pressed
        self.acceleration = vec(0, 0)

        # Player velocity depending on which keys are pressed
        self.keys = settings.Py.key.get_pressed()

        # Motion in the x axis
        if self.keys[settings.Py.K_a]:
            self.acceleration.x = -settings.ACC

        if self.keys[settings.Py.K_d]:
            self.acceleration.x = settings.ACC

        # Motion in the y axis
        if self.keys[settings.Py.K_SPACE]:
            self.jump()

        if self.keys[settings.Py.K_ESCAPE]:
            settings.Py.quit()

        self.physiccalc()

    def jump(self):

        import screen
        # If the player does not have a positive y acc then they are on a platform

        if self.position.y >= settings.floorYCoord or self.onPlat:
            # print("y acc= ", self.acceleration.y)
            self.velocity.y = -settings.JUMP
            self.onPlat = False

    def physiccalc(self):

        # print(col)
        # Using physics equations for motion
        # Applies friction and creates a max speed

        # -------------- X Motion -------------- #
        # a = v * friction
        # The player has not hit the side of a platform motion as normal
        if self.col != 2 and self.col != 3:
            self.acceleration.x += self.velocity.x * settings.FRIC
            # print("Xaccel = ", self.acceleration.x)

            # vf = vi + at
            self.velocity.x += self.acceleration.x * settings.dt

            # dX = v * dt + 1/2at^2
            # Velocity was already multiplied by time
            self.position.x += self.velocity.x + (0.5 * self.acceleration.x * math.pow(settings.dt, 2))
        # The player has hit the side of a platform
        # Stop the x velocity and acceleration
        elif self.col == 2 or self.col == 3:
            self.velocity.x = 0
            self.acceleration.x = 0
            if self.col == 2:
                self.position.x += -2
                self.acceleration.x = -1
            elif self.col == 3:
                self.position.x += 2
                self.acceleration.x = 1
        # -------------- X Motion -------------- #

        # -------------- Y Motion -------------- #
        # print("y pos= ", self.position.y)
        # If the y position is not on the ground or a platform continue to accelerate downwards
        # col = 1 means player is on top of a plat, 0 means they have hit the bottom
        if self.position.y < settings.floorYCoord and self.col != 1:
            self.acceleration.y = -settings.GRAV
            self.velocity.y += self.acceleration.y * settings.dt
            # print("y vel= ", self.velocity.y)
            self.position.y += self.velocity.y + (0.5 * self.acceleration.y * math.pow(settings.dt, 2))

        else:
            # a = v * gravity
            self.acceleration.y = -settings.GRAV
            # print("Yaccel = ", self.acceleration.y)

            # vf = vi + at
            self.velocity.y += self.acceleration.y * settings.dt
            # print("Yvel =", self.velocity.y)

            # dY = v * dt + 1/2at^2
            # Velocity was already multiplied by time
            self.position.y += self.velocity.y + (0.5 * self.acceleration.y * math.pow(settings.dt, 2))

        if self.col == 1:
            self.velocity.y = 0
            self.onPlat = True
        elif self.col == -1:
            self.onPlat = False

        # print("Yvel =", self.velocity.y)
        # print("Yaccel = ", self.acceleration.y)
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


