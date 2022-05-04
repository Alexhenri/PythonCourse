import unittest
import cap




class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')  # add assertion here

    def test_multiple_words(self):
        text = 'too many words'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Too Many Words')


if __name__ == '__main__':
    unittest.main()
