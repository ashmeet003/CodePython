# Ashmeet Kaur
# CompB10 Fall 2025
# ATM Machine
##############
# add decimal verification if possible
##############

# start with some $$
flSavBal = 500.99
flChkBal = 100.31

# Welcome UI Message
print("#"*80)
print("Welcome to the ATM")
print("#"*80)
print("")

# create a loop for the program
while (True):

    #Show the menu options
    print("Choose an option: 1 - Deposit, 2 - Withdrawal, 3 - Check Balance")
    # Ask the user for their choice
    strMenu = input("Your choice: ")

    # works to deposit money
    if (strMenu == "1"):
        print("You want to make a deposit.\n")

        # asks user to input amount to deposit and converted into float
        flAmount = float(input("Enter the amount you want to deposit: $"))
        strChoice = input("Choose an option: 1 - 'checking' or 2 - 'savings': ").strip()

        if (strChoice == "1"):          # if chosen account is checking
            flChkBal += flAmount
            print("Amount Deposited!")
        elif (strChoice == "2"):        # if chosen account is savings
            flSavBal += flAmount
            print("Amount Deposited!")
        else:                           # if enters wrong number for account selection
            print("You entered Invalid account option!")

        print("Your balance is:")       # shows balance at the end
        print("Checking".ljust(9) + ": $" + str(flChkBal).rjust(12))
        print("Savings".ljust(9) + ": $" + str(flSavBal).rjust(12))




    elif (strMenu == "2"):
        print("You want to make a withdrawal.\n")

        # asks user to input amount to withdraw and converted into float
        flAmount = float(input("Enter the amount you want to deposit: $"))
        strChoice = input("Choose an option: 1 - 'checking' or 2 - 'savings': ").strip()

        if (strChoice == "1"):              # if user chooses checking account
            if (flChkBal > flAmount):       # checks if amount to be withdrawn is present in account or not
                flChkBal -= flAmount        # updates checking account balance
                print("Amount Withdrawn!")
            else:                           # if withdraw amount > amount present in account
                print("You do not have enough balance to withdraw!")
        elif (strChoice == "2"):            # if user chooses savings account
            if(flSavBal > flAmount):        # checks if amount to be withdrawn is present in account or not
                flSavBal -= flAmount        # updates savings account balance
                print("Amount Withdrawn!")
            else:                           # if withdraw amount > amount present in account
                print("You do not have enough balance to withdraw!")
        else:                               # if enters wrong number for account selection
            print("You entered Invalid account option!")

        print("Your balance is:")           # shows balance at the end
        print("Checking".ljust(9) + ": $" + str(flChkBal).rjust(12))
        print("Savings".ljust(9) + ": $" + str(flSavBal).rjust(12))




    elif (strMenu == "3"):                  # Shows account Balance
        print("You want to check a balance.\n")
        print("Your balance is:")
        print("Checking".ljust(9) + ": $" + str(flChkBal).rjust(12))
        print("Savings".ljust(9) + ": $" + str(flSavBal).rjust(12))



    else:
        print ("Sorry - that's not a valid choice")

    print("")
    strMore = input("Would you like another transaction? enter y or n: ")

    if (strMore != "y"):            # if user chooses not to do another transaction
        break

    print("")