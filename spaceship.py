import player_movement
import pygame


class Spaceship(player_movement.PlayerMovement):
    """Subclass of PlayerMovement class

    """
    player_img: pygame.Surface = pygame.image.load('graphics/spacecraft.png')

    def __init__(self, screen_dim: tuple):
        self.screen_dim = screen_dim
        player_x = (self.screen_dim[0] / 2) - (self.player_img.get_width() / 2)
        player_y = (self.screen_dim[1] / 4) + (self.screen_dim[1] / 2)
        player_vx = 0
        player_vy = 0

        super().__init__(player_x, player_y, player_vx, player_vy, self.player_img, screen_dim)

    def get_img(self):
        return self.player_img

    def get_img_dim(self):
        return self.player_img.get_width(), self.player_img.get_height()
