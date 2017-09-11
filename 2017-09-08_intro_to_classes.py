class Marker:
    def __init__(self, color):
        self.color = color
        self.capacity = 100

    def write(self):
        if self.capacity != 0:
            self.capacity -= 1

    def isEmpty(self):
        return self.capacity == 0


def createBlackMarker():
    c = 'black'
    bm = Marker(c)
    return bm

def createRedMarker():
    return Marker('red')

def drawLine(marker, length):
    for i in range(1, length + 1):
        if marker.isEmpty():
            print('Your marker is empty')
            break
        marker.write()
    print('Your line is: ' + i + ' in length')



marker = createBlackMarker()
drawLine(marker, 110)