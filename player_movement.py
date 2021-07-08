import pygame


class PlayerMovement:
    """Player pygame Surface object. Movement based on coordinate grid of pygame display

    Attributes:
        Image:
          - player_img: pygame Image, .png drawn in pixels
        Position:
          - player_x: x position
          - player_y: y position
        Velocity:
          - player_vx: speed of x change
          - player_vy: speed of y change

    Functions:
        clip(): Prevents object from moving out of bounds
        move(): Moves object by velocity
        hit_by_alien(): Checks if object has been hit by an alien
        draw(): Draw object on pygame display

    """

    def __init__(self, player_x: float, player_y: float, player_vx: float, player_vy: float,
                 player_img: pygame.Surface, screen_dim: tuple):
        self.player_x = (screen_dim[0] / 2) - (self.player_img.get_width() / 2)
        self.player_y = (screen_dim[1] / 4) + (screen_dim[1] / 2)
        self.player_vx = 0
        self.player_vy = 0
        self.player_img = player_img
        self.width = self.player_img.get_width()
        self.height = self.player_img.get_height()
        self.max_x = screen_dim[0] - self.width
        self.min_x = 0
        self.max_y = screen_dim[1] - self.height
        self.min_y = screen_dim[1] / 2

    def get_x(self):
        return self.player_x

    def get_y(self):
        return self.player_y

    def get_vx(self):
        return self.player_vx

    def get_vy(self):
        return self.player_vy

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_x(self, x):
        self.player_x = x

    def set_y(self, y):
        self.player_y = y

    def set_vx(self, vx):
        self.player_vx = vx

    def set_vy(self, vy):
        self.player_vy = vy

    def clip(self):
        """Prevents the object from going outside of the bounds of the bounds of the area designated for the object.
        (i.e. Object cannot go outside of the active area the user defines for it)
        """
        if self.player_x < self.min_x:
            self.player_x = self.min_x
        elif self.player_x > self.max_x:
            self.player_x = self.max_x
        else:
            self.player_x = self.player_x
        if self.player_y < self.min_y:
            self.player_y = self.min_y
        elif self.player_y > self.max_y:
            self.player_y = self.max_y
        else:
            self.player_y = self.player_y

    def move(self):
        """Move object by velocity"""
        self.player_x += self.player_vx
        self.player_y += self.player_vy
        self.clip()

    def hit_by_alien(self, alien):
        """Determines if player was hit by an alien
        Collision is determined by comparing bounding boxes.
        If the bounding boxes overlap, then a collision is considered to occur

        :param alien:
        :return: True if objects intersects, False otherwise
        """
        return (self.player_x + self.width >= alien.get_x()
                and self.player_y + self.height >= alien.get_y()
                and alien.get_x() + alien.get_width() >= self.player_x
                and alien.get_y() + alien.get_height() >= self.player_y)

    # def draw(self, screen: pygame.display):
    #     """Default draw method that provides how the object should be drawn in the pygame display.
    #     This method does not draw anything. Subclass should override this method based on their object should appear.
    #
    #     :return: error if not implemented by subclass
    #     """
    #     raise NotImplementedError()
