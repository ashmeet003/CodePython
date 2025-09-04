strName = "Ash"
intAge = 22

# 1st method: string format
strText = "My name is {strName} and my age is {intAge}"
strText = strText.format(strName = strName, intAge = intAge)
print(strText)

# 2nd method f string method
strText2 = f"Hello {strName}! Your age is {intAge}"
print(strText2)