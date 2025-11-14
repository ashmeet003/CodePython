class bankAccount:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        print("Name:",self.name)
        print("Balance:",self.balance)
    def deposit(self,amount):
        pass
    def withdraw(self,amount):
        pass

class savingsAccount(bankAccount):
    def __init__(self,name):
        super().__init__(name)
        self.strType = "Savings"
    def __str__(self):
        print("Name:",self.name, "type:",self.strType)

class checkingAccount(bankAccount):
    def __init__(self,name):
        super().__init__(name)
        self.strType = "Checking"
        self.intCheckNum = 1000
    def __str__(self):
        print("Name:",self.name, "type:",self.strType)
    def writeCheck(self):
        strAmount = input("Enter the amount you want to check: ")
        floatAmount = float(strAmount)
        if floatAmount <= self.flBal:
            self.flBal -= floatAmount
            self.intCheckNum += 1
