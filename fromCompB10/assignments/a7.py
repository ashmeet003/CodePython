# Ashmeet Kaur
# CompB10 Fall2025
# Rock Paper Scissors
# Program pseudo:
#   userGuess(): takes a valid input from user
#   compGuess(): computer chooses a random pick
#   winner(): declares winner for a round
#   The main part of program calls the above function
#   and code runs in loop till user chooses to exit game

import random

# the function returns computer input
# based on random letter it chooses from list given
def compGuess():
    liChoice = ["r", "p", "s"]              # r = rocks; p = paper; s = scissors
    strChoice = random.choice(liChoice)     # chooses random letter from list
    if strChoice == "r":
        print("Computer chose rock.")
    elif strChoice == "p":
        print("Computer chose paper.")
    elif strChoice == "s":
        print("Computer chose scissor.")
    return strChoice                        # returns computer's choice


# the function returns a valid user's input
# if invalid prompts for input again
def userGuess():
    strChoice = ""                          # stores valid user's choice
    while True:
        strUserChoice = input("\nEnter 'r' - rock, 'p' - paper or 's' - scissor: ").strip().lower()
        if(strUserChoice == "r"):           # if user input == r (rock)
            strChoice = "r"                     # stores input
            print("You chose rock.")            # prints user's choice
            break                               # break from loop if valid input is entered
        elif(strUserChoice == "p"):         # if user input == p (paper)
            strChoice = "p"
            print("You chose paper.")
            break                               # break from loop if valid input is entered
        elif(strUserChoice == "s"):         # if user input == s (scissor)
            strChoice = "s"
            print("You chose scissor.")
            break                               # break from loop if valid input is entered
        else:                               # loop continues if invalid input is entered
            print("Invalid input entered. Try again!")
    return strChoice                        # return valid user choice


# the function receives userChoice and compChoice as arguments
# it compares two value
# Returns "tie"/"user"/"computer" according to winner declared
def winner(userChoice, compChoice):
    strOutput = ""                          # stores outcome of round
    if (userChoice == compChoice):          # if user and computer chooses same item
        strOutput = "tie"                       # output stores tie
        print("It's a tie!")                    # output is declared
    elif(userChoice == "r"):                # if user enters r (rock)
        if(compChoice == "p"):                  # if computer chooses p (paper)
            strOutput = "computer"              # computer wins
            print("Computer wins this round!")
        elif(compChoice == "s"):                # if computer chooses s (scissor)
            strOutput = "user"                  # user wins
            print("You win this round!")
    elif(userChoice == "p"):                # if user enters p (paper)
        if(compChoice == "r"):                  # if computer chooses r (rock)
            strOutput = "user"                  # user wins
            print("You win this round!")
        elif(compChoice == "s"):                # if computer chooses s (scissor)
            strOutput = "computer"              # computer wins
            print("Computer wins this round!")
    elif(userChoice == "s"):                # if user enters s (scissor)
        if(compChoice == "p"):                  # if computer chooses p (paper)
            strOutput = "user"                  # user wins
            print("You win this round!")
        elif(compChoice == "r"):                # if computer chooses r (rock)
            strOutput = "computer"              # computer wins
            print("Computer wins this round!")
    return strOutput                        # returns output of round


# Main part of program begins
# The following are welcome message and rules displayed
print("*" * 122)
print("*"*30, "Welcome to game of Rock Paper Scissors!".center(60), "*"*30)
print("")
strRules = f"""
Rules of game are:
1. User have to choose among rock, paper, or scissor.
2. User must to enter 'r', 's', or 'p'.
3. User choice would be compared to computer's to declare a winner
4. User or computer have to win 2 rounds to be considered winner
5. In case of a draw, user gets an extra chance.
"""
print(strRules)
print("-"*122)

intNumRounds = 2

# the loop runs till user chooses to exit the game
while True:
    print("\nGame starts...")

    intUserRound = 0                                  # stores number of rounds user wins
    intCompRound = 0                                  # stores number of round computer wins

    # loop runs till either user or computer wins
    while (intUserRound < intNumRounds and intCompRound < intNumRounds):
        userChoice = userGuess()                      # calls userGuess() and stores user's input
        compChoice = compGuess()                      # calls compGuess() and stores comp's choice
        gameOutput = winner(userChoice, compChoice)   # calls winner() and stores output of round
        if(gameOutput == "user"):                     # if outcome of round = "user"
            intUserRound += 1                             # number of rounds user wins increase by 1
        elif(gameOutput == "computer"):               # if outcome of round = "user"
            intCompRound += 1                             # number of rounds computer wins increase by 1
        elif(gameOutput == "tie"):                    # if outcome of round = "user"
            print("You get one extra chance!")            # prints 'Tie' round message

    if(intUserRound == intNumRounds):                 # if number of rounds user wins == 2
        print("\nCongratulations, you won!")              # user wins and scores are displayed
        print(f"Your score: {intUserRound}")
        print(f"Computer score: {intCompRound}")
    elif(intCompRound == intNumRounds):               # if number of rounds computer wins == 2
        print("\nSorry, you lose, computer wins!")        # computer wins and scores are displayed
        print(f"Your score: {intUserRound}")
        print(f"Computer score: {intCompRound}")

    # The set of statements asks user if they want to play again
    # if user enter 'y - yes' the loop continues; games continues
    # if user enters any other input, the loop break
    # and program ends
    print("")
    print("*"*60)
    replay = input("Do you want to play again? (y/n): ").strip().lower()
    if(replay == "y" or replay == "yes"):
        print("You chose to play again!")
        print("*" * 60)
    else:
        print("You chose to exit the game!")
        print("Thank you for playing!")
        print("*" * 60)
        break
