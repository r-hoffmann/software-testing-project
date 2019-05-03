import os, random, string

class Hangman(object):
	def __init__(self, interactive=False, max_lives=9, word=None):
		self.interactive = interactive
		self.alphabet = string.ascii_uppercase
		self.max_lives = max_lives
		if word != None:
			self.word = word.upper()
			self.word_provided = True
		else:
			self.word_provided = False
		self.first_time = True

		# Initialize game
		if not self.word_provided:
			self.word = self.getWord()

		self.visible_word = "".join(["_" for w in self.word])
		self.guessed_characters = ''
		self.lives = self.max_lives
		self.finished = False
		self.play_again = None

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

		for w in self.word:
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
		if not self.word_provided:
			self.word = self.getWord()

		self.visible_word = "".join(["_" for w in self.word])
		self.guessed_characters = ''
		self.lives = self.max_lives
		self.finished = False
		self.play_again = None

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

		if self.first_time:
			self.printWelcome()
		self.printWordInfo()
		self.first_time = False
		self.printPlayWord()
		self.printLine()

		while not self.wordCompleted() and self.alive():
			self.turn()

	def livesLost(self):
		return self.max_lives - self.lives
	
	def alive(self):
		return self.lives > 0

	def willPlayAgain(self):
		play_again = self.play_again.upper() == 'Y'
		return play_again
	# /Functional Functions

	# Interactive Functions
	def promptPlayAgain(self):
		try:
			self.play_again = input('Enter (y/Y) to play again, any other key to exit ').upper()
		except (EOFError, KeyboardInterrupt):
			# Simulate wrong input
			self.play_again = 'n'
			
		if self.willPlayAgain():
			self.play()
		else:
			if self.interactive:
				self.printThanksForPlaying()

	def promptInputUser(self):
		try:
			self.guessed_character = input("Please guess a letter: ").upper()
		except (EOFError, KeyboardInterrupt):
			# Simulate wrong input
			self.guessed_character = ''

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
		if self.first_time:
			s = """\n  How to play: 
  1. On every turn you can guess an alphabetic character
  2. The challenge is to guess the word before 9 incorrect guesses
  3. After the game you have a chance to go for another round
  4. Good luck & have fun!\n\n"""
		else:
			s = ""
		return s + "I'm thinking of a word that is {} characters long...\n\n".format(len(self.word))

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

	def getYouWin(self):
		return(r"""          __   __                     _       
          \ \ / /                    (_)      
           \ V /___  _   _  __      ___ _ __  
            \ // _ \| | | | \ \ /\ / / | '_ \ 
            | | (_) | |_| |  \ V  V /| | | | |
            \_/\___/ \__,_|   \_/\_/ |_|_| |_|
			""")

	def getYouLose(self):
		return(r"""          __   __            _                 
          \ \ / /           | |                
           \ V /___  _   _  | | ___  ___  ___  
            \ // _ \| | | | | |/ _ \/ __|/ _ \ 
            | | (_) | |_| | | | (_) \__ \  __/ 
            \_/\___/ \__,_| |_|\___/|___/\___|
			""")

	def getWelcome(self):
		return(r"""           _    _      _                            _____     
          | |  | |    | |                          |_   _|    
          | |  | | ___| | ___ ___  _ __ ___   ___    | | ___  
          | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \ 
          \  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) |
           \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \_/\___/ 
                                                    
                                                    
            _   _   ___   _   _ _____ ___  ___  ___   _   _   
           | | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |  
           | |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |  
           |  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |  
           | | | || | | || |\  | |_\ \| |  | || | | || |\  |  
           \_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/""")

	def printYouLose(self):
		print(self.getYouLose())
		print('           The word was {}'.format(self.word))

	def printYouWin(self):
		print(self.getYouWin())
		print('           The word was {}'.format(self.word))

	def getThanksForPlaying(self):
		return('\n           Thanks for playing!\n')

	def printThanksForPlaying(self):
		print(self.getThanksForPlaying())
			
	def drawInterface(self):
		if self.gameEndStatus != None:
			if self.gameEndStatus == 1:
				self.printYouWin()
			else:
				self.printYouLose()
			self.printLine()
			self.promptPlayAgain()
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

