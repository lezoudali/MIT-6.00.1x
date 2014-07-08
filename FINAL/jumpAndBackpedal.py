def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1 
    while True:
        if isMyNumber(guess) == 0:
            return guess
        elif isMyNumber(guess) == 1:
            guess -=1
        else:
            guess *=2
    return guess