class clFruit:
    def __init__(self,strN,intQ,flP):
        self.strName = strN
        self.intQuant = intQ
        self.flPrice = flP
        print(f"You added {intQ} {strN}.")

    def __str__(self):
        return f"{self.strName} {self.intQuant}".ljust(20,".")+ f"{self.flPrice:.2f}".rjust(20,".")

    def setQuant(self,intQ):
        if(isinstance(intQ,int)):
            self.intQuant = intQ
        else:
            print("Not a valid Quantity.")

    def getQuant(self):
        return self.intQuant

liFruit = []

print("""
********************
Fruit Stand
********************
""")

while True:
    print("""
    Menu:
    1. Add Fruit
    2. Remove Fruit
    3. Update Quantity
    4. List Fruit
    5. Exit
    """)
    strMenu = input("Enter your choice: ")
    if strMenu == "1":
        print("Add a fruit-\n")
        strName = input("Enter fruit name: ")
        intQuant = int(input("Enter fruit quantity: "))
        flPrice = float(input("Enter fruit price: "))
        liFruit.append(clFruit(strName,intQuant,flPrice))
        print("Fruit added successfully.")

    elif strMenu == "2":
        print("Remove a fruit-")
        intIndex = 0
        for obFruit in liFruit:
            print(intIndex, obFruit)
            intIndex = intIndex + 1
        intPick = int(input("Enter number of fruit to remove: "))
        obTemp = liFruit.pop(intPick)
        print(f"{obTemp.strName} removed successfully.")

    elif strMenu == "3":
        print("Update a fruit Quantity-")
        intIndex = 0
        for obFruit in liFruit:
            print(intIndex, obFruit)
            intIndex = intIndex + 1
        intPick = int(input("Enter number of fruit to update Quantity: "))
        intNQ= int(input("Enter new fruit quantity: "))
        liFruit[intPick].setQuant(intNQ)
        print(f"{liFruit[intPick].strName} quantity changed to {liFruit[intPick].getQuant()} successfully.")

    elif strMenu == "4":
        print("Here is your fruit inventory-")
        for objFruit in liFruit:
            print(objFruit)

    elif strMenu == "5":
        break

    else:
        print("Not a valid Menu choice.")