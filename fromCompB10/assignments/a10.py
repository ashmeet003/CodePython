# Ashmeet Kaur
# CompB10 Fall2025
# LBYL and EAFP type error handling.
# The program is based on Fahrenheit to Celsius and vice versa calculator

# Show the UI
print("#" * 80)
print("#" * 9, " " * 60, "#"*9)
print("#" * 9, "Advanced Calculator".center(60), "#" * 9)
print("#" * 9, " " * 60, "#"*9)
print("#" * 80)
print("\n")

#Welcomes user for temperature Calculator
print("Welcome to Temperature Calculator")
print("*"*60)
# This loop works till user opts to end the program
while True:
    # what if user enters a character not int?? ValueError
    # uses LBYL
    while(True):                                    # this loop works till user enters valid option
        strOption = input("Enter 1 to choose 'F to C' or 2 for 'C to F': ")
        if(strOption == "1" or strOption == "2"):   # if user enters 1 or 2
            intOption = int(strOption)                  # string is converted to int
            break                                       # program comes out of loop and proceeds
        else:                                       # else loop continues
            print("Please enter a valid option")
    print("")

    if intOption == 1:                                              # if user chooses F to C conversion
        while(True):                                                # loop works till user enters a valid float value
            strTemp = input("Enter temperature in Fahrenheit: ")    # uses LBYL
            strNum = strTemp.replace(".","",1)
            if(strNum.isnumeric()):
                floatTemp = float(strTemp)                           # asks user for temperature, converted to float
                floatCel = (floatTemp - 32) * 5/9                    # formula for conversion
                print(f"Temperature in Celsius: {floatCel:.2f}C")    # prints answer
                break
            else:
                print("Please enter a valid Temperature")

    else:                                                                    # if user chooses F to C conversion
        while(True):                                                         # loop works till user enters a valid float value
            try:                                                             # uses EAFP
                floatTemp = float(input("Enter temperature in Celsius: "))   # asks user for temperature, converted to float
                floatFah = (floatTemp * 9/5) + 32                            # formula for conversion
                print(f"Temperature in Fahrenheit: {floatFah:.2f}F")         # prints answer
                break
            except:
                print("Please enter a valid Temperature")

    # the following statements works to ask user if user wants another conversion
    # or exit the program
    print("")
    flag = True
    while True:  # uses LBYL
        replay  = input("Do you want to try another temperature conversion? (y/n): ").strip().lower()
        if(replay == "yes" or replay == "y"):
            print("")
            break
        elif(replay == "no" or replay == "n"):
            print("")
            flag = False
            break
        else:
            print("Please enter a valid option from y-yes or n-no")
    if not flag:
        break


print("#" * 12, "Thank you for using this program".center(36), "#" * 12)