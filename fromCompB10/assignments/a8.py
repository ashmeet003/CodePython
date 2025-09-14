# Ashmeet Kaur
# CompB10 Fall 2025
# Email Extractor
# the program functions as:
#   cleans the string to remove extra delimiters [],()
#   splits clean text into a list
#   use list to find words-> email and form email list
#   add new email list to original email list
#   filters email list to only contain unique email
#   sorts email list to display using for loop

strText1 = "In publishing and graphic design, Lorem george.smith@google.com ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on george.smith@google.com meaningful content. Lorem henry@yahoo.com ipsum may be used as a placeholder before final copy is available. It is also used to temporarily (test@gmail.com) replace text in a process called greeking, which allows designers to consider the form of a webpage or newmail@hotmail.com. publication, without the meaning of the text influencing the design."
strText2 = "The Internet (or internet)[a] is the global@gmail.com system of interconnected computer networks that uses the Internet protocol suite (TCP/IP)[dave@hotmail.com] to communicate between networks and devices. It is a network of networks that consists of private, public, academic, business, and government networks of local to global scope, linked by a broad array of electronic, wireless, and optical networking technologies. The Internet carries a vast range of bill@network.us information resources and services, such as the inter-linked hypertext@linkedin.org documents and applications of the World Wide Web (WWW), electronic mail, telephony, and file sharing."
listEmail = ["bill@network.us","george.smith@google.com", "test@gmail.com"]

# Do this assignment WITHOUT the global keyword
# Function that takes in a string, and returns a list of emails found.
# this function assumes that only emails have their ending as ".com", ".us", ".org"
def emailsFound(strText):
    listText = strText.split(" ")               # splits email using one white space into a list
    listEmail = []                              # list to store emails from the listText
    for word in listText:                       # checks every word in listText
        if(word.find("@") != -1):               # if string has @ sign in it
            if(word.find(".com") != -1):            # if ".com" is found as substring
                if not isPresent(word, listEmail):      # if word is not already present in new listEmail
                    listEmail.append(word)                  # append the word to list
            if (word.find(".us") != -1):            # if ".us" is found as substring
                if not isPresent(word, listEmail):      # if word is not already present in new listEmail
                    listEmail.append(word)                  # append the word to list
            if (word.find(".org") != -1):           # if ".us" is found as substring
                if not isPresent(word, listEmail):      # if word is not already present in new listEmail
                    listEmail.append(word)                  # append the word to list
    return listEmail                            # returns list of email found in string


# Function that removes duplicates in a list, taking a list as input and returning the list without duplicates.
def uniqueList(listText):
    uniqueList = []                             # list stores unique emails
    for email in listText:                      # checks every email string in list
        if email not in uniqueList:             # if email string is not already present in list
            uniqueList.append(email)            # email string is added to list
    return uniqueList                           # returns list of unique emails


# Function that takes a string and a list as input
# returns a True or False depending on whether the string value is in the list or not.
def isPresent(strEmail, listEmail):
    if strEmail in listEmail:
        return True
    else:
        return False


# the function cleans the text
# replaces any possible delimiter such as [], ()
# which could hinder splitting text using single whitespace
def cleanText(strText):
    strText.strip()
    strText = strText.replace("(", " ")
    strText = strText.replace(")", " ")
    strText = strText.replace("[", " ")
    strText = strText.replace("]", " ")
    strText = strText.replace(",", " ")
    strText = strText.replace("   ", " ")
    strText = strText.replace("  ", " ")
    return strText


# main program begins
strText1 = cleanText(strText1)              # cleans strText1
emailsInText1 = emailsFound(strText1)       # stores list of unique emails found in strText1

strText2 = cleanText(strText2)              # cleans strText2
emailsInText2 = emailsFound(strText2)       # stores list of unique emails found in strText2

listEmail.extend(emailsInText1)             # concat email list from strText1 to original listEmail
listEmail.extend(emailsInText2)             # concat email list from strText2 to original listEmail

listEmail = uniqueList(listEmail)           # filters listEmail to store only unique emails
listEmail.sort()                            # sort email in alphabetical order

# the following code displays emails using for loop
print("*"*175)
print("")
print("List of emails stored:")
for index in range(len(listEmail)):
    print(f"{index+1}. {listEmail[index]}")
print("")
print("*"*175)