strText = "This is a String."
intIndex = strText.find(" ")
print(intIndex)

# to find next space in str:
intIndex += 1
print(strText.find(" ", intIndex))

# strings are iterable:
strNew = ""
for letter in strText:
    if letter.isalpha() or letter == " ":
        strNew += letter
print(strNew)


# to print words with only alphas..no extra characters
liText = strText.split(" ")
print(liText)
for strWord in liText:
    if not strWord[-1].isalpha():
        print(strWord[0:-1])
    else:
        print(strWord)

# removes same words
setText = set(liText)
print(setText)
liText = list(setText)
liText.sort()
print(liText)

print(" ".join(liText))