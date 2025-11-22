# Ashmeet Kaur
# CompB10 Fall2025
# ATM using Classes
# This program uses classes, inheritance, polymorphism which helps in encapsulation and code module breaking
# It also uses pickle and os to save data and load data as needed
# ideas: add transfer amount () and delete account() --- in future

import pickle, os

# parent class with functions: deposit() and withdraw()
class bankAccount:
    def __init__(self,name,balance):            # primary variables include name and balance, initially stored at $0
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account name: \"{self.name}\"".ljust(40,".") + f"balance: ${self.balance}".rjust(25,".")

    def deposit(self):                          # asks user for deposit amount, validates amount, and update account's balance
        while (True):                                                                   # loops till valid amount is entered
            strTemp = input("Enter the amount you want to deposit: $")                  # user enters amount to be deposited
            flAmount = strTemp.replace(".","",1)                    # Validates value using LBYL
            if (flAmount.isnumeric()):
                flAmount = float(flAmount)
                self.balance += flAmount                                                # amount deposits, data updated
                print(f"Amount deposited successfully to \"{self.name}\".")
                break
            else:
                print("Enter a valid deposit amount!\n")

    def withdraw(self):                         # asks user for amount to withdraw, validates account balance and amount, updates account
        while (True):                                                                   # works till valid withdraw amount is entered
            # asks user to input amount to withdraw and converted into float
            strTemp = input("Enter the amount you want to withdraw: $")                 # amount to be withdrawn is asked
            flAmount = strTemp.replace(".","",1)                    # checks value through LBYL
            if (flAmount.isnumeric()):
                flAmount = float(flAmount)                                              # if account is present
                if(self.balance >= flAmount):                                           # if available balance > amount to be withdrawn
                    self.balance -= flAmount                                            # amount withdrawn successfully
                    print(f"Amount withdrawn successfully from \"{self.name}\".")
                else:                                                                   # else shows, not enough balance in account chosen
                    print("You do not have enough balance to withdraw!")
                break
            else:
                print("Enter a valid withdrawal amount!\n")


# subclass - primary for a savings account, uses parent class's functions as well to deposit and withdraw amount
class savingsAccount(bankAccount):
    def __init__(self,name,balance):            # stores subclass variable strType = "Savings"
        super().__init__(name,balance)
        self.strType = "Savings"                # account type is "Savings"
        print("You opened a savings account!")

    def __str__(self):                          # savings account's object's description
        return f"Account name: \"{self.name}\"".ljust(40,".") + f"Type: \"{self.strType}\"".ljust(35,".") + "Balance: $" + f"{self.balance:.2f}".rjust(20,".")


# subclass - Checking Account - apart from parent class' functions: deposit() and withdraw(), has additional function writeCheck()
class checkingAccount(bankAccount):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        self.strType = "Checking"                                               # stores object type: "Checking"
        self.checkNum = 1                                                       # stores number of checks used till point
        print("You opened a checking account!")

    def __str__(self):                                                          # object's description
        return f"Account name: \"{self.name}\"".ljust(40, ".") + f"Type: \"{self.strType}\"".ljust(35,".") + "Balance: $" + f"{self.balance:.2f}".rjust(20,".")

    def writeCheck(self):
        while (True):                                                           # works till valid withdraw amount is entered
            # asks user to input amount to withdraw and converted into float
            strTemp = input("Enter the amount you want to write check for: $")  # amount to be withdrawn is asked
            flAmount = strTemp.replace(".", "", 1)          # checks value through LBYL
            if (flAmount.isnumeric()):
                flAmount = float(flAmount)                                      # if valid float amount is entered, input converted to float
                if (self.balance >= flAmount):                                  # if available balance > amount to be withdrawn
                    self.balance -= flAmount                                    # amount withdrawn successfully
                    print(f"You wrote check#{self.checkNum} successfully from \"{self.name}\".")
                    self.checkNum += 1                                          # increases the number of checks used by 1
                else:                                                           # else shows, not enough balance in account chosen
                    print("Check Bounced! Not have enough balance to withdraw!")
                break
            else:
                print("Enter a valid withdrawal amount!\n")


# checks if account with same name and account type (Savings/Checking) already exists
# if such an object exists, returns False - flagging not to append the object to list
# if not - returns True - object gets appended to list
def checkName(name, type, listObj):
    for account in listObj:
        if account.name == name and account.strType == type:
            print(f"{account.strType} account with name \"{accountName}\" already exists.\n")
            return False
    return True


# saves data from liAccounts( list of bank account objects) to pickle file
def saveAccount(listObj):
    with open("balance.txt", "wb") as f:
        pickle.dump(listObj, f)
        print("Data Saved...")


# initialises a list to store class objects
# checks if already saved account data exists in pickle file
# if data exists, it gets loaded to list object
liAccounts = []
if os.path.exists("balance.txt"):
    with open("balance.txt", "rb") as f:
        liAccounts = pickle.load(f)
        print("...Data Loaded")

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

    option = input("Enter your option: ").strip()                                       # choose and option from menu
    print("")
    if option == "1":                                                                   # works to open a new account
        print("\nLet's open an account for you!!")
        print("---------------------------------------------------------------------------------------------------------------\n")
        while True:
            accountName = input("Enter name for you account: ").strip()
            if len(accountName) > 0:                                                    # checks for invalid account name is entered(space, enter)
                print("""Account types available:\n    1. Savings\n    2. Checking""")  # prints the type of accounts available to open
                while True:                                                             # works till user enters valid index option for account type
                    accountType = input("Enter the option number for the account type you need: ").strip().title()
                    if accountType == "1" or accountType == "Savings":                  # for savings account
                        if checkName(accountName, "Savings", liAccounts):          # checks for existence of similar object
                            liAccounts.append(savingsAccount(accountName,0))    # if everything is correct, gets appended to list
                        break                                                           # breaks from inner while loop(to check valid account type)
                    elif accountType == "2" or accountType == "Checking":               # for checking account
                        if checkName(accountName, "Checking", liAccounts):         # checks for existence of similar object
                            liAccounts.append(checkingAccount(accountName,0))   # if everything is correct, gets appended to list
                        break                                                           # breaks from inner while loop(to check valid account type)
                    else:                                                               # else loop continues till a valid account type option is entered
                        print("Invalid Value! Enter 1 for Savings, 2 for Checking.\n")
                break                                                                   # breaks from outer while loop(if all options entered were correct or similar object exists)
            else:                                                                       # loop continues till a valid name is entered (for a space or enter)
                print("You need to enter least one character to name your account!\n")
        saveAccount(liAccounts)                                                         # updated list is saved to pickle

    elif option == "2":                                                                 # to deposit amount to an open account
        print("\nLet the bank help to deposit your amount!!")
        print("---------------------------------------------------------------------------------------------------------------\n")
        if not liAccounts:                                                              # prints message if no account exists yet
            print("You need to open an account first!")
        else:                                                                           # if account exists
            while True:                                                                 # works till a valid index option is entered for accounts available
                print("Your open account(s):")
                intIndex = 1                                                            # works as index number of an account while printing
                for account in liAccounts:                                              # shows account's description through __str__
                    print(f"{intIndex}. {account}")
                    intIndex += 1                                                       # to-be-printed index increases by 1
                strIndex = input("\nEnter index of account you want to deposit money into: ").strip()
                if strIndex.isnumeric():                                                # if entered index from list is a number
                    intIndex = int(strIndex) - 1                                        # input converted to integer -1 (valid for index of a list from 0)
                    if intIndex >= 0 and intIndex < len(liAccounts):                    # checks if entered input is valid and within range of len(list)
                        liAccounts[intIndex].deposit()                                  # if right account is chosen - its related deposit() is called
                        break                                                           # breaks from while loop - everything went correct
                    else:                                                               # if out-of-range index is entered
                        print(f"Invalid index! Enter a index number from options given.\n")
                else:                                                                   # if a not-a-integer value is entered
                    print("Enter a valid index number!\n")
        saveAccount(liAccounts)                                                         # updated list object is saved to pickle

    elif option == "3":                                                                 # works to withdraw amount from a object's balance
        print("\nYou wish to withdraw an amount?! Lets do it!")
        print("---------------------------------------------------------------------------------------------------------------\n")
        if not liAccounts:                                                              # prints message if no account exists yet
            print("You need to open an account first!")
        else:                                                                           # if account exists
            while True:                                                                 # works till a valid index option is entered for accounts available
                print("Your open account(s):")
                intIndex = 1                                                            # works as index number of an account while printing
                for account in liAccounts:
                    print(f"{intIndex}. {account}")                                     # shows account's description through __str__
                    intIndex += 1                                                       # to-be-printed index increases by 1
                strIndex = input("\nEnter index of account you want to withdraw amount from: ").strip()
                if strIndex.isnumeric():                                                # if entered index from list is a number
                    intIndex = int(strIndex) - 1                                        # input converted to integer -1 (valid for index of a list from 0)
                    if intIndex >= 0 and intIndex < len(liAccounts):                    # checks if entered input is valid and within range of len(list)
                        liAccounts[intIndex].withdraw()                                 # if right account is chosen - its related withdraw() is called
                        break                                                           # breaks from while loop - everything went correct
                    else:                                                               # if out-of-range index is entered
                        print(f"Invalid index! Enter a index number from options given.\n")
                else:                                                                   # if a not-a-integer value is entered
                    print("Enter a valid index number!\n")
        saveAccount(liAccounts)                                                         # updated list object is saved to pickle

    elif option == "4":                                                                 # write a check
        print("\nNeed to write a check? Lets do it!")
        print("---------------------------------------------------------------------------------------------------------------\n")
        if not liAccounts:                                                              # prints message if no account exists yet
            print("You need to open a checking account first!")
        else:
            while True:                                                                 # if account exists
                print("Your open checking account(s):")
                checkingAccountNum = 0                                                  # works for index of accounts available while printing
                for account in liAccounts:
                    if account.strType == "Checking":                                   # shows only accounts with type-checking(this func is to write a check)
                        checkingAccountNum += 1                                         # increases index-to-be printed by 1
                        print(f"{checkingAccountNum}. {account}")                       # shows account's description through class checkingAccount: __str__
                if checkingAccountNum == 0:                                             # if no checking account is found, prints message, and breaks from loop - back to main menu
                    print("You need to open a checking account first!")
                    break
                strOption = input("\nEnter index of account you want to write check from: ").strip()    # if checking account exists, asks for index of account from  checking account' list printed
                if strOption.isnumeric():                                               # if a number was entered
                    intOption = int(strOption)                                          # input to integer
                    if intOption >= 1 and intOption <= checkingAccountNum:              # checks is input entered is from the range of index printed in checking account's list printed
                        matchCheckingIndex = 0                                          # index to match the input entered
                        indexInList = -1                                                # this is to find index of account chosen by user in actual list
                        for account in liAccounts:                                      # loop starts
                            indexInList += 1                                            # first object-> object = 0 and increases everytime
                            if account.strType == "Checking":                           # checks for checking account as in original loop
                                matchCheckingIndex += 1                                 # similar to checkingAccountNum index
                                if matchCheckingIndex == intOption:                     # we need the input entered to match the matchCheckingIndex(basically checking which account user chose)
                                    liAccounts[indexInList].writeCheck()                # Now this is the object we need with original index from list as indexInList - calls for writeCheck()
                                    break                                               # breaks from for loop
                        break                                                           # breaks from while loop (if valid index was entered as input from shown options)
                    else:                                                               # if invalid number - different from index shown entered
                        print(f"Invalid index! Enter a index number from options given.\n")
                else:                                                                   # if invalid value other than number is entered
                    print("Enter a valid index number!\n")
        saveAccount(liAccounts)                                                         # list data saved to pickle

    elif option == "5":                                                                 # shows all account's balance
        print("\nAccount Balance:")
        print("---------------------------------------------------------------------------------------------------------------\n")
        if not liAccounts:                                                              # if zero accounts opened, shows appropriate message
            print("You have zero accounts open.")
        else:
            print("Your open account(s):")
            index = 1
            for account in liAccounts:
                print(f"{index}. {account}")
                index += 1


    elif option == "6":                                                                 # shows thank you message and exits the program
        print("\n---------------------------------------------------------------------------------------------------------------\n")
        print("                    ******************* Thank you for using the Bank!! *******************")
        print("---------------------------------------------------------------------------------------------------------------\n")
        break

    else:                                                                               # if invalid option from main menu is entered
        print("Enter a valid option!\n")