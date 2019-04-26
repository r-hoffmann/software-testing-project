import os, string

class Hangman(object):
	def __init__(self, interactive=False, max_lives=9, word=None):
		self.interactive=interactive
		self.alphabet = string.ascii_lowercase
		if word == None:
			self.word = self.getWord()
		else:
			self.word = word

		self.visible_word = "".join(["_" for w in self.word])
		self.guessed_characters = ''
		self.max_lives = max_lives
		self.lives = self.max_lives
		self.finished = False

	# Functional Functions
	def getWord(self):
		return "kaas"

	def turn(self):
		guessed_character = self.promptInputUser()
		self.processInput(guessed_character)
		if self.interactive:
			self.printLives()
			self.printStatus()
			self.printHangman()
			self.printLine()
	
	def characterAlreadyGuessed(self, guessed_character):
		if guessed_character in self.guessed_characters:
			if self.interactive:
				print("You've already tried \"{}\", please choose another.".format(guessed_character))
			return True
		return False

	def characterInWord(self, guessed_character):
		return guessed_character in self.word

	def wordCompleted(self):
		return self.visible_word == self.word

	def updateVisibleWord(self):
		self.visible_word = ''
		for i, w in enumerate(self.word):
			if w in self.guessed_characters:
				self.visible_word += w
			else:
				self.visible_word += '_'

	def processInput(self, guessed_character):	
		if self.characterAlreadyGuessed(guessed_character):
			self.promptInputUser()
		else:
			self.guessed_characters += guessed_character
			if self.characterInWord(guessed_character):
				self.updateVisibleWord()

				if self.wordCompleted():
					self.finished = True
					self.won = True
					if self.interactive:
						print("\nYou win! The word was: {}\n".format(self.word.upper()))
				else:
					if self.interactive:
						print("Good guess! \"{}\" is part of the word!\n".format(guessed_character.upper()))
			else:
				if self.interactive:
					print(u"\nAah, too bad! \"{}\" is not part of the word! -♥\n".format(guessed_character.upper()))

				self.lives -= 1
				if not self.alive():
					self.finished = True
					self.won = False
					if self.interactive:
						print("YOU HANG... The word was: {}".format(self.word.upper()))

	def play(self):
		self.printWelcome()
		self.printHangman()
		while not self.wordCompleted() and self.alive():
			self.turn()
			if self.interactive:
				self.drawInterface()

	def livesLost(self):
		return self.max_lives - self.lives
	
	def alive(self):
		return self.lives > 0
	# /Functional Functions

	# Interactive Functions
	def promptInputUser(self):

		guessed_character = input("Please guess a letter: ").lower()
		self.printLine()

		print('You guessed: "{}"'.format(guessed_character.upper()))

		while not self.validUserInput(guessed_character):
			print("False input, try again.\n")
			# self.printLine()

			return self.promptInputUser()
		return guessed_character

	def validUserInput(self, guessed_character):
		return len(guessed_character) == 1 and guessed_character in self.alphabet

	def getLine(self, n=50):
		return "-" * n + ""

	def printLine(self, n=50):
		print(self.getLine(n))

	def printLives(self):
		print(u'[ ' + '♥ '*self.lives + '  '*self.livesLost()+']')

	def getWelcome(self):
		# print("You have " + str(self.max_lives) + " lives guess it...")
		return "\nWELCOME TO HANGMAN!\n\nHow to play: \n1. Enter alphabetical characters\n2. Have fun!\n\nI'm thinking of a word that is {} characters long...?\n\n".format(len(self.word))

	def printWelcome(self):
		print(self.getWelcome())

	def getStatus(self):
		return "Guessed characters: {}\nWord: {}\n".format(
			 
			"[ " + ''.join([character.upper() + ' ' if character.isalpha() else '_ ' for character in list(self.guessed_characters)]) + "]",
			''.join([character.upper()+' ' if character.isalpha() else '_ ' for character in list(self.visible_word)])
			)

	def printStatus(self):
		print(self.getStatus())

	def getHangman(self):
		printed_hangman = {
			0: "\n"*8,
			1: "\n" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n",
			2: "\n_________" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n",
			3: "\n_________" + "\n|        |" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n",
			4: "\n_________" + "\n|        |" + "\n|        0" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n",
			5: "\n_________" + "\n|        |" + "\n|        0" + "\n|        |" + "\n|" + "\n|" + "\n|_______________________\n",
			6: "\n_________" + "\n|        |" + "\n|        0" + "\n|       /|" + "\n|" + "\n|" + "\n|_______________________\n",
			7: "\n_________" + "\n|        |" + "\n|        0" + "\n|       /|\\" + "\n|" + "\n|" + "\n|_______________________\n",
			8: "\n_________" + "\n|        |" + "\n|        0" + "\n|       /|\\" + "\n|        ^" +  "\n|                 " + "\n|_______________________\n",
			9: "\n_________" + "\n|        |" + "\n|        0" + "\n|       /|\\" + "\n|        ^" + " \n|       / \\      " + "\n|_______________________\n"
		}
		return printed_hangman[self.livesLost()]

	def printHangman(self):
		print(self.getHangman())
	
	def drawInterface(self):
		pass
	# /Interactive Functions
	

if __name__ == '__main__':
	hangman = Hangman(True)
	hangman.play()
