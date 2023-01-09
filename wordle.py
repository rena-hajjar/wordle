'''
This program is an imitation game of wordle. A random word is chosen from a list of words, and the user gets 6 tries to
guess what the word is while being told which letters in their guess are correct or not. If the user enters a guess with duplicates
of letters, they will be asked to enter a new guess as none of the magic words have duplicate letters.

Author: Rena Hajjar
Date: November 2 2022
'''
import random

def chooseWord():
    """
    This function chooses a word from a pre-defined list.
    Parameters:  None
    Return Value: a string representing the secret word
    """

    #This function was not modified by me, it was made my my CISC 101 professor Wendy Powley for this assignment
    
    validWords = ["could", "smile", "ultra", "extra", \
                  "beacon", "hearts", "cap", "wordle", \
                  "computing", "python"]

    #random.randint(0, 5) will generate an integer between 0 and 5 (inclusive)
    #this is then used to select a value from the list validWords.

    wordPosition = random.randint(0,len(validWords)-1)

    return validWords[wordPosition]

    

def checkLetters(secretWord, userWord):
    """
    This function checks the letters guessed by the user against the secret
    word and informs the user as to which letters are in the correct location,
    which letters are in the word but not in the correct location and which
    letters are not in the word.
    Paramters:   secretWord, userWord - strings
    Returns:  None
    """

    for x in userWord: 
        position = userWord.find(x) #stores the index of the specific letter to compare later
        if x in secretWord: #courses of action if the letter is in the correct word, finds where it is in the word
            if x == secretWord[position]:
                print(x.upper(), "is in the correct place!")
            else:
                print(x.upper(), "is in the word, not in this spot.")
        else:
            print(x.upper(), "is not in the word.")

    
def checkForDuplicates(userWord):
    """
    This function checks the user's word for duplicate letters.
    If there are duplicate letters, the function returns True, otherwise, False.
    Parameters:  userWord - string
    Return:  Boolean
    """

    #for loop compares each letter to every other letter in the entered word to ensure the user didn't use duplicates
    for x in range(len(userWord)):
        for y in range(len(userWord)):
            if userWord[x] == userWord[y] and x != y:
                return True

    #if there are no duplicates, the function will return False
    return False
    
    
def play(secretWord):
    """
    This function allows the user to play the game, entering up to 6 words to
    try to guess the secret word. When the correct word is guessed, the play
    stops and the user is congratulated.
    Parameters: string representing the secretWord
    Return Value:  None
    """

    #you may use a for loop with a break in this function.  You will break
    #when/if the user wins the game.

    
    userWord = input("Type what you think the word is here to start the game: ")

    numGuess = 1

    while win != True and numGuess <= 6: #ensures that the user has not won and they are still not past the 6 guesses given
        duplicates = checkForDuplicates(userWord)
        while duplicates: #continuously asks user for a new guess while their old guess has duplicate letters
            userWord = input("Your guess shouldn't have any duplicate letters. Please enter a new guess: ")
            duplicates = checkForDuplicates(userWord)

        
        if userWord == secretWord: #checks if user has guessed correctly
            win = True
            print("CONGRATULATIONS, the word was", secretWord, "!!!")
            numGuess = 7
        else: #if not guessed correctly, tells the user which letters are correctly placed or not and asks for the next guess
            if duplicates != True:
                checkLetters(secretWord, userWord)
            userWord = input("Enter your next guess: ")
        numGuess+=1
    

def main():
    """
    This implements the user interface for the program.
    """

    magicWord = chooseWord() #chooses a random word to be the correct word

    print(magicWord) #prints for assignment to be checked

    print("Welcome to Wordle!")

    print("The magic word is", len(magicWord), "letters long.")

    play(magicWord)#starts the game
    
main()
