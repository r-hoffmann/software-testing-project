import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def hangman():
    # Het aantal levens, en alle letters uit het alfabet die geraad mogen worden.
    lives = 8
    letters = "abcdefghijklmnopqrstuvwxyz"

    # Een random woord uit de lijst halen.
    word = wordlist[random.randint(0,len(wordlist))]
    # introductie van 'hangman'
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(word))+" letters long.")

    # Het woord wat de gebruiker ziet
    VisibleWord = ""
    for i in range(len(word)):
        VisibleWord = VisibleWord+"_"

    # Het daadwerkelijke spel gaat door tot het woord is geraden, of als de levens op zijn.  
    done = False
    while done == False:
        print("-------------")
        print("You have "+str(lives)+" guesses left.")
        print("Available letters: "+str(letters))
        letter = input("Please guess a letter: ").lower()
        if letter not in letters or not len(letter) == 1:
            print("         False input, try again. My word: "+VisibleWord)
        else:
            lives -= 1
            if lives < 1:
                done = True
                print("Aww, you lost.")
                again = input("Try again?(Y) ").upper()
                if again == "Y":
                    print("")
                    hangman()
            if letter in word:
                for i in range(len(word)):
                    if word[i:i+1] == letter:
                        VisibleWord = VisibleWord[:i]+letter+VisibleWord[i+1:]
                print("Good guess: "+VisibleWord)
            else:
                print("Oops! That letter is not in my word: "+VisibleWord)
            if "_" not in VisibleWord:
                print("Congratulations! You won!")
                done = True
                again = input("Try again?(Y) ").upper()
                if again == "Y":
                    print("")
                    hangman()
            letters = letters.replace(letter,"")
    print("")
    print("The word was "+word+".")
    
hangman()