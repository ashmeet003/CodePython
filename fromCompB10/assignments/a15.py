# Aahmeet Kaur
# CompB10 Fall2025
# ATM using Classes

class bankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account name: {self.name}".ljust(40,".") + f"balance: ${self.balance}".rjust(25,".")

    def deposit(self,amount):
        self.balance += amount
        while (True):                                                                   # loops till valid amount is entered
            strTemp = input("Enter the amount you want to deposit: $")                  # user enters amount to be deposited
            flAmount = strTemp.replace(".","",1)                    # Validates value using LBYL
            if (flAmount.isnumeric()):
                flAmount = float(flAmount)
                self.balance += flAmount                                   # amount deposits, data updated
                print(f"Amount deposited successfully to \"{self.name}\".")
                break
            else:
                print("Enter a valid deposit amount!\n")

    def withdraw(self,amount):
        while (True):                                                                   # works till valid withdraw amount is entered
            # asks user to input amount to withdraw and converted into float
            strTemp = input("Enter the amount you want to withdraw: $")                 # amount to be withdrawn is asked
            flAmount = strTemp.replace(".","",1)                    # checks value through LBYL
            if (flAmount.isnumeric()):
                flAmount = float(flAmount)                                        # if account is present
                if(self.balance >= flAmount):                               # if available balance > amount to be withdrawn
                    self.balance -= flAmount                               # amount withdrawn successfully
                    print(f"Amount withdrawn successfully from \"{self.name}\".")
                else:                                                               # else shows, not enough balance in account chosen
                    print("You do not have enough balance to withdraw!")
                break
            else:
                print("Enter a valid withdrawal amount!\n")


class savingsAccount(bankAccount):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        self.strType = "Savings"
        print("You opened a savings account!")

    def __str__(self):
        return f"Account name: {self.name}".ljust(40,".") + f"Type: {self.strType}".ljust(15,".") + f"balance: ${self.balance}".rjust(25,".")

class checkingAccount(bankAccount):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        self.strType = "Checking"
        self.checkNum = 1
        print("You opened a checking account!")

    def __str__(self):
        return f"Account name: {self.name}".ljust(40, ".") + f"Type: {self.strType}".ljust(15,".") + f"balance: ${self.balance}".rjust(25, ".")

    def writeCheck(self,amount):
        while (True):  # works till valid withdraw amount is entered
            # asks user to input amount to withdraw and converted into float
            strTemp = input("Enter the amount you want to write check for: $")  # amount to be withdrawn is asked
            flAmount = strTemp.replace(".", "", 1)  # checks value through LBYL
            if (flAmount.isnumeric()):
                flAmount = float(flAmount)  # if account is present
                if (self.balance >= flAmount):  # if available balance > amount to be withdrawn
                    self.balance -= flAmount  # amount withdrawn successfully
                    print(f"You wrote check#{self.checkNum} successfully.")
                    self.checkNum += 1
                else:  # else shows, not enough balance in account chosen
                    print("You do not have enough balance to withdraw!")
                break
            else:
                print("Enter a valid withdrawal amount!\n")


liAccounts = []

print("""
****************************************
            Welcome to Bank            
****************************************""")
while True:
    print("""
    Menu:
    1. Open an account
    2. Deposit a amount
    3. Withdraw a amount
    3. Write a check
    4. Check Balance
    5. Exit""")

    input = input("Enter your option: ").strip().title()
    if input == "1":
        pass

    elif input == "2":
        if not liAccounts:
            print("You need to open an account first!")
        else:
            pass

    elif input == "3":
        if not liAccounts:
            print("You need to open an account first!")
        else:
            pass

    elif input == "4":
        if not liAccounts:
            print("You need to open an account first!")
        else:
            pass

    elif input == "5":
        break

    else:
        print("Enter a valid option!\n")