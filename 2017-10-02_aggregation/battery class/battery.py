class Battery:
    def __init__(self, capacity):
        self.charge = capacity
        self.capacity = capacity

    def getCapacity(self):
        return self.capacity

    def getCharge(self):
        return self.charge

    def drain(self, milliamps):

        if milliamps <= 0:
            return False

        if self.getCharge() == 0:
            return False

        self.charge -= milliamps
        if self.getCharge() < 0:
            self.charge = 0.

        return True
    