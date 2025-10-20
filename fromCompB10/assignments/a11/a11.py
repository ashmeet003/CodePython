import rockPaperScissor as rps

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
        userChoice = rps.userGuess()                      # calls userGuess() and stores user's input
        compChoice = rps.compGuess()                      # calls compGuess() and stores comp's choice
        gameOutput = rps.winner(userChoice, compChoice)   # calls winner() and stores output of round
        if(gameOutput == "user"):                     # if outcome of round = "user"
            intUserRound += 1                             # number of rounds user wins increase by 1
        elif(gameOutput == "computer"):               # if outcome of round = "user"
            intCompRound += 1                             # number of rounds computer wins increase by 1
        elif(gameOutput == "tie"):                    # if outcome of round = "user"
            print("You get one extra chance!")            # prints 'Tie' round message


    rps.finalWinner(intUserRound, intCompRound, intNumRounds) # prints final winner based on all rounds


    # The set of statements asks user if they want to play again
    # if user enter 'y - yes', function returns True; the loop continues; games continues
    # if user enter 'n - no', function returns False; the loop breaks
    # and program ends
    if not rps.gameReplay(): # if user chooses to end gameplay, loop breaks; program ends
        break

