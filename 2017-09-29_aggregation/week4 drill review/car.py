MAX_SPEED = 80.

class Car:
    def __init__(self):
        self.speed = 0.0

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        if speed == self.getSpeed():
            return False

        if 0. <= speed <= MAX_SPEED:
            self.speed = speed
            return True

        return False

    def accelerate(self, delta_speed):

        if delta_speed <= 0:
            return False

        if self.getSpeed() == MAX_SPEED:
            return False

        self.speed += delta_speed
        if self.getSpeed() > MAX_SPEED:
            self.speed = MAX_SPEED

        return True




