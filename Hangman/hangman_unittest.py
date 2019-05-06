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
            hangman.guessed_character = character.upper()
            valid = hangman.validUserInput()
            self.assertEqual(valid, character.upper() in string.ascii_uppercase)
        
    def test_incorrect_letter_changes_hangman(self):
        hangman = Hangman(False, 9, 'hangman')
        hangman_figures = []
        for character in 'bcdefijkl':
            hangman_figures.append(hangman.getHangman())
            hangman.guessed_character = character.upper()
            hangman.processInput()

        for figure_1, figure_2 in zip(hangman_figures[:-1], hangman_figures[1:]):
            self.assertNotEqual(figure_1, figure_2)
        
    def test_incorrect_letter_reduces_lives(self):
        hangman = Hangman(False, 9, 'hangman')
        hangman_figures = []
        lives = hangman.lives
        for character in 'bcdefijkl':
            hangman_figures.append(hangman.getHangman())
            hangman.guessed_character = character.upper()
            hangman.processInput()
            self.assertTrue(hangman.lives < lives)
            lives = hangman.lives
        
    def test_number_of_tries_limited(self):
        pass
        
    def test_user_completes_word_implies_win(self):
        hangman = Hangman(False, 9, 'hangman')
        for character in 'hangm':
            hangman.guessed_character = character.upper()
            hangman.processInput()
        self.assertTrue(hangman.finished)
        self.assertTrue(hangman.won)
        
    def test_user_without_lives_implies_loss(self):
        hangman = Hangman(False, 9, 'hangman')
        for character in 'bcdefijkl':
            hangman.guessed_character = character.upper()
            hangman.processInput()
        self.assertTrue(hangman.finished)
        self.assertFalse(hangman.won)
        
    def test_feedback_on_user_input(self):
        for character in string.ascii_letters:
            with mock.patch('builtins.input', return_value=character):
                hangman = Hangman(True, 9, 'hangman')
                f = io.StringIO()
                with redirect_stdout(f):
                    hangman.turn()
                out = f.getvalue()
                if character.lower() in 'hangman':
                    self.assertTrue('Good guess!' in out)
                else:
                    self.assertTrue('too bad' in out)

    def test_feedback_win(self):
        hangman = Hangman(True, 9, 'hangman')
        f = io.StringIO()
        with redirect_stdout(f):
            for character in 'hangm':
                with mock.patch('builtins.input', return_value=character):
                    hangman.turn()

            # Simulate play again
            with mock.patch('builtins.input', return_value='n'):
                hangman.turn()
        out = f.getvalue()

        # All characters are valid
        self.assertFalse('too bad' in out)

        # You win is displayed
        self.assertTrue(hangman.getYouWin() in out)

        # Play again is asked
        self.assertTrue(hangman.play_again != None)

    def test_feedback_lose(self):
        hangman = Hangman(True, 9, 'hangman')
        f = io.StringIO()
        with redirect_stdout(f):
            for character in 'bcdefijkl':
                with mock.patch('builtins.input', return_value=character):
                    hangman.turn()

            # Simulate play again
            with mock.patch('builtins.input', return_value='n'):
                hangman.turn()
        out = f.getvalue()

        # All characters are invalid
        self.assertFalse('Good guess!' in out)

        # You lose is displayed
        self.assertTrue(hangman.getYouLose() in out)

        # Play again is asked
        self.assertTrue(hangman.play_again != None)

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

    def test_user_plays_again_sets_same_word_when_provided(self):
        hangman = Hangman(False, 9, 'hangman')
        word_1 = hangman.word
        hangman = Hangman(False, 9, 'hangman')
        word_2 = hangman.word
        self.assertTrue(word_1 == word_2)

    def test_user_plays_again_sets_new_word_when_not_provided(self):
        hangman = Hangman()
        word_1 = hangman.word
        hangman = Hangman()
        word_2 = hangman.word
        self.assertTrue(word_1 != word_2)
    
    def test_play_again_only_input_y_plays_again(self):
        for character in string.printable:
            hangman = Hangman()
            hangman.play_again = character
            self.assertEqual(hangman.willPlayAgain(), character.upper() == 'Y')

if __name__ == '__main__':
    unittest.main()