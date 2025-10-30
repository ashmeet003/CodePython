# Ashmeet Kaur
# CompB10 Fall 2025
# ATM Machine
# works on dictionary model which allows to add a new account if needed
# this programs intends on saving data using pickle module

import os, pickle

def saveData(diAccounts):                    # saves data in text file using pickle
    with open("balance.txt", "wb") as file:
        pickle.dump(diAccounts, file)
        file.close()
        print("Data Saved")

def currentBalnce(diAccounts):                # prints currentBalance when prompted
    print("Your current balance is:")
    for key, value in diAccounts.items():
        print(key.ljust(12) + ": $" + f"{value:.2f}".rjust(12))

diAccounts = {}                               # dictionary to store account and balances
if os.path.exists("balance.txt"):             # if account file already exists
    with open("balance.txt", "rb") as f:      # file is opened and loaded
        diAccounts = pickle.load(f)
        print("Data loaded")
        f.close()
        currentBalnce(diAccounts)             # current accounts and balance is shown
else:                                         # else new account and file is created
    diAccounts = {"Savings": 0.00, "Checking": 0.00}
    saveData(diAccounts)
    currentBalnce(diAccounts)

# Welcome UI Message
print("#"*80)
print("Welcome to the ATM")
print("#"*80)
print("")

# create a loop for the program
while (True): # works is user chooses another transaction- to continue program

    #Show the menu options
    print("Choose an option: 1 - Deposit, 2 - Withdrawal, 3 - Check Balance, 4 - Open new account")
    # Ask the user for their choice
    strMenu = input("Your choice: ").strip().lower()

    # works to deposit money
    if (strMenu == "1" or strMenu == "deposit"):
        print("You want to make a deposit.\n")
        # asks user to input amount to deposit and converted into float
        while (True):                                                                   # loops till valid amount is entered
            strTemp = input("Enter the amount you want to deposit: $")                  # user enters amount to be deposited
            flAmount = strTemp.replace(".","",1)                    # Validates value using LBYL
            if (flAmount.isnumeric()):
                flAmount = float(flAmount)
                while (True):                                                           # loops till valid account name is entered
                    print("\nChoose an account to deposit your money:")                  # prompted to choose account from available accounts
                    for key in diAccounts:                                              # displays account names (keys)
                        print(f"- {key}")
                    strChoice = input("Enter your option: ").strip().title()            # user enters account name
                    if strChoice in diAccounts:                                         # if account name entered matches actual account name
                        diAccounts[strChoice] += flAmount                                   # amount deposits, data updated
                        print("Amount deposited successfully!")
                        break
                    else:                                                               # if enters wrong number for account selection
                        print("Please enter a valid account name")
                break
            else:
                print("Enter a valid deposit amount!\n")
        saveData(diAccounts)            # saves data in file
        currentBalnce(diAccounts)       # displays current balance



    elif (strMenu == "2" or strMenu == "withdrawal"):                                   # works for withdrawal
        print("You want to make a withdrawal.\n")
        while (True):                                                                   # works till valid withdraw amount is entered
            # asks user to input amount to withdraw and converted into float
            strTemp = input("Enter the amount you want to withdraw: $")                 # amount to be withdrawn is asked
            flAmount = strTemp.replace(".","",1)                    # checks value through LBYL
            if (flAmount.isnumeric()):
                flAmount = float(flAmount)
                while (True):                                                           # works till valid account name is entered
                    print("\nChoose an account to withdraw your money:")
                    for key in diAccounts:                                              # list of accounts available is displayed
                        print(f"-: {key}")
                    strChoice = input("Enter your option: ").strip().title()            # user enters account name
                    if(strChoice in diAccounts):                                        # if account is present
                        if(diAccounts[strChoice] > flAmount):                               # if available balance > amount to be withdrawn
                            diAccounts[strChoice] -= flAmount                               # amount withdrawn successfully
                            print("Amount withdrawn successfully!")
                        else:                                                               # else shows, not enough balance in account chosen
                            print("You do not have enough balance to withdraw!")
                        break
                    else:                                                               # else entered invalid account name
                        print("You entered invalid account.")
                break
            else:
                print("Enter a valid withdrawal amount!\n")
        saveData(diAccounts)  # saves data in file
        currentBalnce(diAccounts)  # displays current balance


    elif (strMenu == "3" or strMenu == "check balance"):                  # Shows account Balance
        print("You want to check a balance.\n")
        currentBalnce(diAccounts)  # displays current balance


    elif(strMenu == "4" or strMenu == "open new account"):                  # to open a new account, add new key to dictionary
        # validates if user wants to open new account - double verification
        while (True):                     # works till user enters y or n
            openAccount = input("You wish to open new account. yes - y or no -n?:").strip().lower()
            if (openAccount == "y" or openAccount == "yes"):                    # if user chooses to open an account
                accountName = input("Enter the account name: ").strip().title() # user enters customized account name
                diAccounts[accountName] = 0.0                                   # by default account is set to $0 balance
                print("Account opened successfully!")
                break
            elif (openAccount == "n" or openAccount == "no"):                   # if user chooses no, prints message - breaks
                print("You chose not to open a new account.")
                break
            else:
                print("Enter valid answer please! y/n ?\n")

        saveData(diAccounts)  # saves data in file
        currentBalnce(diAccounts)  # displays current balance


    else:                                  # if user enters invalid value from initial options
        print ("Sorry - that's not a valid choice")

    print("")
    strMore = ""
    while (True):   # works to validate answer for another transaction y/n ?
        strMore = input("Would you like another transaction? enter y or n: ").strip().lower()  # prompts for another transaction option
        if(strMore == "y" or strMore == "yes" or strMore == "n" or strMore == "no"):
            break
        else:
            print("Enter a valid answer please! y/n ?\n")

    if (strMore == "n" or strMore == "no"):                                 # if user chooses not to do another transaction
        break                                                               # break from loop, exit

    print("")


# exit message
print("#"*80)
print("Thank you for using ATM")
print("#"*80)