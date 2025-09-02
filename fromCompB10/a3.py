# Name: Ashmeet Kaur
# CompB10

#list is declared
liCard = []

# in the following lines, user is asked for input and stored input is appended to the list
name = input("Enter your full name: ").strip().title() # strip() for extra white space and title() to make 1st letter capital
liCard.append(name)
phoneNumber = input("Enter your phone number: ").strip() #strip for extra spaces
liCard.append(phoneNumber)
email = input("Enter your email: ").strip().lower() #lower in case capital letters are entered for email
liCard.append(email)
birthday = input("Enter your birthday: ").strip().title() # title in case 'aug 8, 2025' is entered
liCard.append(birthday)

print(liCard) # prints list
print("\n\n") # adds two line breaks

# personalCard uses multi-line strings and f string
personalCard = f"""Here is your card:
Name: {liCard[0]}
Phone: {liCard[1]}
Email: {liCard[2]}
Birthday: {liCard[3]}"""

print(personalCard) # prints personalCard