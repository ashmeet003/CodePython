# Ashmeet Kaur
# CompB10 Fall2025
# The program is based on number guessing Game

import random
# the above line tells Python that we want to
# import and use the random module.

intSecretNumber = random.randint(1,10)
# The line above uses the random module's randint (random integer)
# function to generate a random int between 1 and 10.
# The random number is assigned to the variable "intSecretNumber"

# the following block of code will run till the user guesses the number right
# or if the user chooses to play again
while True:
    intUserGuess = int(input("Guess a number between 1 and 10: "))
    # this line of code asks the user to input a number between 1 and 10,
    # converts their input string to an int,
    # and then assigns it to "intUSerGuess".

    if(intUserGuess == intSecretNumber):                                        # prints if input is equal to random number
        print("You got the number right!")
        print("Computer's number is: " + str(intSecretNumber))
        print("\n" + "*"*60)
        rePlay = input("\nDo you want to play again? (y/n): ").strip().lower()  #asks the user if wants to play again
        if(rePlay == "y" or rePlay == "yes"):                                   # if yes, a secret random number is chosen and game continues
            intSecretNumber = random.randint(1, 10)
            continue
        else:                                                                   # if no, then user exits the game
            print("Thank you for playing!")
            break
    else:                                                                        # prints if numbers are not equal and secret number is revealed
        print("You guessed the number wrong.")
        if(intUserGuess > intSecretNumber):                                     # if a user chooses a number high
            print("You guessed too high. Try again.\n")                         # prints appropriate message and game continues
        else:
            print("You guessed too low. Try again.\n")