import unittest
import hangman_beta

class TestHangman(unittest.TestCase):
    def test_boot(self):
        self.assertEqual('FO', 'FOO')

if __name__ == '__main__':
    unittest.main()