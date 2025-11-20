# Ashmeet Kaur
# CompB10 Fall 2025
# example of class inheritance and polymorphism
import random
class clPet:
    def __init__(self, strName):
        self.strPetName = strName
        self.intHunger = 5
        self.intBoredom = 5

    def takeTurn(self):
        print("\n -- TIME PASSES --\n")
        self.intHunger -= random.randint(0,3)
        self.intBoredom -= random.randint(0,3)
        if (self.intHunger < 4 and self.intHunger > 0):
            print(f"{self.strPetName} is Hungry!")
        elif (self.intHunger < 1):
            print(f"{self.strPetName} has found an owner that will feed them!")
        if (self.intBoredom < 4 and self.intBoredom > 0):
            print(f"{self.strPetName} is so BORED!")
        elif (self.intBoredom < 1):
            print(f"{self.strPetName} has run away to find some fun.")
        print("\n\n")

    def feedPet(self):
        self.intHunger += 5
        print(f"You fed {self.strPetName}.")

    def playPet(self):
        self.intBoredom += 5
        print(f"You played with {self.strPetName}.")

class clPetFish(clPet):
    def __init__(self, strName):
        super().__init__(strName)
        self.type = "Fish"

    def __str__(self):
        return f"{obPet.strPetName} - {self.type} - (Hunger: {obPet.intHunger}) (Boredom: {obPet.intBoredom})"

    def playPet(self):
        self.intBoredom += 5
        print(f"You splashed around with {self.strPetName}.")


class clPetDog(clPet):
    def __init__(self, strName):
        super().__init__(strName)
        self.type = "Dog"

    def __str__(self):
        return f"{obPet.strPetName} - {self.type} - (Hunger: {obPet.intHunger}) (Boredom: {obPet.intBoredom})"

    def playPet(self):
        self.intBoredom += 5
        print(f"You played fetch with {self.strPetName}.")


class clPetCat(clPet):
    def __init__(self, strName):
        super().__init__(strName)
        self.type = "Cat"

    def __str__(self):
        return f"{obPet.strPetName} - {self.type} - (Hunger: {obPet.intHunger}) (Boredom: {obPet.intBoredom})"

    def playPet(self):
        self.intBoredom += 5
        print(f"You played fetch with {self.strPetName}.")


def welcomeUser ():
    print("Welcome to the pet store.")

liPets = []
welcomeUser()
while True:
    print("Here are the options:")
    print("-"*20)
    print("1. Adopt a pet.")
    print("2. Feed a pet.")
    print("3. Play with a pet.")
    print("4. Check on pets.")

    strMenu = input("What would you like to do? ")
    if (strMenu == "1"):
        print("\nWe have the following  animals:")
        print("1. Fish")
        print("2. Dogs")
        print("3. Cats")
        strType = input("What do you want to adopt?")
        strName = input("What is the pet's name? ")
        if (strType == "1"):
            # Fish
            liPets.append(clPetFish(strName))
        elif (strType == "2"):
            # Dog
            liPets.append(clPetDog(strName))
        elif (strType == "3"):
            #Cat
            liPets.append(clPetCat(strName))
        else:
            print("We don't have any of those.")

        # We moved the takeTurn( ) here so you can
        # check on pets without taking a turn.
        for obPet in liPets:
            obPet.takeTurn()

    elif (strMenu == "2"):
        # This code is to feed the pet
        print("\nYou chose to feed a pet.\n")
        # First, we need to set up an integer variable
        # to allow users to choose a pet easily
        intNumber = 1
        # Iterate through the list of pets
        for obPet in liPets:
            # Print the index, and then the pet info
            print(intNumber, obPet)
            # Add one to the index so the next
            # pet will get their own number.
            intNumber += 1
        # Ask the user to enter the number of the pet they want to feed.
        # We subtract 1 from the number they enter to change it to
        # the correct index for that pet.
        intIndex = int(input("Enter the number of the pet you want to feed: "))-1
        # Use the index to call the feedPet method of the right pet from the list.
        liPets[intIndex].feedPet()

        # We moved the takeTurn( ) here so you can
        # check on pets without taking a turn.
        for obPet in liPets:
            obPet.takeTurn()

    elif (strMenu == "3"):
        print("\nYou chose to play with a pet.\n")
        # use the pet feed from "option 2" above to complete the play section below.
        intNumber = 1
        for obPet in liPets:
            print(intNumber, obPet)
            intNumber += 1
        intIndex = int(input("Enter the number of the pet you want to play: "))-1
        liPets[intIndex].playPet()



        # We moved the takeTurn( ) here so you can
        # check on pets without taking a turn.
        for obPet in liPets:
            obPet.takeTurn()

    elif (strMenu == "4"):
        print("\nYou check in on your pets:")
        for obPet in liPets:
            print(obPet)
    else:
        print("Not a valid option. Try again.")

    for obPet in liPets:
        if obPet.intBoredom < 1 or obPet.intHunger < 1:
            liPets.remove(obPet)


