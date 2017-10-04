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