import pygame

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.r = radius
        self.color = color

    def getPos(self):
        return (self.x, self.y)

    def getRadius(self):
        return int(self.r)

    def getColor(self):
        return self.color

    def paint(self, surface):
        pygame.draw.circle(surface, self.getColor(), self.getPos(), self.getRadius())