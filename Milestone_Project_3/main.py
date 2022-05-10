'''
This is the main file of Milestone project 3

BlackJack - Simple Version

In the BlackJack Simple Version the player starts making a bet between 0 and his amount of money
The round begins and the player get 2 cards as same the Computer Deal, but the last, gets one face down and one face up.
Then, the player can call:

        Hit : Grab another card from the deck
        Stay : Stop and give the chance for the Computer Deal to act

The Player wins if the sum of his cards are exactly 21 or the Computer Deal get bust,
    that means that he pass the sum of 21 while trying to get closer to 21 than the player.

The Player loses if, while trying to get 21, he gets bust or if the Computer Deal sum is higher than the player sum,
    and so, closer to 21.

    Cards values:
        2... 10 - Theirs perspective number
        Jack, Queen, King - 10
        Ace - Can be 1 or 10.
'''

#Importing classes

import deck
import player

def get_bet(player):
    while True:
        try:
            bet = float(input("Please enter your bet for this round: $"))
            if bet > player.money:
                print("Sorry, you don't have this amount of money avaiable. Your funds are: ${:.2f}".format(money))
            else:
                break
        except:
            print('Sorry, i do not understand.')
    player.money -= bet
    return bet

def check_bust(d):
    if d.sum_of_cards > 21:
        return True
    else:
        return False

def check_win(d):
    if d.sum_of_cards == 21:
        return True
    else:
        return False

def hit(all_d, d):
    card = all_d.remove_one_card()
    d.add_one_card(card)

def get_first_two_card_player(all_d, d):
    card = all_d.remove_one_card()
    d.add_one_card(card)

    card = all_d.remove_one_card()
    d.add_one_card(card)

def get_first_two_card_computer(all_d, d):
    card = all_d.remove_one_card()
    d.add_one_card(card)

    card = all_d.remove_one_card()
    d.add_one_card(card)

def print_round_info(player, bet, cp_d, round, hide):
    print(player)
    print("Round {} - Bet: ${:.2f}".format(round, bet))
    print("Computer Cards: ")
    if hide:
        print("***************")
        print(cp_d.cards[1])
    else:
        cp_d.print_all_deck()
    player.show_player_cards()

def get_action():
    while True:
        action = input("Hit or Stay? Hit/Stay or H/S\n")
        if action == "Hit" or action == "H":
            print('Hitando')
            return "HIT"
        elif action == "Stay" or action == "S":
            print('Stayando')
            return "STAY"
        else:
            print("Please type choose your action.")


# Main Function
if __name__ == '__main__':

    # Game Setup
    all_deck = deck.Deck()
    bet = 0
    round = 0

    # Player Setup
    name, money = player.get_player_infos()
    p_deck = deck.Deck()
    player = player.Player(name,money, p_deck)

    # Computer Setup
    computer_deck = deck.Deck()

    # Round Loop
    while True:

        # Round Setup
        all_deck.create_Deck()
        all_deck.rand_deck()
        player_looses = False
        cp_looses = False
        round += 1

        bet = get_bet(player)

        get_first_two_card_player(all_deck, player.deck)
        get_first_two_card_computer(all_deck, computer_deck)

        print_round_info(player, bet, computer_deck, round, True)
        # Player Hit loop
        while True:
            pass
            action = get_action()
            if action == "HIT":
                hit(all_deck, player.deck)
                #print(player)
                #player.deck.print_all_deck()
                print_round_info(player, bet, computer_deck, round, True)
                if check_bust(player.deck):
                    player_looses = True
                    break
                if check_win(player.deck):
                    cp_looses = True
                    break
            else:
                break

        # Computer Deal Hit loop
        while player_looses == False and cp_looses == False:
            hit(all_deck, computer_deck)
            print("Computer Deal - Sum: {}".format(computer_deck.sum_of_cards))
            print_round_info(player, bet, computer_deck, round, False)
            if computer_deck.sum_of_cards > player.deck.sum_of_cards and computer_deck.sum_of_cards < 21:
                player_looses = True
                break
            if check_bust(computer_deck):
                cp_looses = True
                break

        if(player_looses):
            print("You loose. You lost yor bet")
        else:
            print("You win. You doubled your bet.")
            player.money += (2 * bet)
        # End Loop
    # End Game



