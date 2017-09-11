import random

class Card:
    def __init__(self, display, suit):
        self.suit = suit
        self.display = display

    def print(self):
        return self.display + self.suit

    def value(self):
        lookup = {
            'A': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 11,
            'Q': 12,
            'K': 13
        }
        return lookup[self.display]

    def blackJackValue(self):
        lookup = {
            'A': 11,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10
        }
        return lookup[self.display]



#kingspades = Card('K', 'spades')

suits = ['S', 'H', 'D', 'C']
displays = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = []

for suit in suits:
    for display in displays:
        card = Card(display, suit)
        deck.append(card)

#index = random.randint(0, len(deck)-1)
#index = random.randrange(len(deck))
#card = deck[index]
card = random.choice(deck)
print( card.print() )
print(len(deck))

# shuffle the deck
random.shuffle(deck)
for i in range(len(deck)):
    # take the top card off the deck
    card = deck.pop(0)

    # print card, value, bjvalue, cards_left_in_deck
    print( card.print(), card.value(), card.blackJackValue(), len(deck) )
