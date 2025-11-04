class clCar:
    intWheels = 4
    boolRunning = False
    intMileage = 0

    def __init__(self, strMake = "Toyota", strColor = "White"): # method above any other method, creates new properties
        self.strMake = strMake
        self.strColor = strColor

    def startCar(self): # this methods belongs to self object
        print("This car has started")
        self.boolRunning = True

    def driveCar(self, intNewMiles):
        if(self.boolRunning):
            self.intMileage += intNewMiles
            print(f"You drove car for {intNewMiles} miles. New mileage is: {self.intMileage}")
        else:
            print("The car needs to be started first")


myCar1 = clCar("Toyota Corolla", "Black")
myCar2 = clCar("Ford", "Green")
myCar3 = clCar()

print(myCar1.intWheels) #same
print(myCar2.intWheels) # same
myCar1.intWheels = 6
print(myCar1.intWheels) # different
print(myCar2.intWheels) # same

myCar1.startCar()
myCar1.driveCar(50)
myCar2.driveCar(50)
myCar1.driveCar(50)

print(f"The {myCar1.strMake} is {myCar1.strColor}")
print(f"The {myCar3.strMake} is {myCar3.strColor}")