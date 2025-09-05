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

intUserGuess = int(input("Guess a number between 1 and 10: "))
# this line of code asks the user to input a number between 1 and 10,
# converts their input string to an int,
# and then assigns it to "intUSerGuess".

if(intUserGuess == intSecretNumber):  # prints if input is equal to random number
    print("You got the number right!")
else:                                 # prints if numbers are not equal and secret number is revealed
    print("You guessed the number wrong.")
    print("The secret number is:", intSecretNumber)