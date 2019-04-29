import containers, io, mock, string, unittest, sys
from contextlib import redirect_stdout
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
        hangman.guessed_character = 'aa'
        self.assertFalse(hangman.validUserInput())
        
    def test_letter_correct(self):
        hangman = Hangman()
        for character in string.printable:
            hangman.guessed_character = character
            valid = hangman.validUserInput()
            self.assertEqual(valid, character in string.ascii_uppercase)
        
    def test_incorrect_letter_changes_hangman(self):
        hangman = Hangman(False, 9, 'hangman')
        hangman_figures = []
        for character in 'bcdefijkl':
            hangman_figures.append(hangman.getHangman())
            hangman.guessed_character = character
            hangman.processInput()

        for figure_1, figure_2 in zip(hangman_figures[:-1], hangman_figures[1:]):
            self.assertNotEqual(figure_1, figure_2)
        
    def test_incorrect_letter_reduces_lives(self):
        hangman = Hangman(False, 9, 'hangman')
        hangman_figures = []
        lives = hangman.lives
        for character in 'bcdefijkl':
            hangman_figures.append(hangman.getHangman())
            hangman.guessed_character = character
            hangman.processInput()
            self.assertTrue(hangman.lives < lives)
            lives = hangman.lives
        
    def test_number_of_tries_limited(self):
        pass
        
    def test_user_completes_word_implies_win(self):
        hangman = Hangman(False, 9, 'hangman')
        for character in 'hangm':
            hangman.guessed_character = character
            hangman.processInput()
        self.assertTrue(hangman.finished)
        self.assertTrue(hangman.won)
        
    def test_user_without_lives_implies_loss(self):
        hangman = Hangman(False, 9, 'hangman')
        for character in 'bcdefijkl':
            hangman.guessed_character = character
            hangman.processInput()
        self.assertTrue(hangman.finished)
        self.assertFalse(hangman.won)
        
    def test_supply_feedback(self):
        for character in string.ascii_letters:
            with mock.patch('builtins.input', return_value=character):
                hangman = Hangman(True, 9, 'hangman')
                f = io.StringIO()
                with redirect_stdout(f):
                    hangman.turn()
                out = f.getvalue()
                print(character, out)
                if character.lower() in 'hangman':
                    assert 'Good guess!' in out
                else:
                    assert 'too bad' in out
        
    def test_user_guesses_last_character(self):
        pass
        
    def test_user_enters_invalid_character(self):
        pass

    def test_user_enters_multiple_characters(self):
        hangman = Hangman()
        hangman.guessed_character = 'aa'
        self.assertFalse(hangman.validUserInput())
        
    def test_user_enters_no_character(self):
        hangman = Hangman()
        hangman.guessed_character = ''
        self.assertFalse(hangman.validUserInput())
        
    def test_user_enters_same_character_multiple_times(self):
        hangman = Hangman()
        hangman.guessed_character = 'a'
        hangman.processInput()
        hangman.guessed_character = 'a'
        self.assertTrue(hangman.characterAlreadyGuessed())
        
if __name__ == '__main__':
    unittest.main()