# Ashmeet Kaur
# CompB10 Fall2025
# The program is based on calculating simple Interest and total amount
# Formulas used: 'I = P * R * T' and 'A = P + I'

# Welcomes user to the calculator
print("*"*81)
print("*"*20 + "Welcome to Simple Interest Calculator".center(41) + "*"*20 + "\n")

# user is asked for input and values are converted to float
# assuming interest rate, principal amount or time could be decimal point values
fPrincipal = float(input("Enter the principal amount: $"))
fRate = float(input("Enter the rate of interest: "))
fTime = float(input("Enter the time of investment (in years): "))

# Calculations are made
fRate = fRate / 100                     # Rate of interest
fInterest = fPrincipal * fRate * fTime  # Interest made
fAmount = fPrincipal + fInterest        # Total Amount calculated

# Prints final interest and amount
print("\n" + "*"*60 + "\n")
print("Your Results:")
print(f"Your interest is: ${fInterest:.2f}")
print(f"Your final amount is: ${fAmount:.2f}")