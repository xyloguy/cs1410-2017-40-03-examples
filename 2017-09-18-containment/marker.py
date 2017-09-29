MAX_CAPACITY = 50

class Marker:
    def __init__(self):
        self.ink = 0
        self.addInk(MAX_CAPACITY)


    def write(self):
        if not self.isEmpty():
            self.ink -= 1
            return True
        else:
            return False


    def addInk(self, amount):
        try:
            amount = float(amount)
            amount = int(amount)
        except:
            amount = 0


        if amount <= 0:
            return 0

        diff = MAX_CAPACITY - self.ink

        if amount > diff:
            self.ink += diff
            return diff

        else:
            self.ink += amount
            return amount



    def isEmpty(self):
        if self.ink <= 0:
            self.ink = 0
            return True
        else:
            return False

def test():
    m = Marker()
    print(m.ink)

if __name__ == '__main__':
    test()