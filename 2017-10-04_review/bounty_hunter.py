class BountyHunter:
    def __init__(self):
        self.cash = 0

    def collectBounty(self, bounty):
        self.cash += bounty

    def payExpense(self, expense):
        self.cash -= expense

    def getCash(self):
        return self.cash