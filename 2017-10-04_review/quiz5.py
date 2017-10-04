import collectory

tivan = collectory.Collector()
tivan.collectStone('Mind Gem')
tivan.collectStone('Soul Gem')
tivan.collectStone('Space Gem')
tivan.collectStone('Power Gem')

gem = tivan.discardStone()
print(gem, 'discarded.') # Soul Gem discarded.

tivan.collectStone('Time Gem')
tivan.collectStone('Reality Gem')

for gem in tivan.getAllStones():
    print(gem) #Power Gem, Time Gem, Reality Gem








import bounty_hunter
boba = bounty_hunter.BountyHunter()
boba.collectBounty(1500)
boba.collectBounty(750)
boba.payExpense(2500)
print(boba.getCash()) # -250
