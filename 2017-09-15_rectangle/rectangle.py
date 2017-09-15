import math

class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        widths = self.getWidth() * 2
        heights = self.getHeight() * 2
        return widths + heights

    def getH(self):
        a = self.getWidth()
        b = self.getHeight()
        c = math.sqrt(a**2 + b**2)
        return c

if __name__ == '__main__':
    r = Rectangle(10, 5)

    print(r.getArea()) #50

    print(r.getPerimeter()) #30

    print(r.getH()) #11.18 (rounded)