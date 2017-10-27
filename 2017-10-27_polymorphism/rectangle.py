class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_size(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError('width and height must be greater than 0')

        self.width = width
        self.height = height

    def get_area(self):
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        return self.get_width() * 2 + self.get_height() * 2
