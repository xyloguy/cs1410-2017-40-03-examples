import rectangle

class Square(rectangle.Rectangle):
    def __init__(self, size):
        rectangle.Rectangle.__init__(self, size, size)

    def set_size(self, size):
        rectangle.Rectangle.set_size(self, size, size)


rect = rectangle.Rectangle(10, 20)
rect.set_size(1, 10)
print(rect.get_area())

square = Square(10)
square.set_size(1)
print(square.get_area())