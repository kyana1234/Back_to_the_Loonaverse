import pygame
import constant_movement


class Bullet(constant_movement.ConstantMovement):
    """Projectiles that the players shoot to destroy the aliens.
    Subclass of ConstantMovement

    Attributes:
         Please reference constant_movement.py for attributes

    Functions:
        get_img()
    """

    img: pygame.Surface = pygame.image.load('graphics/star.png')

    def __init__(self, screen_dim, player_x: float, player_y: float, player_img_dim: tuple):
        self.screen_dim = screen_dim
        super().__init__(self.img, screen_dim)

        # Shifted x,y based on how the bullets were drawn relative to spaceship in GUI testing.
        self.set_x(player_x + (player_img_dim[0] / 2) - 10)
        self.set_y(player_y - (player_img_dim[1] / 2) + 5)
        # Default y-velocity
        self.set_vy(-5)  # Upward motion is negative y-velocity.

    def get_img(self):
        return self.img
