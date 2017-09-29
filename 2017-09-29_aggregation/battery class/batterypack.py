import random
from battery import Battery

class BatteryPack:
    def __init__(self, maxbatteries):
        self.capacity = maxbatteries
        self.pack = []

    def addBattery(self, battery):

        if len(self.getPack()) >= self.capacity:
            return False

        self.pack.append(battery)
        return True

    def getPack(self):
        return self.pack

    def getBatteries(self):
        return self.getPack()

    def getCharge(self):
        total = 0
        for battery in self.getBatteries():
            total += battery.getCharge()
        return total

if __name__ == "__main__":
    batteryBank = BatteryPack(4)
    print(batteryBank.addBattery(Battery(2500)))
    print(batteryBank.addBattery(Battery(2500)))
    print(batteryBank.addBattery(Battery(2500)))
    print(batteryBank.addBattery(Battery(2500)))
    print(batteryBank.getCharge())

    totaldrain = 0
    for battery in batteryBank.getBatteries():
        num = random.randint(0,2501)
        totaldrain += num
        battery.drain(num)
    print(totaldrain)
    print(batteryBank.getCharge())
