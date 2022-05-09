'''

This is the main.py of the War Game Project

    The War Game is a card game that take the Standard 52-Card Deck and divide then for two players,
    so each player receives a deck with 26 cards.

    Each player get the first card of his deck and the player with the higher card takes both cards to the bottom of his deck.

    If the cards are with the same rank, each player get two cards of his deck, one face down and the other face up,
    and do the same check up to the face up card. The player with the higher rank get the 6 cards (the first card, the
    face down card, and the face up card). If the cards are again with the same rank repeat this process until one player win
    or one deck became empty.

    Rank
    2 < 3 < 4 ... < 10 < Jack < Queen < King < Ace

'''
import deck
import player

'''
Imported Modules:
    
'''

def rank_war_game():
    print('Rank\n2 < 3 < 4 ... < 10 < Jack < Queen < King < Ace')

def rules_war_game():
    print("The War Game is a card game that take the Standard 52-Card Deck and divide then for two players, so each player receives a deck with 26 cards.")
    print('\n')
    print("Each player get the first card of his deck and the player with the higher card takes both cards to the bottom of his deck.")
    print('\n')
    print("If the cards are with the same rank, each player get two cards of his deck, one face down and the other face up,and do the same check up to the face up card.")
    print("The player with the higher rank get the 6 cards (the first card, the face down card, and the face up card).")
    print("If the cards are again with the same rank repeat this process until one player win or one deck became empty.")

def welcome_war_game():
    print('Hello!\nWelcome to the war game!!')
    rules_war_game()
    print('\n')
    rank_war_game()
    print('\n')
    print('\n')

def check_finish_game(p1, p2):
    if p1 == 0 or p2 == 0:
        return True

    return False


if __name__ == '__main__':
    '''
    War game main function 
    '''
    welcome_war_game()

    # Create the Deck
    all_cards_deck = deck.Deck()
    all_cards_deck.create_Deck()

    while True:

        # Randomize Deck and divide evenly - Deck 1 and Deck 2 - Both with 26 Cards
        all_cards_deck.rand_deck()
        # Test to win - 7 win in 395 rounds (Won last round)  - 8 to win in 51 rounds (Won with Draw)
        #all_cards_deck.sort_deck_to_win(8)
        deck1 = deck.Deck(all_cards_deck.cards[0:26])
        deck2 = deck.Deck(all_cards_deck.cards[26::])

        # Ask players info and give then their decks
        names = player.get_player_names()
        p1 = player.Player(name = names[0], d = deck1)
        p2 = player.Player(name = names[1], d = deck2)

        print(p1)
        print(p2)

        count = 0
        pile_count = 0
        pile_of_cards = []

        while True:

            # Game loop - true until one player win or one deck became empty

            #input('Tap enter to get one card from your deck.')
            c1 = p1.deck.grab_one_card()
            c2 = p2.deck.grab_one_card()

            pile_of_cards.extend([c1, c2])

            print('{}: {}'.format(p1.name, c1))
            print('{}: {}'.format(p2.name, c2))

            if c1.rank == c2.rank:
                print('War!! This cards and one more of each player are added to the pile of cards')
                if not check_finish_game(p1.count, p2.count):
                    c1 = p1.deck.grab_one_card()
                    c2 = p2.deck.grab_one_card()

                    pile_of_cards.extend([c1,c2])
                    pile_count += 4
            elif c1.rank > c2.rank:
                print('{} won this round!! This cards and the pile of cards with {} are added to you deck'.format(p1.name, pile_count))
                p1.deck.cards = pile_of_cards + p1.deck.cards
                pile_count = 0
                pile_of_cards = []
            else:
                print('{} won this round!! This cards and the pile of cards with {} are added to you deck'.format(p2.name, pile_count))
                p2.deck.cards = pile_of_cards + p2.deck.cards
                pile_count = 0
                pile_of_cards = []

            count += 1
            p1.count = len(p1.deck.cards)
            p2.count = len(p2.deck.cards)

            print(str(p1)+'\n'+str(p2))
            if check_finish_game(p1.count,p2.count):
               break

        if (p2.count == 0):
            print('{} won!! You took {} rounds!'.format(p1.name, count))
        elif (p1.count == 0):
            print('{} won!! You took {} rounds!'.format(p2.name, count))
        else:
            print('Both players deck are empty!')

        break