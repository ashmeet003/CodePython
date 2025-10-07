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

# asks for user choice between F to C conversion or C to F
# converted to int for if-else statement

# what if user enters a character not int?? Valueerror
intOption = int(input("Enter 1 to choose 'F to C' or 2 for 'C to F': "))
print("\n")

if intOption == 1:                                                  # if user chooses F to C conversion

    # what if user enters a character not float?? ValueError
    floatTemp = float(input("Enter temperature in Fahrenheit: "))   # asks user for temperature, converted to float
    floatCel = (floatTemp - 32) * 5/9                               # formula for conversion
    print(f"Temperature in Celsius: {floatCel:.2f}C")               # prints answer

elif intOption == 2:                                                # if user chooses F to C conversion

    # what if user enters a character not float?? ValueError
    floatTemp = float(input("Enter temperature in Celsius: "))      # asks user for temperature, converted to float
    floatFah = (floatTemp * 9/5) + 32                               # formula for conversion
    print(f"Temperature in Fahrenheit: {floatFah:.2f}F")            # prints answer

else:                                                               # if user enters wrong option for conversion
    print("Invalid input. Please enter 1 or 2")                     # prints 'Invalid choice' message


##
# modify to include option for another calculation