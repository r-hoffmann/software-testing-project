import os

def line(n=50):
	print("-" * n + "\n") 

class Hangman(object):
	def __init__(self, max_lives=9, word=None):
		self.alphabet = "abcdefghijklmnopqrstuvwxyz"
		if word == None:
			self.word = self.getWord()
		else:
			self.word = word

		self.visible_word = "".join(["_" for w in self.word])
		self.guessed_characters = ''
		self.max_lives = max_lives
		self.alive = True

	def getWord(self):
		return "kaas"

	def printWelcome(self):
		print("Welcome to hangman!\n")
		print("I'm thinking of a word that is {} characters long.".format(len(self.word)))
		# print("You have " + str(self.max_lives) + " lives guess it...")
		line()

	def status(self):
		print("Word: " + self.visible_word)
		print("Guessed characters: " + self.guessed_characters)

	def turn(self):
		self.status()
		print()
		self.promptInputUser()
		self.draw_hangman(self.max_lives - self.lives)
		line()

	def promptInputUser(self):
		guessed_character = input("Please guess a letter: ").lower()
		self.check_input_user(guessed_character)

	def check_input_user(self, guessed_character):
		# guessed_word = ''.join(x for x in self.visible_word if x.isalpha())

		if guessed_character not in self.alphabet or not len(guessed_character) == 1:
			print("False input, try again.")
			self.promptInputUser()
		elif guessed_character in self.guessed_characters:
			print("You've already tried \"" + guessed_character + "\", please choose another.")
			self.promptInputUser()
		elif guessed_character in self.word:
			self.guessed_characters += guessed_character

			temp = list(self.visible_word)
			for i, w in enumerate(self.word):
				if w == guessed_character:
					temp[i] = guessed_character
				
			self.visible_word = ''.join(temp)

			if self.visible_word == self.word:
				self.alive = False
				print("\nYou win! The word was: {}".format(self.visible_word))
			else:
				print("Good guess! \"" + guessed_character + "\" is part of the word!")

		else:
			print("\"" + guessed_character + "\" is not part of the word! You lose one live...")
			self.guessed_characters += guessed_character

			self.lives -= 1

			if self.lives < 1:
				print("YOU HANG...")
				self.alive = False

	def draw_hangman(self, errors):
		hangman = ''
		if errors == 1:
			hangman = "\n" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n"
		elif errors == 2:
			hangman = "\n_________" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n"
		elif errors == 3:
			hangman =  "\n________" + "\n|       |" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n"
		elif errors == 4:
			hangman =  "\n________" + "\n|       |" + "\n|       O" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n"
		elif errors == 5:
			hangman =  "\n________" + "\n|       |" + "\n|       O" + "\n|       |" + "\n|" + "\n|" + "\n|_______________________\n"
		elif errors == 6:
			hangman =  "\n________" + "\n|       |" + "\n|       O" + "\n|      /|" + "\n|" + "\n|" + "\n|_______________________\n"
		elif errors == 7:
			hangman =  "\n________" + "\n|       |" + "\n|       O" + "\n|      /|\\" + "\n|" + "\n|" + "\n|_______________________\n"
		elif errors == 8:
			hangman = "\n_________" + "\n|        |" + "\n|        O" + "\n|       /|\\" + "\n|        ^" +  "\n|                 " + "\n|_______________________\n"
		elif errors == 9:
			hangman = "\n_________" + "\n|        |" + "\n|        O" + "\n|       /|\\" + "\n|        ^" + " \n|       / \\      " + "\n|_______________________\n"
		print(hangman)

	def play(self):
		self.lives = self.max_lives
		self.printWelcome()
		while self.alive:
			self.turn()
			

if __name__ == '__main__':
	hangman = Hangman()
	hangman.play()
