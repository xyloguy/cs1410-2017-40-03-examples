import card
import random

class Deck:
    def __init__(self):
        self.deck = []

        # possible suits
        suits = ['S', 'H', 'D', 'C']

        # possible cards
        displays = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in suits:
            for display in displays:
                c = card.Card(display, suit)
                self.deck.append(c)

    def shuffle(self):
        random.shuffle(self.deck)

    def cut(self, n=None):
        if n is None:
            n = random.randrange(0, len(self.deck))

        top = self.deck[:n]
        bottom = self.deck[n:]

        self.deck = bottom + top

    #deal the top card off the deck

