import containers, io, string, unittest, unittest.mock
from hangman_beta import Hangman

class TestHangman(unittest.TestCase):
    def test_boot(self):
        hangman = Hangman()
        self.assertIsInstance(hangman, Hangman)

    def test_generated_word_is_string(self):
        hangman = Hangman()
        hangman.getWord()
        self.assertIsInstance(hangman.word, str)

    def test_generated_word_is_nonempty(self):
        hangman = Hangman()
        hangman.getWord()
        self.assertTrue(len(hangman.word) > 0)

    def test_enter_one_letter(self):
        hangman = Hangman()
        self.assertFalse(hangman.validUserInput('aa'))
        
    def test_letter_correct(self):
        hangman = Hangman()
        for s in string.printable:
            valid = hangman.validUserInput(s)
            self.assertEqual(valid, s in string.ascii_lowercase)
        
    def test_incorrect_letter_changes_hangman(self):
        hangman = Hangman(False, 9, 'hangman')
        hangman_figures = []
        for character in 'bcdefijkl':
            hangman_figures.append(hangman.getHangman())
            hangman.processInput(character)

        for figure_1, figure_2 in zip(hangman_figures[:-1], hangman_figures[1:]):
            self.assertNotEqual(figure_1, figure_2)
        
    def test_incorrect_letter_reduces_lives(self):
        hangman = Hangman(False, 9, 'hangman')
        hangman_figures = []
        lives = hangman.lives
        for character in 'bcdefijkl':
            hangman_figures.append(hangman.getHangman())
            hangman.processInput(character)
            self.assertTrue(hangman.lives < lives)
            lives = hangman.lives
        
    def test_number_of_tries_limited(self):
        pass
        
    def test_user_completes_word_implies_win(self):
        hangman = Hangman(False, 9, 'hangman')
        for character in 'hangm':
            hangman.processInput(character)
        self.assertTrue(hangman.finished)
        self.assertTrue(hangman.won)
        
    def test_user_without_lives_implies_loss(self):
        hangman = Hangman(False, 9, 'hangman')
        for character in 'bcdefijkl':
            hangman.processInput(character)
        self.assertTrue(hangman.finished)
        self.assertFalse(hangman.won)
        
    def test_supply_feedback(self):
        pass
        
    def test_user_guesses_last_character(self):
        pass
        
    def test_user_enters_invalid_character(self):
        pass
        
    def test_user_enters_punctuation(self):
        # see test_letter_correct
        pass

    def test_user_enters_number(self):
        # see test_letter_correct
        pass

    def test_user_enters_multiple_characters(self):
        hangman = Hangman()
        self.assertFalse(hangman.validUserInput('aa'))
        
    def test_user_enters_no_character(self):
        hangman = Hangman()
        self.assertFalse(hangman.validUserInput(''))
        
    def test_user_enters_same_character_multiple_times(self):
        hangman = Hangman()
        hangman.processInput('a')
        self.assertTrue(hangman.characterAlreadyGuessed('a'))
        
if __name__ == '__main__':
    unittest.main()