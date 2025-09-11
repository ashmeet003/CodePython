# practise of list
liNames = ["Bill", "Joe", "Dave"]

# printing whole list
print(liNames)
print(*liNames)
print("")

# accessing single value from list
strName = liNames[0]
print(strName)
print("")

# changing a value in list
liNames[0] = "Ashley"

# using pop
strTerm = liNames.pop(1)
# or del arrFruit[1] could also be used;
print(f"{strTerm} is fired.")
print("")

# append at the end of the list
liNames.append("Joe")

# use insert for adding to any index (index, value)
liNames.insert(1, "Susie")
liNames.insert(1, ["sub1", "sub2", "sub3"])
print(liNames)

# printing whole list
intCount = 1
for strName in liNames:
    print(f"{intCount}. {strName}")
    intCount += 1


# list.clear()
# cpyList = list.copy()
# count = list.count("Bills")
# length = len(list)
# index = list.index("Joe")
# list.remove("Banana")  removes first Banana found in list
# list.reverse()
# list.sort(reverse = True)