# Ashmeet Kaur
# CompB10 Fall2025
# Text Sophistication Algorithm


# the function cleans the text, replaces any delimiter with space
def cleanText(strText):
    strText = strText.replace("\n", " ")
    strText = strText.replace("—", " ")
    strText = strText.replace("-", " ")
    strText = strText.replace("[", " ")
    strText = strText.replace("]", " ")
    strText = strText.replace("(", " ")
    strText = strText.replace(")", " ")
    strText = strText.replace(". ", " ")
    strText = strText.replace("?", " ")
    strText = strText.replace("!", " ")
    strText = strText.replace(", ", " ")
    strText = strText.replace("   ", " ")
    strText = strText.replace("  ", " ")
    return strText

# returns a list of unique words in the text
def uniqueWords(strText):
    liWords = strText.split()
    arNew = []
    for strWord in liWords:
        if (strWord not in arNew):
            arNew.append(strWord)
    return arNew

# the function returns length and prints list of words with length > 7
def longWords(liWords):
    intNumCount = 0
    for index in range(len(liWords)):  # from last → first
        if len(liWords[index]) > 7:
            intNumCount += 1
    return(intNumCount)

# the following program get a text from user and stores it into a list
# user can choose to enter more text if needed
liText = []
while True:
    strText = input("Enter the text: ").strip()
    liText.append(strText)

    reType = input("Do you want to enter another text snippet? y/n: ").strip().lower()
    if reType == "y":
        continue
    else:
        break


# the following program does all calculation
# finds number of sentences, words, words>7, average word length
# total score = sum of all the above factors
# text number and score is stored in dictionary as key-value pair
# the dictionary is then sorted according to values
# and displayed in descending order
# The order signifies level of text from highest to lowest
diScores = {}
for index in range(len(liText)):
    strText = liText[index]
    # num of characters
    numOfChar = len(strText)
    numWords = len(strText.split())
    # average word length
    avgWordLength = numOfChar / numWords
    # num of sentences
    sentenceCount = strText.count(". ") + strText.count("! ") + strText.count("? ") + 1
    strText = cleanText(strText)
    liTemp = uniqueWords(strText)
    #num of unique words used
    uniqueWordCount = len(liTemp)
    # num of words greater than 7
    longWordCount = longWords(liTemp)

    # total score is calculated and text number and score is stored in dictionary
    totalScore = sentenceCount + uniqueWordCount + longWordCount + avgWordLength
    key = f"Text{index + 1}"
    diScores[key] = totalScore


# Sort by values in descending order
sorted_items = sorted(diScores.items(), key=lambda item: item[1], reverse=True)
# Convert back to a dictionary
sorted_dict = dict(sorted_items)

# the following set of code displays sorted dictionary
print("*"*150 + "\n")
print("Difficulty levels of text(s) entered; highest to lowest:")
intNum = 1
for key, value in sorted_dict.items():
    print(f"{intNum}. {key}, Score: {value:.2f}")
    intNum += 1
print("\n" + "*"*150)
