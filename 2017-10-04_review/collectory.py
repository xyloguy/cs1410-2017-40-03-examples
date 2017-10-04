MAX_STONE = 3
class Collector:
    def __init__(self):
        self.stones = []

    def collectStone(self, stone):
        self.stones.append(stone)
        if len(self.stones) > MAX_STONE:
            self.discardStone()

    def discardStone(self):
        stone = self.stones[0]
        self.stones = self.stones[1:]
        return stone

    def getAllStones(self):
        return self.stones
