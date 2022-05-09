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
               '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
card_suits   = ['Spade', 'Club', 'Heart', 'Diamond']

class Card():

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.rank = card_values[value]

        if(suit == 'Heart' or suit == 'Diamond'):
            self.color = 'red'
        else:
            self.color = 'black'

    def __str__(self):
        return (f'{self.value} of {self.suit}')

    def show_card(self):
        print(f'{self.value} of {self.suit}')
