
import pygame
import constant_movement


class Alien(constant_movement.ConstantMovement):
    """

    """

    img: pygame.Surface = pygame.image.load('graphics/alien.png')

    def __init__(self, screen_dim):
        self.screen_dim = screen_dim
        super().__init__(self.img, screen_dim)

        self.set_x(self.get_random_x())
        self.set_vy(self.get_random_velocity())

    def get_img(self):
        return self.img

    def hit_by_bullet(self, bullet):
        """Determines if alien was hit by a player bullet
        Collision is determined by comparing bounding boxes.
        If the bounding boxes overlap, then a collision is considered to occur

        :param bullet:
        :return: True if objects intersects, False otherwise
        """
        return (self.x + self.width >= bullet.get_x()
                and self.y + self.height >= bullet.get_y()
                and bullet.get_x() + bullet.get_width() >= self.x
                and bullet.get_y() + bullet.get_height() >= self.y)
