import pygame

class Triangle:
    def __init__(self, points, color):
        self.points = points[:3]
        self.color = color

    def getPoints(self):
        return self.points

    def getColor(self):
        return self.color

    def paint(self, surface):
        # draws the outline
        pygame.draw.polygon(surface, self.getColor(), self.getPoints())
