# Aahmeet Kaur
# CompB10 Fall2025
# ATM using Classes

class bankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account name: \"{self.name}\"".ljust(40,".") + f"balance: ${self.balance}".rjust(25,".")

    def deposit(self):
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

    def withdraw(self):
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
        return f"Account name: \"{self.name}\"".ljust(40,".") + f"Type: \"{self.strType}\"".ljust(15,".") + f"balance: ${self.balance}".rjust(40,".")

class checkingAccount(bankAccount):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        self.strType = "Checking"
        self.checkNum = 1
        print("You opened a checking account!")

    def __str__(self):
        return f"Account name: \"{self.name}\"".ljust(40, ".") + f"Type: \"{self.strType}\"".ljust(15,".") + f"balance: ${self.balance}".rjust(40, ".")

    def writeCheck(self):
        while (True):  # works till valid withdraw amount is entered
            # asks user to input amount to withdraw and converted into float
            strTemp = input("Enter the amount you want to write check for: $")  # amount to be withdrawn is asked
            flAmount = strTemp.replace(".", "", 1)  # checks value through LBYL
            if (flAmount.isnumeric()):
                flAmount = float(flAmount)  # if account is present
                if (self.balance >= flAmount):  # if available balance > amount to be withdrawn
                    self.balance -= flAmount  # amount withdrawn successfully
                    print(f"You wrote check#{self.checkNum} successfully from \"{self.name}\".")
                    self.checkNum += 1
                else:  # else shows, not enough balance in account chosen
                    print("Check Bounced! Not have enough balance to withdraw!")
                break
            else:
                print("Enter a valid withdrawal amount!\n")

def checkName(name, type, listObj):
    for account in listObj:
        if account.name == name and account.strType == type:
            print(f"{account.strType} account with name \"{accountName}\" already exists.\n")
            return False
    return True

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
    4. Write a check
    5. Display accounts
    6. Exit""")

    option = input("Enter your option: ").strip()
    print("")
    if option == "1":
        while True:
            accountName = input("Enter name for you account: ").strip()
            if len(accountName) > 0:
                print("""Account types available:\n    1. Savings\n    2. Checking""")
                while True:
                    accountType = input("Enter the option number for the account type you need: ").strip().title()
                    if accountType == "1" or accountType == "Savings":
                        if checkName(accountName, "Savings", liAccounts):
                            liAccounts.append(savingsAccount(accountName,0))
                        break
                    elif accountType == "2" or accountType == "Checking":
                        if checkName(accountName, "Checking", liAccounts):
                            liAccounts.append(checkingAccount(accountName,0))
                        break
                    else:
                        print("Invalid Value! Enter 1 for Savings, 2 for Checking.\n")
                break
            else:
                print("You need to enter least one character to name your account!\n")

    elif option == "2":
        if not liAccounts:
            print("You need to open an account first!")
        else:
            while True:
                print("Your open account(s):")
                intIndex = 1
                for account in liAccounts:
                    print(f"{intIndex}. {account}")
                    intIndex += 1
                strIndex = input("\nEnter index of account you want to deposit money into: ").strip()
                if strIndex.isnumeric():
                    intIndex = int(strIndex) - 1
                    if intIndex >= 0 and intIndex < len(liAccounts):
                        liAccounts[intIndex].deposit()
                        break
                    else:
                        print(f"Invalid index! Enter a index number from options given.\n")
                else:
                    print("Enter a valid index number!\n")

    elif option == "3":
        if not liAccounts:
            print("You need to open an account first!")
        else:
            while True:
                print("Your open account(s):")
                intIndex = 1
                for account in liAccounts:
                    print(f"{intIndex}. {account}")
                    intIndex += 1
                strIndex = input("\nEnter index of account you want to withdraw amount from: ").strip()
                if strIndex.isnumeric():
                    intIndex = int(strIndex) - 1
                    if intIndex >= 0 and intIndex < len(liAccounts):
                        liAccounts[intIndex].withdraw()
                        break
                    else:
                        print(f"Invalid index! Enter a index number from options given.\n")
                else:
                    print("Enter a valid index number!\n")

    elif option == "4": # write a check
        if not liAccounts:
            print("You need to open a checking account first!")
        else:
            while True:
                print("Your open checking account(s):")
                checkingAccountNum = 0
                for account in liAccounts:
                    if account.strType == "Checking":
                        checkingAccountNum += 1
                        print(f"{checkingAccountNum}. {account}")
                if checkingAccountNum == 0:
                    print("You need to open a checking account first!")
                    break
                strOption = input("\nEnter index of account you want to write check from: ").strip()
                if strOption.isnumeric():
                    intOption = int(strOption)
                    if intOption >= 1 and intOption <= checkingAccountNum:
                        #liAccounts[intIndex].withdraw()
                        matchCheckingIndex = 0
                        indexInList = -1
                        for account in liAccounts:
                            indexInList += 1
                            if account.strType == "Checking":
                                matchCheckingIndex += 1
                                if matchCheckingIndex == intOption:
                                    liAccounts[indexInList].writeCheck()
                                    break
                        break
                    else:
                        print(f"Invalid index! Enter a index number from options given.\n")
                else:
                    print("Enter a valid index number!\n")

    elif option == "5":
        if not liAccounts:
            print("You have zero accounts open.")
        else:
            print("Your open account(s):")
            index = 1
            for account in liAccounts:
                print(f"{index}. {account}")
                index += 1


    elif option == "6":
        print("******************* Thank you for using the Bank!! *******************")
        break

    else:
        print("Enter a valid option!\n")