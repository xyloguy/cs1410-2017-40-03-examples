from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.color = 'red'

    def get_radius(self):
        return self.radius

    def get_area(self):
        return pi * self.get_radius() ** 2

    def get_circumference(self):
        return 2 * pi * self.get_radius()

    def greater_than(self, other):
        return self.get_radius() > other.get_radius()

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

    def __add__(self, other):
        r1 = self.get_radius()
        r2 = other.get_radius()
        r3 = r1 + r2
        return Circle(r3)

    def __sub__(self, other):
        r1 = self.get_radius()
        r2 = other.get_radius()
        newr = abs(r1 - r2)
        return Circle(newr)

    def __mul__(self, other):
        r1 = self.get_radius()
        r2 = other.get_radius()
        newr = r1 * r2
        return Circle(newr)

    def __iadd__(self, other):
        r1 = self.get_radius()
        r2 = other.get_radius()
        r3 = r1 + r2
        self.radius = r3
        return self


c1 = Circle(9)
c1.color = 'blue'
c2 = Circle(10)
print(c1.color)

c3 = c1 + c2
c4 = c2 - c1
c5 = c1 * c2

c1 += c2
print(c1.color)

print(c3.get_radius())
print(c4.get_radius())
print(c5.get_radius())
print(c1.get_radius())