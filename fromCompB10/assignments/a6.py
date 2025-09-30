# Ashmeet Kaur
# CompB10 Fall 2025
# ATM Machine
##############
# add decimal verification if possible
##############

# start with some $$
flSavBal = 500.99
flChkBal = 100.31
diAccounts = {"Savings": 500.99, "Checking": 100.31}

# Welcome UI Message
print("#"*80)
print("Welcome to the ATM")
print("#"*80)
print("")

# create a loop for the program
while (True):

    #Show the menu options
    print("Choose an option: 1 - Deposit, 2 - Withdrawal, 3 - Check Balance, 4 - Open new account")
    # Ask the user for their choice
    strMenu = input("Your choice: ").strip().lower()

    # works to deposit money
    if (strMenu == "1" or strMenu == "deposit"):
        print("You want to make a deposit.\n")

        # asks user to input amount to deposit and converted into float
        flAmount = float(input("Enter the amount you want to deposit: $"))
        print("Choose an account to deposit your money:")
        intCount = 1
        for key in diAccounts:
            print(f"{intCount}: {key}")
            intCount += 1
        strChoice = input("Enter your option: ").strip().title()

        if strChoice in diAccounts:
            diAccounts[strChoice] += flAmount
            print("Amount deposited successfully!")
        else:                           # if enters wrong number for account selection
            print("You entered Invalid account!")

        print("Your balance is:")       # shows balance at the end
        for key, value in diAccounts.items():
            print(key.ljust(12) + ": $" + f"{value:.2f}".rjust(12))




    elif (strMenu == "2" or strMenu == "withdrawal"):
        print("You want to make a withdrawal.\n")

        # asks user to input amount to withdraw and converted into float
        flAmount = float(input("Enter the amount you want to deposit: $"))
        print("Choose an account to deposit your money:")
        intCount = 1
        for key in diAccounts:
            print(f"{intCount}: {key}")
            intCount += 1
        strChoice = input("Enter your option: ").strip().title()

        if(strChoice in diAccounts):
            if(diAccounts[strChoice] > flAmount):
                diAccounts[strChoice] -= flAmount
                print("Amount withdrawn successfully!")
            else:
                print("You do not have enough balance to withdraw!")
        else:
            print("You entered invalid account.")


        print("Your balance is:")       # shows balance at the end
        for key, value in diAccounts.items():
            print(key.ljust(12) + ": $" + f"{value:.2f}".rjust(12))




    elif (strMenu == "3" or strMenu == "check balance"):                  # Shows account Balance
        print("You want to check a balance.\n")
        print("Your balance is:")       # shows balance at the end1
        for key, value in diAccounts.items():
            print(key.ljust(12) + ": $" + f"{value:.2f}".rjust(12))


    elif(strMenu == "4" or strMenu == "open new account"):
        openAccount = input("You wish to open new account. yes - y or no -n?:").strip().lower()
        if (openAccount == "y" or openAccount == "yes"):
            accountName = input("Enter the account name: ").strip().title()
            diAccounts[accountName] = 0.0
            print("Account opened successfully!")

        print("Your balance is:")       # shows balance at the end1
        for key, value in diAccounts.items():
            #print(key.ljust(12) + ": $" + str(value).rjust(12))
            print(key.ljust(12) + ": $" + f"{value:.2f}".rjust(12))


    else:
        print ("Sorry - that's not a valid choice")

    print("")
    strMore = input("Would you like another transaction? enter y or n: ")

    if (strMore != "y"):            # if user chooses not to do another transaction
        break

    print("")