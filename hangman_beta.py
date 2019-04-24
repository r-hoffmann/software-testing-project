word = 'kaas'
alphabet = "abcdefghijklmnopqrstuvwxyz"
VisibleWord = "_"*len(word)
guessed_characters = ''
MAX_LIVES = 9

lives = MAX_LIVES
correct = True

def main():
	
	greeting()
	print_game_info(word)
	while(correct):
		prompt_input_user()


def greeting():
	print("\n\n\nWELKOM TO HANGMAN!")

def print_game_info(word):
	global guessed_characters
	print("\n\nI'm thinking of a word that is "+ str(len(word)) + " characters long \n\n" + "_"*len(word)+'\n\n')
	print("guessed characters: "+ guessed_characters)


def prompt_input_user():
	guessed_character = input("Please guess a letter: ").lower()
	check_input_user(guessed_character)

def check_input_user(character):
	global VisibleWord
	global guessed_characters
	global lives
	global correct

	guessed_word = ''.join(x for x in VisibleWord if x.isalpha())
	print(guessed_word)

	if character not in alphabet or not len(character) == 1:
		print("         False input, try again. My word: {}".format(VisibleWord))
	elif character in guessed_characters:
		print('You\'ve already tried this character. Choose another.')
		prompt_input_user()
	elif character in word:
		
		guessed_characters += character

		temp = list(VisibleWord)
		for i in range(len(word)):
			if word[i:i+1] == character:
				temp[i] = character
			elif VisibleWord[i:i+1].isalpha():
				pass
			else:
				pass
			
		VisibleWord = "".join(x for x in temp)

		if VisibleWord == word:
			correct = False
			print("\n\nThats it! The word was: "+VisibleWord)
		else:
			print('You guessed a correct letter!\n Look at your guessed word so far...: '+VisibleWord)

	else:
		print("That was not correct! You lose one live.")
		guessed_characters += character

		lives -= 1
		draw_hangman((MAX_LIVES - lives))

		if lives < 1:
			print("YOU HANG...")
			correct = False

def draw_hangman(errors):
	hangman = ''
	if errors == 1:
		hangman = "\n" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n"
	elif errors == 2:
		hangman = "\n_________" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n"
	elif errors == 3:
		hangman =  "\n________" + "\n|       |" + "\n|" + "\n|" + "\n|" + "\n|" + "\n|_______________________\n";
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
			



main()