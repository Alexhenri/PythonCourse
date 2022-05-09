'''
This is the Player Class
Every player has a Deck and a Name
'''

# Importing Deck Class
from deck import Deck

class Player():

    def __init__(self, name, d):
        self.name = name
        self.deck = d
        self.count = len(d.cards)


    def __str__(self):
        return (f'{self.name} - Deck with {self.count} cards')



def get_player_names():
        n1 = input(f'Please enter the Player One name: ')
        if n1 == '':
            n1 = 'Player One'
            print('Empty? So i will call you Player One')

        n2 = input(f'Please enter the Player Two name: ')
        if n2 == '':
            n2 = 'Player One'
            print('Empty? So i will call you Player Two')
        elif n1 == n2:
            print("Same name? So i will call you both as 'P1 {}' and 'P2 {}'".format(n1,n1))
            n1 = 'P1 '+ n1
            n2 = 'P2 '+ n2

        return (n1,n2)
