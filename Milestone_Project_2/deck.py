'''
This deck.py is responsable to created the Deck Class
The Deck Class is a list of cards - Class Card
'''

# Importing Card Class and card_values and card_suits
import card
import random


class Deck():
    '''
    The deck class is a list of cards
    self.cards -> type Class Card
    '''

    def __init__(self, cards=[]):
        self.cards = cards

    def create_Deck(self):
        """
        :type self: Deck
        """
        cards = []
        for cs in card.card_suits:
            for cv in card.card_values:
                c = card.Card(cv, cs)
                cards.append(c)

        self.cards = cards

    def print_suit(self, suit):
        for item in self.cards:
            if item.suit == suit:
                item.show_card()

    def print_all_deck(self):
        for item in self.cards:
                item.show_card()

    def rand_deck(self):
        random.shuffle(self.cards)

    def sort_deck_to_win(self, n):
        c_up = []
        c = []
        for item in self.cards:
            if(item.rank > n):
                c_up.append(item)
            else:
                c.append(item)

        self.cards = c_up + c

