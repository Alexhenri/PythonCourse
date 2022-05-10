import unittest
import card
import deck
import player
import main


class MyCardTest(unittest.TestCase):
    def test_card_init(self):
        c = card.Card('Ace', 'Spade')
        value = c.value
        color = c.color
        suit  = c.suit

        self.assertEqual(color, 'black')
        self.assertEqual(suit, 'Spade')
        self.assertEqual(value, 'Ace')

    def test_print_card(self):
        c = card.Card('Ace', 'Spade')
        result = str(c)
        self.assertEqual(result, 'Ace of Spade')

class MyDeckTest(unittest.TestCase):
    def test_deck_init(self):
        c = card.Card('Ace', 'Spade')
        c1 = card.Card('Ace', 'Heart')

        d = deck.Deck()
        result = d.cards[1].suit
        self.assertEqual(result, "Heart")


    def test_deck_creation(self):
        d = deck.Deck()
        d.create_Deck()
        result = d.cards[0].value
        result2 = len(d.cards)
        self.assertEqual(result, '2')  # add assertion here
        self.assertEqual(result2, 52 )  # add assertion here

class MyPlayerTest(unittest.TestCase):

    def test_player_get_infos(self):
        result = player.get_player_infos()
        self.assertEqual(result[0], 'Alex')

class MySumTest(unittest.TestCase):

    def test_get_best_sum(self):
        c1 = card.Card('5', 'Hearts')
        c2 = card.Card('6', 'Spades')
        c3 = card.Card('Queen', 'Hearts')
        #c4 = card.Card('Jack', 'Diamonds')
        cards = [c1,c2,c3]
        result = main.get_best_sum(cards)

        self.assertEqual(result, 21)




if __name__ == '__main__':
    unittest.main()
