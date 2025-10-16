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
while True:
    # asks for user choice between F to C conversion or C to F
    # converted to int for if-else statement

    # what if user enters a character not int?? ValueError
    while(True):
        strOption = input("Enter 1 to choose 'F to C' or 2 for 'C to F': ")
        if(strOption == "1" or strOption == "2"):
            intOption = int(strOption)
            break
        else:
            print("Please enter a valid option")
    print("\n")

    if intOption == 1:                                                  # if user chooses F to C conversion

        # what if user enters a character not float?? ValueError
        while(True):
            strTemp = input("Enter temperature in Fahrenheit: ")
            strNum = strTemp.replace(".","",1)
            if(strNum.isnumeric()):
                floatTemp = float(strTemp)   # asks user for temperature, converted to float
                floatCel = (floatTemp - 32) * 5/9                               # formula for conversion
                print(f"Temperature in Celsius: {floatCel:.2f}C")               # prints answer
                break
            else:
                print("Please enter a valid Temperature")

    else:                                                # if user chooses F to C conversion

        # what if user enters a character not float?? ValueError
        while(True):
            try:
                floatTemp = float(input("Enter temperature in Celsius: "))      # asks user for temperature, converted to float
                floatFah = (floatTemp * 9/5) + 32                               # formula for conversion
                print(f"Temperature in Fahrenheit: {floatFah:.2f}F")            # prints answer
                break
            except:
                print("Please enter a valid Temperature")

    print("")
    replay  = input("Do you want to try another temperature conversion? (y/n): ").strip().lower()
    if(replay == "yes" or replay == "y"):
        print("")
        continue
    elif(replay == "no" or replay == "n"):
        print("")
        break
    else:
        print("Please enter a valid option from y-yes or n-no")


print("#" * 9, "Thank you for using this program".center(36), "#" * 9)