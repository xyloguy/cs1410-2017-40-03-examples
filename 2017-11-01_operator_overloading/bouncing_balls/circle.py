from math import pi
import pygame
from config import *

class Circle:
    def __init__(self, radius, x, y, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.dx = 0
        self.dy = 0

    def get_radius(self):
        return self.radius

    def get_area(self):
        return pi * self.get_radius() ** 2

    def get_circumference(self):
        return 2 * pi * self.get_radius()

    def __gt__(self, other):
        return self.get_radius() > other.get_radius()

    def __eq__(self, other):
        if self > other:
            return False # can't be great than the other
        if other > self:
            return False # can't be smaller than the other

        return True

    def __lt__(self, other):
        if self > other:
            return False # can't be greater than the other
        if self == other:
            return False # can't be equal to the other

        return True

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return 'Circle({}, {}, {}, {})'.format(self.radius, self.x, self.y, self.color)

    def __repr__(self):
        return str(self)

    def move(self):
        self.x += self.dx
        if self.x <= 0:
            self.dx = -self.dx
            self.x = 0

        if self.x + self.radius >= WIDTH:
            self.dx = -self.dx
            self.x = WIDTH - self.radius

        self.y += self.dy
        if self.y <= 0:
            self.dy = -self.dy
            self.y = 0

        if self.y + self.radius >= HEIGHT:
            self.dy = -self.dy
            self.y = HEIGHT-self.radius

    def paint(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
