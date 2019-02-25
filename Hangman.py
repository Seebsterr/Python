
import string


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed: return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessingWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessingWord += letter
        else:
            guessingWord += '_ '
    return guessingWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in letters:
            letters.remove(letter)
    return ''.join(letters)


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
    '''

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {0} letters long'.format(len(secretWord)))

    lettersGuessed=[]
    i=8
    while i >0:
        print('-----------')
        print('You have {0} guesses left'.format(i))
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        inputLetter = input('Please guess a letter: ')
        lettersGuessed.append(" ")
        lettersGuessed.append(inputLetter)
        if isWordGuessed(secretWord,lettersGuessed) == True:
            print('Good guess: {0}'.format(secretWord))
            print('-----------')
            print('Congratulations, you won!')
            break

        lettersGuessed.remove(inputLetter)

        if inputLetter not in secretWord:
            lettersGuessed.append(inputLetter)
            print("Oops! That letter is not in my word: {0}".format(getGuessedWord(secretWord, lettersGuessed)))
            i-=1
        elif inputLetter in secretWord and  inputLetter not in lettersGuessed:
            lettersGuessed.append(inputLetter)
            print('Good guess: {0}'.format(getGuessedWord(secretWord, lettersGuessed)))
        elif inputLetter in lettersGuessed:
            lettersGuessed.append(inputLetter)
            print("Oops! You've already guessed that letter: {0}".format(getGuessedWord(secretWord, lettersGuessed)))


    print('-----------')
    if isWordGuessed(secretWord,lettersGuessed) == False:
        print('Expected: Sorry, you ran out of guesses. The word was {0}.'.format(secretWord))




secretWord='secret words'    # Here write your secret word
hangman(secretWord)
input("")

