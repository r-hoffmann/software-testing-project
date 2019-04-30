import os, random, string

class Hangman(object):
	def __init__(self, interactive=False, max_lives=9, word=None):
		self.interactive = interactive
		self.alphabet = string.ascii_uppercase
		if word == None:
			self.word = self.getWord()
		else:
			self.word = word.upper()

		self.visible_word = "".join(["_" for w in self.word])
		self.guessed_characters = ''
		self.max_lives = max_lives
		self.lives = self.max_lives
		self.finished = False

		'''
		userInputStatus:		0. Already Tried
								1. Good guess
								2. Wrong Guess
								3. Wrong input

		'''
		self.userInputStatus = None

		'''
		gameEndStatus:			0. Loss
								1. Win
		'''		
		self.gameEndStatus = None
		self.guessed_character = None

	# Functional Functions
	def getWord(self):
		from words import words 

		wordlist = words.split()
		return wordlist[random.randint(0,len(wordlist) - 1)].upper()

	def turn(self):
		self.userInputStatus = 0
		self.promptInputUser()
		if self.userInputStatus == 0:
			self.processInput()
		if self.interactive:
			self.drawInterface()
	
	def characterAlreadyGuessed(self):
		if self.guessed_character != None and self.guessed_character in self.guessed_characters:
			if self.interactive:
				self.userInputStatus = 0
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
		if self.guessed_character == None:
			return 
		if self.characterAlreadyGuessed():
			self.userInputStatus = 0 
		else:
			self.guessed_characters += self.guessed_character
			self.guessed_characters = sorted(self.guessed_characters)
			if self.characterInWord():
				self.updateVisibleWord()

				if self.wordCompleted():
					self.finished = True
					self.won = True
					if self.interactive:
						self.gameEndStatus = 1
				else:
					if self.interactive:
						self.userInputStatus = 1
			else:
				if self.interactive:
					self.userInputStatus = 2

				self.lives -= 1
				if not self.alive():
					self.finished = True
					self.won = False
					if self.interactive:
						self.gameEndStatus = 0

	def play(self):
		self.userInputStatus = 0
		self.drawInterface()
		while not self.wordCompleted() and self.alive():
			self.turn()

	def livesLost(self):
		return self.max_lives - self.lives
	
	def alive(self):
		return self.lives > 0
	# /Functional Functions

	# Interactive Functions
	def promptInputUser(self):
		self.guessed_character = input("Please guess a letter: ").upper()
		if not self.validUserInput():
			self.userInputStatus = 3

	def validUserInput(self):
		return len(self.guessed_character) == 1 and self.guessed_character in self.alphabet

	def getLine(self, n=50):
		return "_" * n

	def printLine(self, n=50):
		print(self.getLine(n))

	def printLives(self):
		print(u'          [ ' + '♥ '*self.lives + '  '*self.livesLost()+'] X {}'.format(self.lives))

	def getWordInfo(self):
		return "\n          How to play: \n            1. Enter alphabetical characters\n            2. Have fun!\n\n          I'm thinking of a word that is {} characters long...?\n\n".format(len(self.word))

	def printWordInfo(self):
		print(self.getWordInfo())

	def printWelcome(self):
		print(self.getWelcome())

	def getPlayWord(self):
		return "          " + "_"*(len(self.word)*(2)+6) + "\n" + "\n          {}\n".format(
			''.join([character.upper()+' ' if character.isalpha() else '_ ' for character in list(self.visible_word)])
			) + "          " + "_"*(len(self.word)*(2)+6)

	def printPlayWord(self):
		print(self.getPlayWord())

	def getHangman(self):
		printed_hangman = {
			0: "\n"*8,
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
		if self.guessed_characters != '':
			print("\n          [ " + ''.join([character.upper() + ' ' if character.isalpha() else '_ ' for character in list(self.guessed_characters)]) + "]")
		print(self.getHangman())

	def YouWin(self):
		return(
"          __   __                     _       \n"
"          \ \ / /                    (_)      \n"
"           \ V /___  _   _  __      ___ _ __  \n"
"            \ // _ \| | | | \ \ /\ / / | '_ \ \n"
"            | | (_) | |_| |  \ V  V /| | | | |\n"
"            \_/\___/ \__,_|   \_/\_/ |_|_| |_|\n")

	def getYouLose(self):
		return(
"          __   __            _                 \n"
"          \ \ / /           | |                \n"
"           \ V /___  _   _  | | ___  ___  ___  \n"
"            \ // _ \| | | | | |/ _ \/ __|/ _ \ \n"
"            | | (_) | |_| | | | (_) \__ \  __/ \n"
"            \_/\___/ \__,_| |_|\___/|___/\___| \n")

	def getWelcome(self):
		print(
"           _    _      _                            _____     \n"
"          | |  | |    | |                          |_   _|    \n"
"          | |  | | ___| | ___ ___  _ __ ___   ___    | | ___  \n"
"          | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \ \n"
"          \  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) |\n"
"           \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \_/\___/ \n"
                                                    "\n"
                                                    "\n"
"           _   _   ___   _   _ _____ ___  ___  ___   _   _   \n"
"           | | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |  \n"
"           | |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |  \n"
"           |  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |  \n"
"           | | | || | | || |\  | |_\ \| |  | || | | || |\  |  \n"
"           \_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/  \n"
                                                    
		)

	def printYouLose(self):
		print(self.getYouLose())
		print('           The word was {}'.format(self.word))

	def printYouWin(self):
		print(self.YouWin())
		print('           The word was {}'.format(self.word))
			
	def drawInterface(self):
		if self.gameEndStatus != None:
			if self.gameEndStatus == 1:
				self.printYouWin()
			else:
				self.printYouLose()
			return


		if self.guessed_character == None:
			self.guessed_character_uppercase = ''
		else:
			self.guessed_character_uppercase = self.guessed_character.upper()
			
		self.printStatus = {
			"userInput": {
				0: "\n          You've already tried \"{}\", please choose another.".format(self.guessed_character),
				1: "\n          Good guess! \"{}\" is part of the word!".format(self.guessed_character_uppercase),
				2: u"\n          Aah, too bad! \"{}\" is not part of the word! -♥".format(self.guessed_character_uppercase),
				3: "\n          False input, try again."
			},
			"guessed":'          You guessed: "{}"'.format(self.guessed_character_uppercase)
		}

		print()
		print(self.printStatus['guessed'])
		print(self.printStatus['userInput'][self.userInputStatus])
		self.printHangman()
		self.printLives()
		self.printPlayWord()
		print()
		self.printLine()
	# /Interactive Functions
	

if __name__ == '__main__':
	hangman = Hangman(True)
	hangman.play()

