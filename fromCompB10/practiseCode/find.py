strText = "This is a String."
intIndex = strText.find(" ")

# to find next space in str:
intIndex += 1
print(strText.find(" ", intIndex))