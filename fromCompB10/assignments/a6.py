# Ashmeet Kaur
# CompB10 Fall 2025
# ATM Machine
# works on dictionary model which allows to add a new account if needed

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
        flAmount = float(input("Enter the amount you want to deposit: $"))  # user enters amount to be deposited
        print("Choose an account to deposit your money:")                   # prompted to choose account from available accounts
        intCount = 1                                                        # just a counter for display number
        for key in diAccounts:                                              # displays account names (keys)
            print(f"{intCount}: {key}")
            intCount += 1
        strChoice = input("Enter your option: ").strip().title()            # user enters account name

        if strChoice in diAccounts:                                         # if account name entered matches actual account name
            diAccounts[strChoice] += flAmount                                   # amount deposits, data updated
            print("Amount deposited successfully!")
        else:                                                               # if enters wrong number for account selection
            print("You entered Invalid account!")

        print("Your balance is:")                                           # shows balance at the end
        for key, value in diAccounts.items():
            print(key.ljust(12) + ": $" + f"{value:.2f}".rjust(12))         # formatted to 2 decimal, just in case



    elif (strMenu == "2" or strMenu == "withdrawal"):                       # works for withdrawal
        print("You want to make a withdrawal.\n")
        # asks user to input amount to withdraw and converted into float
        flAmount = float(input("Enter the amount you want to withdraw: $"))  # amount to be withdrawn is asked
        print("Choose an account to withdraw your money:")
        intCount = 1
        for key in diAccounts:                                              # list of accounts available is displayed
            print(f"{intCount}: {key}")
            intCount += 1
        strChoice = input("Enter your option: ").strip().title()            # user enters account name

        if(strChoice in diAccounts):                                        # if account is present
            if(diAccounts[strChoice] > flAmount):                               # if available balance > amount to be withdrawn
                diAccounts[strChoice] -= flAmount                               # amount withdrawn successfully
                print("Amount withdrawn successfully!")
            else:                                                               # else shows, not enough balance in account chosen
                print("You do not have enough balance to withdraw!")
        else:                                                               # else entered invalid account name
            print("You entered invalid account.")

        print("Your balance is:")                                           # shows balance at the end
        for key, value in diAccounts.items():
            print(key.ljust(12) + ": $" + f"{value:.2f}".rjust(12))


    elif (strMenu == "3" or strMenu == "check balance"):                  # Shows account Balance
        print("You want to check a balance.\n")
        print("Your balance is:")       # shows balance at the end1
        for key, value in diAccounts.items():
            print(key.ljust(12) + ": $" + f"{value:.2f}".rjust(12))


    elif(strMenu == "4" or strMenu == "open new account"):                  # to open a new account, add new key to dictionary
        # confirms if user wants to open new account
        openAccount = input("You wish to open new account. yes - y or no -n?:").strip().lower()
        if (openAccount == "y" or openAccount == "yes"):                    # if user chooses to open an account
            accountName = input("Enter the account name: ").strip().title() # user enters customized account name
            diAccounts[accountName] = 0.0                                   # by default account is set to $0 balance
            print("Account opened successfully!")

        print("Your balance is:")                                            # shows all accounts and balance at the end
        for key, value in diAccounts.items():
            print(key.ljust(12) + ": $" + f"{value:.2f}".rjust(12))


    else:                                                                   # if user enters invalid value from initial options
        print ("Sorry - that's not a valid choice")

    print("")
    strMore = input("Would you like another transaction? enter y or n: ")   # prompts for another transaction option

    if (strMore != "y"):                                                    # if user chooses not to do another transaction
        break                                                               # break from loop, exit

    print("")


# exit message
print("#"*80)
print("Thank you for using ATM")
print("#"*80)