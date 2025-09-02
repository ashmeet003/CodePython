# Name: Ashmeet Kaur
# CompB10 Fall 2025

arQuote = ["in", "rather", "someone", "a", "change", "be", "else's", "powerful", "cloud", "rainbow"]

arQuote.sort()                          #sorts the list
arQuote.pop(2)                          # removes 3rd element
arQuote.remove("powerful")              # removes element "powerful"
arQuote2 = arQuote.copy()               # creates a copy of list as arQuote2
arQuote[0] = arQuote2[1].capitalize()   # stores 2nd element of arQuote2 at 1st index of arQuote with capitalized first letter
arQuote[1] = arQuote2[0]                # stores 2nd element of arQuote2 at 1st index of arQuote
heldWord = arQuote.pop(7)               # removes 8th element of arQuote and stores it in heldWord
arQuote.pop(6)                          # removes 7th element
arQuote2 = arQuote.copy()               # copies arQuote to arQuote2
arQuote[2] = arQuote2[5]                # stores 5th element of arQuote2 at 2nd index of arQuote
arQuote[5] = arQuote2[2]                # stores 2nd element of arQuote2 at 5th index of arQuote
arQuote[3] = arQuote2[4]                # stores 4th element of arQuote2 at 3rd index of arQuote
arQuote[4] = arQuote2[3]                # stores 3rd element of arQuote2 at 4th index of arQuote
arQuote.insert(4, heldWord)             # inserts value in heldWord at index 4

#prints arQuote without ',' or []
print(*arQuote)