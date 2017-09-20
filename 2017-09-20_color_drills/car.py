MAX_SPEED = 80

class Car:
    def __init__(self):
        self.speed = 0.0

    def getSpeed(self):
        return self.speed

    def setSpeed(self, newspeed):
        c = self.getSpeed()
        if newspeed == c:
            return False

        if newspeed in range(0, MAX_SPEED+1):
            self.speed = newspeed
            return True

        return False


c = Car()
print(c.setSpeed(1))
print(c.getSpeed())
