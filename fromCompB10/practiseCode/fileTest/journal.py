import os
print("********** My Journal ****************")

if not(os.path.exists('journal.txt')):
    myFile = open('journal.txt',"w")
    myFile.close()

myFile = open('journal.txt',"r")
strJournal = myFile.read()
myFile.close()
print(strJournal)

strDate = input("What is today's date? ")
strEntry = input("What do you want to add?")

myFile = open('journal.txt',"a")
myFile.write(f"{strDate}\n{strEntry}\n\n")
myFile.close()

print("You completed the journal file")