from random import *
randNumb = randint(0,20)



def newGuess(numbOfGuesses):

    userGuess = int(input("Enter a Guess: "))

    numbOfGuesses = numbOfGuesses + 1

    if userGuess == randNumb:
        print("Correct Answer!\n\nNumber of Guesses: ", numbOfGuesses)
    else:
        print("Incorrect Answer! Try Again.")
        if userGuess > randNumb:
            print("Too High!")
        elif userGuess < randNumb:
            print("Too Low!")

    if userGuess != randNumb:
        newGuess(numbOfGuesses)

newGuess(0)
