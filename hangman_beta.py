import os, random, string

class Hangman(object):
	def __init__(self, interactive=False, max_lives=9, word=None):
		self.interactive = interactive
		self.alphabet = string.ascii_uppercase
		if word == None:
			self.word = self.getWord()
		else:
			self.word = word

		self.visible_word = "".join(["_" for w in self.word])
		self.guessed_characters = ''
		self.max_lives = max_lives
		self.lives = self.max_lives
		self.finished = False

		self.userInputStatus = None
		self.gameEndStatus = None
		self.guessed_character = None


		
	# def printInputStatus():
	# 	return self.printStatus['userInput'][self.input_status]
	# Functional Functions
	def getWord(self):
		return "aardbeitje".upper()

		from words import words 

		# wordlist: list of strings
		wordlist = words.split()
		return wordlist[random.randint(0,len(wordlist) - 1)].upper()

	def turn(self):
		self.guessed_character = self.promptInputUser()
		self.processInput()
		if self.interactive:
			self.drawInterface()
			# self.printLives()
			# self.printStatus()
			# self.printHangman()
			# self.printLine()
	
	def characterAlreadyGuessed(self):
		if self.guessed_character in self.guessed_characters:
			if self.interactive:
				self.userInputStatus = 0
				# print("You've already tried \"{}\", please choose another.".format(guessed_character))
			return True
		return False

	def characterInWord(self):
		return self.guessed_character in self.word

	def wordCompleted(self):
		return self.visible_word == self.word

	def updateVisibleWord(self):
		self.visible_word = ''

		for i, w in enumerate(self.word):
			if w in self.guessed_characters:
				self.visible_word += w
			else:
				self.visible_word += '_'

	def processInput(self):	
		if self.characterAlreadyGuessed():
			self.promptInputUser()
		else:
			self.guessed_characters += self.guessed_character
			self.guessed_characters = sorted(self.guessed_characters)
			if self.characterInWord():
				self.updateVisibleWord()

				if self.wordCompleted():
					self.finished = True
					self.won = True
					if self.interactive:
						self.gameEndStatus = 1;

						# print("\n          You win! The word was: {}\n".format(self.word.upper()))
				else:
					if self.interactive:
						self.userInputStatus = 1
						# print("\n          Good guess! \"{}\" is part of the word!\n".format(guessed_character.upper()))
			else:
				if self.interactive:
					self.userInputStatus = 2
					# print(u"\n          Aah, too bad! \"{}\" is not part of the word! -♥\n".format(guessed_character.upper()))

				self.lives -= 1
				if not self.alive():
					self.finished = True
					self.won = False
					if self.interactive:
						self.gameEndStatus = 0;
						# print("\n          YOU HANG... The word was: {}".format(self.word.upper()))

	def play(self):
		self.printWelcome()
		self.printHangman()
		while not self.wordCompleted() and self.alive():
			self.turn()
			# if self.interactive:
			# 	self.drawInterface()

	def livesLost(self):
		return self.max_lives - self.lives
	
	def alive(self):
		return self.lives > 0
	# /Functional Functions

	# Interactive Functions
	def promptInputUser(self):
		self.guessed_character = input("Please guess a letter: ").upper()
		# self.printLine()

		# print('          You guessed: "{}"'.format(guessed_character.upper()))

		while not self.validUserInput():
			print("          False input, try again.\n")
			# self.printLine()

			return self.promptInputUser()
		return self.guessed_character

	def validUserInput(self):
		return len(self.guessed_character) == 1 and self.guessed_character in self.alphabet

	def getLine(self, n=50):
		return "-" * n + ""

	def printLine(self, n=50):
		print(self.getLine(n))

	def printLives(self):
		print(u'          [ ' + '♥ '*self.lives + '  '*self.livesLost()+'] X {}'.format(self.lives))

	def getWelcome(self):
		# print("You have " + str(self.max_lives) + " lives guess it...")
		return "\n          WELCOME TO HANGMAN!\n\n          How to play: \n            1. Enter alphabetical characters\n            2. Have fun!\n\n          I'm thinking of a word that is {} characters long...?\n\n".format(len(self.word))

	def printWelcome(self):
		print(self.getWelcome())

	def getStatus(self):
		return "          " + "_"*(len(self.word)*(2)+6) + "\n" + "\n          {}\n".format(
			# "[ " + ''.join([character.upper() + ' ' if character.isalpha() else '_ ' for character in list(self.guessed_characters)]) + "]",
			''.join([character.upper()+' ' if character.isalpha() else '_ ' for character in list(self.visible_word)])
			) + "          " + "_"*(len(self.word)*(2)+6)

	def printStatus(self):
		print(self.getStatus())

	def getHangman(self):
		printed_hangman = {
			0: "\n",
			1: "\n" + "\n          |" + "\n          |" + "\n          |          " + "\n          |" + "\n          |" + "\n          |_______________________\n",
			2: "\n          _________" + "\n          |" + "\n          |" + "\n          |" + "\n          |" + "\n          |" + "\n          |_______________________\n",
			3: "\n          _________" + "\n          |        |" + "\n          |" + "\n          |" + "\n          |" + "\n          |" + "\n          |_______________________\n",
			4: "\n          _________" + "\n          |        |" + "\n          |        0" + "\n          |" + "\n          |" + "\n          |" + "\n          |_______________________\n",
			5: "\n          _________" + "\n          |        |" + "\n          |        0" + "\n          |        |" + "\n          |" + "\n          |" + "\n          |_______________________\n",
			6: "\n          _________" + "\n          |        |" + "\n          |        0" + "\n          |       /|" + "\n          |" + "\n          |" + "\n          |_______________________\n",
			7: "\n          _________" + "\n          |        |" + "\n          |        0" + "\n          |       /|\\" + "\n          |" + "\n          |" + "\n          |_______________________\n",
			8: "\n          _________" + "\n          |        |" + "\n          |        0" + "\n          |       /|\\" + "\n          |        ^" +  "\n          |                 " + "\n          |_______________________\n",
			9: "\n          _________" + "\n          |        |" + "\n          |        0" + "\n          |       /|\\" + "\n          |        ^" + " \n          |       / \\      " + "\n          |_______________________\n"
		}
		return printed_hangman[self.livesLost()]

	def printHangman(self):
		if self.lives != self.max_lives:
			print("\n          [ " + ''.join([character.upper() + ' ' if character.isalpha() else '_ ' for character in list(self.guessed_characters)]) + "]"
				+ self.getHangman())
		else:
			print(self.getHangman())
			
	def drawInterface(self):
		
		self.printStatus = {
			"userInput": {
				0: "\n          You've already tried \"{}\", please choose another.".format(self.guessed_character),
				1: "\n          Good guess! \"{}\" is part of the word!\n".format(self.guessed_character.upper()),
				2: u"\n          Aah, too bad! \"{}\" is not part of the word! -♥\n".format(self.guessed_character.upper()),
			},
			"gameEnd" :{
				0: "\n          YOU HANG... The word was: {}".format(self.word.upper()),
				1: "\n          You win! The word was: {}\n".format(self.word.upper())
			},
			"guessed":'          You guessed: "{}"'.format(self.guessed_character.upper())
		}

		self.printLine()
		print(self.printStatus['guessed'])
		print(self.printStatus['userInput'][self.userInputStatus])
		self.printStatus()

		pass
	# /Interactive Functions
	

if __name__ == '__main__':
	hangman = Hangman(True)
	hangman.play()
