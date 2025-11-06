class clCar:
    intWheels = 4
    boolRunning = False
    intMileage = 0
    boolAvailable = True

    def __init__(self, strMake = "Toyota", strColor = "White"): # method above any other method, creates new properties
        self.strMake = strMake
        self.strColor = strColor

    def __str__(self):
        return f"This is a {self.strColor} {self.strMake} car with mileage-{self.intMileage}."

    def startCar(self): # this methods belongs to self object
        print("This car has started")
        self.boolRunning = True

    def driveCar(self, intNewMiles):
        if(self.boolRunning):
            self.intMileage += intNewMiles
            print(f"You drove car for {intNewMiles} miles. New mileage is: {self.intMileage}")
        else:
            print("The car needs to be started first")

    def rentOut(self):
        self.boolAvailable = False

    def setWheels(self, intN):
        if(isinstance(intN, int) and intN > 1):
            self.intWheels = intN
        else:
            print("No")

    def getWheels(self):
        return self.intWheels

liCars = []
liCars.append(clCar("Toyota Corolla", "Black"))
liCars.append(clCar("Ford", "Green"))
liCars.append(clCar())

liCars[1].rentOut()
liCars[1].startCar()
liCars[1].driveCar(100)

for car in liCars:
    if(car.boolAvailable):
        print(car)

# print(myCar1.intWheels) #same
# print(myCar2.intWheels) # same
# myCar1.intWheels = 6
# print(myCar1.intWheels) # different
# print(myCar2.intWheels) # same
#
# myCar1.startCar()
# myCar1.driveCar(50)
# myCar2.driveCar(50)
# myCar1.driveCar(50)
#
# print(f"The {myCar1.strMake} is {myCar1.strColor}")
# print(f"The {myCar3.strMake} is {myCar3.strColor}")
#
# print(myCar3)
# print(myCar2)