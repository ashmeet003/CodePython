# Ashmeet Kaur
# CompB10 Fall2025
# The program is based on Fahrenheit to Celsius and vice versa calculator

print("Welcome to Temperature Calculator")
intOption = int(input("Enter 1 to choose 'F to C' or 2 for 'C to F': "))

if intOption == 1:
    floatTemp = float(input("Enter temperature in Fahrenheit: "))
    floatCel = (floatTemp - 32) * 5/9
    print(f"{floatCel:.2f}F")

if intOption == 2:
    floatTemp = float(input("Enter temperature in Celsius: "))
    floatFah = (floatTemp * 9/5) + 32
    print(f"{floatFah:.2f}C")