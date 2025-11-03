import random
class clPet:
    def __init__(self, strName):
        self.strPetName = strName
        self.intHunger = 5
        self.intBoredom = 5

        print(f"You adopted a new pet and named them {self.strPetName}.")

    def __str__(self):
        return f"{obPet.strPetName} (Hunger: {obPet.intHunger}) (Boredom: {obPet.intBoredom})"

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
        strName = input("What is the pet's name? ")
        liPets.append(clPet(strName))
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

    elif (strMenu == "3"):
        print("\nYou chose to play with a pet.\n")
        # use the pet feed from "option 2" above to complete the play section below.

    elif (strMenu == "4"):
        for obPet in liPets:
            print(obPet)
    else:
        print("Not a valid option. Try again.")

    for obPet in liPets:
        if obPet.intBoredom < 1 or obPet.intHunger < 1:
            liPets.remove(obPet)
