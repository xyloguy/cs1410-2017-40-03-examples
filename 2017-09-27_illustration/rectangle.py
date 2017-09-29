import pygame
class Rectangle:
    def __init__(self, width, height, x, y, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getX(self):
        return self.x

    def setX(self, newx):
        self.x = newx

    def getY(self):
        return self.y

    def setY(self, newy):
        self.y = newy

    def getColor(self):
        return self.color

    def setColor(self, r, g, b):
        self.color = (r, g, b)


    def paint(self, surface):
        rect = pygame.Rect(self.getX(), self.getY(), self.getWidth(), self.getHeight())
        pygame.draw.rect(surface, self.getColor(), rect)