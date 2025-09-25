# number guessing game
import random

intMaxTries = 3
intMaxRange = 10
intTotalGamesPlayed = 0
intTotalGamesWon = 0

while True:
    intCurrentTry = 1
    intSecret = random.randint(1, intMaxRange)
    intTotalGamesPlayed += 1

    while(intCurrentTry <= intMaxTries):
        intUserGuess = int(input(f"Guess a number between 1 and {intMaxRange}: "))

        if(intUserGuess == intSecret):
            print("You guessed correctly")
            intTotalGamesWon += 1
            break
        elif(intUserGuess < intSecret):
            print("You guessed too low")
        else:
            print("You guessed too high")

        intCurrentTry += 1

    strAgain = input("Would you like to play again? (y/n): ").strip().lower()
    if(strAgain == "n"):
        break

print("")
intGamesLost = intTotalGamesPlayed - intTotalGamesWon
strResult = f"""Total games played: {intTotalGamesPlayed}
Total games won: {intTotalGamesWon}
Total Games Lost: {intGamesLost}"""
print(strResult)
print("Thank you for playing!")