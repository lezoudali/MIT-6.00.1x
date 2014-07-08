# 6.00 Problem Set 3
# 
# Hangman game
#
# -----------------------------------


import random
import string

#change to word.txt directory
WORDLIST_FILENAME = "/Users/lezoujonathan/Desktop/hangman/words.txt" 

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

# This is was a assignement for a MOOC class
# I wrote all the codes below the dashed line
# -----------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for e in secretWord:
        if not(e in lettersGuessed):
            return False
    return True
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = []
    for i in secretWord:
        guess.append(' ')
        guess.append('_')
    for e in lettersGuessed:
        inc = 0
        for i in secretWord:
            if e == i:
                guess[inc+(inc+1)] = i
            inc +=1
    guess = guess[1:]
    string = ''
    for i in guess:
        string += i
    return string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in lettersGuessed:
        letters = letters.replace(i, '')
    return letters

def alreadyGuess(guess, lettersGuessed):
    for i in lettersGuessed:
        if i == guess:
            return True 
    return False 
    
def isGuessGood(guess, secretWord):
    
    for i in secretWord:
        if guess == i:
            return True
    return False
               
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print ''
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    i = 8
    guess = ''
    lettersGuessed = []
    while i > 0:
        print ''
        print '-----------'
        print ''
        print 'You have ' + str(i) + ' guesses left.'
        print 'Available Letters: ' + getAvailableLetters(lettersGuessed) 
        guess = ''
        while guess == '':       
            guess = raw_input("Please guess a letter: ")
            guess = guess.lower()
            if len(guess)>1:
                guess = guess[0]
        AlreadyGuessed = alreadyGuess(guess, lettersGuessed)
        if AlreadyGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
        else:
            lettersGuessed.append(guess)
            goodGuess = isGuessGood(guess, secretWord)
            if goodGuess:
                print "Good Guess: " + getGuessedWord(secretWord, lettersGuessed) 
                if (isWordGuessed(secretWord, lettersGuessed)):
                    print "Congratulations, you won!"
                    break       
            else:
                print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
                i -= 1
   
        print "Letters Guessed: " + str(lettersGuessed)
        
    if i == 0:
        print "Sorry, you ran out of guesses. The word was " + str(secretWord)
              
# -----------------------------------

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
