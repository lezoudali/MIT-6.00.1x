from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#


def isCompWordValid(word, hand):
    handCopy = hand.copy()
    for letter in word:
        if letter in handCopy.keys():
            handCopy[letter] = handCopy.get(letter, 0)-1
            if handCopy[letter] < 0:
                return False
        else:
            return False
    return True 
    
def compChooseWord(hand, wordList, n):
    maxScore = 0                                                # Create a new variable to store the maximum score seen so far (initially 0)
    bestWord = None                                             # Create a new variable to store the best word seen so far (initially None)  
    validWord = False    
    for word in wordList:                                       # For each word in the wordList
        validWord = isCompWordValid(word, hand)
        if validWord == True:                                   # If you can construct the word from your hand
            tempScore = getWordScore(word, n)                   # Find out how much making that word is worth
            if maxScore < tempScore:                            # If the score for that word is higher than your best score
                maxScore = tempScore                            # Update your best score, and best word accordingly
                bestWord = word
    return bestWord                                             # return the best word you found.

#
# Problem #7: Computer plays a hand
#

def compPlayHand(hand, wordList, n):
    total = 0                                                                          # Keep track of the total score
    word = ''
    test = False
    for i in hand.keys():
        if hand.get(i,0) > 0:
            test = True    
  
    while test:                                                                         # As long as there are still letters left in the hand:
        print 'Current hand: ',
        displayHand(hand)                                                               # Display the hand
        word =  compChooseWord(hand, wordList, n)                                       # Ask user for input 
        if word == None:                                                                # If the input is a single period:
            break                                                                       # End the game (break out of the loop)
        else:                                                                           # Otherwise (the input is not a single period):                                                                       # Otherwise (the word is valid):
            total += getWordScore(word, n)       
            print "'"+str(word)+"'" + ' earned', 
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
# Problem #8: Playing a game
#
#
def playGame(wordList):

    hand = {}
    n = HAND_SIZE
    option = ''
    while option == '':
        option = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        try:
            if option != 'r' and option != 'n' and option != 'e':
                    raise ValueError('Invalid command.')
            
            if option == 'r' and hand == {}:
                raise NameError('You have not played a hand yet. Please play a new hand first!')
            elif option == 'e':
                break
                
            option2 = ''
            while option2 == '':
                option2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if option2 != 'c' and option2 != 'u':
                    print 'Invalid command.'
                    option2 = ''
                    
            if option == 'r':
                if option2 == 'u':
                    playHand(hand, wordList, n)
                else:
                    compPlayHand(hand, wordList, n)
                    
            elif option == 'n':
                if option2 == 'u':
                    hand = dealHand(n)
                    playHand(hand, wordList, n) 
                else:
                    hand = dealHand(n)
                    compPlayHand(hand, wordList, n)       
        except NameError, e:
            print str(e)
        except ValueError, e:
            print str(e)
        finally:
            option = ''




        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


