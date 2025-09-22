# Ashmeet Kaur
# CompB10 Fall2025
# Error Pokemon: because you gotta catch them all:)
# raising errors on Purpose

strName = "Bill"
intAge = 48
try:
    #TypeError: trying to add int and string values
    strSentence = strName + " is " + intAge + " years old."
except TypeError as e:
    print("Error raised as: ", str(e))

try:
    #ValueError: strName is valid just not compatible for int conversion
    strToInt = int(strName)
except ValueError as e:
    print("Error raised as: ", str(e))

try:
    # ZeroDivisionError: dividing by 0
    intDivide = intAge / 0
except ZeroDivisionError as e:
    print("Error raised as: ", str(e))

try:
    # NameError: Python doesn't recognize 'intage'; Not defined yet
    print(intage)
except NameError as e:
    print("Error raised as: ", str(e))

try:
    # IndexError: trying to access an index which doesn't exist
    myList = [1,2,3]
    print(myList[3])
except IndexError as e:
    print("Error raised as: ", str(e))



