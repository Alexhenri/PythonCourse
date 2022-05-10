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

    def __init__(self):
        self.cards = []

    def create_Deck(self):

        cards = []
        for cs in card.card_suits:
            for cv in card.card_values:
                c = card.Card(cv, cs)
                cards.append(c)

        self.cards = cards


    def print_all_deck(self):
        for item in self.cards:
                item.show_card()

    def rand_deck(self):
        random.shuffle(self.cards)

    def remove_one_card(self):
        return self.cards.pop()
