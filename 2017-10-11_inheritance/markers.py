class ExpoMarker:
    def __init__(self, color):
        self.capacity = 100
        self.color = color
        self.tipsize = 3

    def write(self):
        if self.capacity == 0:
            return 0

        temp = self.capacity
        self.capacity -= (self.tipsize+1)

        if self.capacity < 0:
            self.capacity = 0
            return temp

        return self.tipsize+1


class BlueExpoMarker(ExpoMarker):
    def __init__(self):
        color = 'blue'
        ExpoMarker.__init__(self, color)


class RedExpoMarker(ExpoMarker):
    def __init__(self):
        color = 'red'
        ExpoMarker.__init__(self, color)



m1 = BlueExpoMarker()
r1 = RedExpoMarker()

print(m1.write())

