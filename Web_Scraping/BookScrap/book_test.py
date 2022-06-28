import unittest
from books import BookToScrap

class MyBookTest(unittest.TestCase):
    def test_book_init(self):
        book = BookToScrap(title="Harry Potter and The Prisoner of Azkaban",
                           image="https://upload.wikimedia.org/wikipedia/en/a/a0"
                                 "/Harry_Potter_and_the_Prisoner_of_Azkaban.jpg 1.5x",
                           rank=5, price=49.99, available=True)

        self.assertEqual(book.rank, 5)  # add assertion here


if __name__ == '__main__':
    unittest.main()
