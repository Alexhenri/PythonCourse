'''
This is the Player Class
Every player has a Name, Deck, Sum of Cards and amount of money
'''

# Importing Deck Class
import deck
import card


class Player():

    def __init__(self, name, money):

        self.name = name
        self.money = money
        self.list_of_cards = []

    def __str__(self):
        return ('{} - Amount of money:  $ {:.2f}'.format(self.name, self.money))

    def show_player_cards(self):
        print("{} Cards:".format(self.name))
        print('', *self.list_of_cards, sep='\n')
        #for card in self.list_of_cards:
        #    card.show_card()

    def add_card_player(self, c):
        self.list_of_cards.append(c)



def get_player_infos():
    name = input(f'Please enter the Player name: ')
    if name == '':
        name = 'Player One'
        print('Empty? So i will call you Player One')

    while True:
        try:
            money = float(input(f'Hello {name}!! With how much of money do you want to start the game? '))
            break
        except:
            print("Sorry, but we can't understand. Please enter with an amount of money.")

    return (name, money)
