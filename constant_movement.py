import pygame
import random


class ConstantMovement:
    """Player pygame Surface object. Movement based on coordinate grid of pygame display

    Attributes:
        Image:
          - img: pygame Image, .png drawn in pixels
        Position:
          - x: x position
          - y: y position
        Velocity:
          - vx: speed of x change
          - vy: speed of y change

    Functions:
        clip(): Prevents object from moving out of bounds
        move(): Moves object by velocity
        hit_by_alien(): Checks if object has been hit by an alien
        draw(): Draw object on pygame display

    """

    def __init__(self, img: pygame.Surface, screen_dim: tuple):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.max_x = screen_dim[0]
        self.maxY = screen_dim[1] - self.img.get_height()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_vx(self, vx):
        self.vx = vx

    def set_vy(self, vy):
        self.vy = vy

    # Random Variable Generators
    def get_random_x(self):
        return int(round(self.max_x * random.random()))

    @staticmethod
    def get_random_velocity():
        return random.random() + 3

    def move(self):
        """Move object by velocity"""
        self.x += self.vx
        self.y += self.vy

    def reach_end(self):
        """Checks to see if object has reached the end of the screen (top/bottom).
        Aliens can only move downwards; bullets can only move upwards.


        :return: True if reached the end of screen, otherwise False
        """
        if self.y + self.vy > self.maxY:
            return True
        elif self.y + self.vy < 0:
            return True
        else:
            return False
