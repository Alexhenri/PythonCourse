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

# Importing classes

import deck
import player

winner = {'Continue': 0, 'Win': 1, "Loose": 2}


def get_bet(player):
    while True:
        try:
            bet = float(input("Please enter your bet for this round: $"))
            if bet > player.money:
                print("Sorry, you don't have this amount of money available. Your funds are: ${:.2f}".format(player.money))
            else:
                break
        except:
            print('Sorry, i do not understand.')
    player.money -= bet
    return bet


def get_best_sum(list_of_cards):
    sum = 0
    ace_cards = []

    for card in list_of_cards:
        if (card.rank == 'Ace'):
            ace_cards.append(card)
        else:
            sum += card.value

    if len(ace_cards) == 1:
        if (sum + 11) > 21:
            sum += 1
        else:
            sum += 11
    elif len(ace_cards) == 2:
        if (sum + 12) > 21:
            sum += 2
        else:
            sum += 12
    elif len(ace_cards) == 3:
        if (sum + 13) > 21:
            sum += 3
        else:
            sum += 13
    elif len(ace_cards) == 4:
        if (sum + 14) > 21:
            sum += 4
        else:
            sum += 14

    return sum


def check_end_game(list_of_cards):
    sum = 0

    sum = get_best_sum(list_of_cards)

    if sum == 21:
        return winner['Win']

    if sum > 21:
        return winner['Loose']

    return 0


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


def hit(all_d, list_of_cards):
    card = all_d.remove_one_card()
    list_of_cards.append(card)
    card.show_card()


def get_first_two_card(all_d, p, cp_c):
    for n in range(0, 2):
        p.add_card_player(all_d.remove_one_card())
        cp_c.append(all_d.remove_one_card())


def print_round_info(player, bet, cp_c, round, hide):
    print(player)
    print("Round {} - Bet: ${:.2f}".format(round, bet))
    if hide:
        print("Computer Cards: ")
        print("***************")
        print(cp_c[1])
        player.show_player_cards()
    else:
        player.show_player_cards()
        print("Computer Cards: ")
        for card in cp_c:
            card.show_card()


def get_action():
    while True:
        action = input("Hit or Stay? Hit/Stay or H/S\n")
        if action == "Hit" or action == "H":
            return "HIT"
        elif action == "Stay" or action == "S":
            return "STAY"
        else:
            print("Please type choose your action.")


def play_again():
    while True:
        answer = input('Do you like to play another round? Yes/No Y/N')
        if(answer == 'Y' or answer == 'Yes'):
            return True
        elif(answer == 'N' or answer == 'No'):
            return False
        else:
            print("Sorry, i don't understand.")


# Main Function
if __name__ == '__main__':

    # Game Setup
    all_deck = deck.Deck()
    round = 0

    # Player Setup
    name, money = player.get_player_infos()
    player = player.Player(name, money)

    # Round Loop
    while True:
        # Round Setup
        round += 1

        # Setting hit player and hit cpu = 0 (That defines who win)
        hit_player = 0
        hit_cpu = 0

        # Computer List
        computer_cards = []

        # Resetting player list
        player.list_of_cards = []

        # Creating new Deck and shuffle it
        all_deck.create_Deck()
        all_deck.rand_deck()

        # Getting players new bet
        bet = get_bet(player)

        # Deal two cards for the player, and the computer
        get_first_two_card(all_deck, player, computer_cards)
        print_round_info(player, bet, computer_cards, round, True)

        # Player Hit loop
        while hit_player == 0:
            action = get_action()
            if action == "HIT":
                hit(all_deck, player.list_of_cards)
                hit_player = check_end_game(player.list_of_cards)
            else:
                break

        print_round_info(player, bet, computer_cards, round, False)

        # Checking if cpu already win with the 2 first cards
        hit_cpu = check_end_game(computer_cards)

        # Computer Deal Hit loop
        while hit_player == 0 and hit_cpu == 0:
            hit(all_deck, computer_cards)
            hit_cpu = check_end_game(computer_cards)
            if hit_cpu == 0 and (get_best_sum(computer_cards) > get_best_sum(player.list_of_cards)):
                hit_cpu = winner['Win']

        if hit_player == winner['Loose'] or hit_cpu == winner['Win']:
            print("You loose. You lost yor bet")
        else:
            print("You win. You doubled your bet. ")
            player.money += (2 * bet)

        print(player)
        if player.money == 0:
            print('You are out of money. Bye bye')
            break

        if play_again() == False:
            print("Got it! Bye bye")
            break
        # End Loop
    # End Game
