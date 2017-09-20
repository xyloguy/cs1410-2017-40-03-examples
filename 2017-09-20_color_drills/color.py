class Color:
    def __init__(self, red, green, blue):
        self.__r = red
        self.__g = green
        self.__b = blue

    def getRed(self):
        return self.__r

    def getGreen(self):
        return self.__g

    def getBlue(self):
        return self.__b

    def setRed(self, newcolor):
        currentcolor = self.getRed()
        if newcolor != currentcolor and newcolor >= 0 and newcolor <= 255:
            self.__r = newcolor
            return True
        else:
            return False

    def setGreen(self, newcolor):
        currentcolor = self.getGreen()
        if newcolor != currentcolor and newcolor >= 0 and newcolor <= 255:
            self.__g = newcolor
            return True
        else:
            return False

    def setBlue(self, newcolor):
        currentcolor = self.getBlue()
        if newcolor != currentcolor and newcolor >= 0 and newcolor <= 255:
            self.__b = newcolor
            return True
        else:
            return False

    def triad(self):
        red = self.getRed()
        green = self.getGreen()
        blue = self.getBlue()

        self.setRed(green)
        self.setGreen(blue)
        self.setBlue(red)

r = 186
g = 28
b = 33
ba1c21 = Color(r, g, b)
print(ba1c21.getRed())
print(ba1c21.getGreen())
print(ba1c21.getBlue())
print()
ba1c21.triad()

print(ba1c21.getRed())
print(ba1c21.getGreen())
print(ba1c21.getBlue())
print()

ba1c21.triad()

print(ba1c21.getRed())
print(ba1c21.getGreen())
print(ba1c21.getBlue())
print()

