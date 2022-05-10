'''
This is the Card Class

Every card has a Value and Suit
The value is
    2 .. 10, Jack, Queen, King, Ace
The suit is
    Spade, Club, Diamond, Heart
The color is
    black   for Spade and Club
    red     for Diamond and Heart
'''

card_values = {'2': 2 , '3': 3, '4': 4, '5': 5,
               '6': 6 , '7': 7 , '8': 8, '9': 9 ,
               '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}
card_suits   = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

class Card():

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = card_values[rank]

        if(suit == 'Hearts' or suit == 'Diamonds'):
            self.color = 'red'
        else:
            self.color = 'black'

    def __str__(self):
        return (f'{self.rank} of {self.suit}')

    def show_card(self):
        print(f'{self.rank} of {self.suit}')
