class Marker:
    def __init__(self, color):
        self.color = color
        self.capacity = 100

    def write(self):
        if self.capacity != 0:
            self.capacity -= 1

    def isEmpty(self):
        if self.capacity == 0:
            return True
        return False


blackmarker = Marker('black')
print(blackmarker.color)
print(blackmarker.capacity)
blackmarker.capacity = 80
print(blackmarker.capacity)

for i in range(90):
    print(blackmarker.isEmpty())
    blackmarker.write()
print(blackmarker.capacity)
