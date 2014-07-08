# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "/Users/lezoujonathan/Desktop/ProblemSet4/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    """
    # TO DO ... <-- Remove this comment when you code this function
    sum = 0
    for i in word:
        sum += int(SCRABBLE_LETTER_VALUES[i])
    sum *= len(word)
    if len(word) == n:
        sum += 50
    return sum

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    print out something like:
       a x x l l l e
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand are be VOWELS.

    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#

def updateHand(hand, word):
    '''
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    '''
    hand2 = hand.copy()
    for i in word:
        if hand2.get(i, 0) > 0:
            hand2[i] -= 1
            
    return hand2


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    """
    handCopy = hand.copy()
    if word in wordList:
        for letter in word:
            if letter in handCopy.keys():
                handCopy[letter] = handCopy.get(letter, 0)-1
                if handCopy[letter] < 0:
                    return False
            else:
                return False
        return True
    else:
        return False

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    """
    length = 0
    for i in hand.keys():
        if hand.get(i, 0) > 0:
            length += hand[i]
    return length


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand
    """    
    total = 0                                                                          # Keep track of the total score
    word = ''
    test = False
    for i in hand.keys():
        if hand.get(i,0) > 0:
            test = True    
  
    while test:                                                                         # As long as there are still letters left in the hand:
        print 'Current hand: ',
        displayHand(hand)                                                               # Display the hand
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')    # Ask user for input 
        if word == '.':                                                                 # If the input is a single period:
            break                                                                       # End the game (break out of the loop)
        else:                                                                           # Otherwise (the input is not a single period):
            if isValidWord(word, hand, wordList) == False:                              # If the word is not valid:
                print 'Invalid Word'                                                    # Reject invalid word (print a message followed by a blank line)
                print 
            else:                                                                       # Otherwise (the word is valid):
                total += getWordScore(word, n)       
                print str(word) + ' earned', 
                print str(getWordScore(word, n)),                                       # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print 'points.',
                print 'Total: ' + str(total)
                
                hand = updateHand(hand, word)                                           # Update the hand 
        test = False
        for i in hand.keys():
            if hand.get(i,0) > 0:
                test = True
    print 'Goodbye! Total score:',
    print str(total) + ' points.'                                                       # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    return 
#
# Problem #5: Playing a game
# 

def playGame(wordList):
    '''
    Allows the user to play an arbitrary number of hands.
    '''
    
    hand = {}
    n = HAND_SIZE
    option = ''
    while option == '':
        option = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        try:
            if option == 'r':
                if hand == {}:
                    raise NameError('You have not played a hand yet. Please play a new hand first!')
                else:
                    playHand(hand, wordList, n)
            elif option == 'n':
                hand = dealHand(n)
                playHand(hand, wordList, n)
            elif option != 'e':
                raise ValueError('Invalid command.')         
        except NameError, e:
            print str(e)
        except ValueError, e:
            print str(e)
        finally:
            if option == 'e':
                break
            else:
                option = ''

#
# Build data structures used for entire session and play game
#


if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
