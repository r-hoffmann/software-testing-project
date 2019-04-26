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
        pass
        
    def test_letter_correct(self):
        pass
        
    def test_incorrect_letter_changes_hangman(self):
        pass
        
    def test_incorrect_letter_reduces_lives(self):
        pass
        
    def test_number_of_tries_limited(self):
        pass
        
    def test_user_completes_word_implies_win(self):
        pass
        
    def test_user_without_lives_implies_loss(self):
        pass
        
    def test_supply_feedback(self):
        pass
        
    def test_user_enters_valid_character(self):
        hangman = Hangman()
        for s in string.printable:
            valid = hangman.validUserInput(s)
            self.assertEqual(valid, s in string.ascii_lowercase)
        
    def test_user_guesses_last_character(self):
        pass
        
    def test_user_enters_invalid_character(self):
        pass
        
    def test_user_enters_punctuation(self):
        pass

    def test_user_enters_number(self):
        pass
        
    def test_user_enters_multiple_characters(self):
        pass
        
    def test_user_enters_no_character(self):
        pass
        
    def test_user_enters_same_character_multiple_times(self):
        pass
        
        
if __name__ == '__main__':
    unittest.main()