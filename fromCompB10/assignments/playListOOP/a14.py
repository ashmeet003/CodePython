# Ashmeet Kaur
# CompB10 Fall 2025
# OOP PLayList
# uses class to create list of objects, to update values, add/remove objects and store final list to pickle file

import pickle

# The Song class initialises values, displays object in string format and has a setter function for rating
class Song:

    def __init__(self, title, year, rating):
        self.songTitle = title
        self.songYear = year
        self.songRating = rating

    def __str__(self):
        return f"\"{self.songTitle}\"".ljust(20,".") + f"Year: {self.songYear}".ljust(30,".") + f"Rating: {self.songRating:.1f}".rjust(12,".")

    def setRating(self, rating):
        self.songRating = rating



def addSong(liSongs, title, year, rating):                              # initialises a new song object and appends to list
    for obSong in liSongs:                                              # checks if an object with same name and year already exists
        if(obSong.songTitle == title and obSong.songYear == year):      # if yes, the object doesn't get appended to list
            print(f"\"{title}\" with year: {year} already exists.")
            return                                                      # returns back to main function
    liSongs.append(Song(title, year, rating))                           # else object is added to list
    print(f"\"{title}\" added successfully.")

def removeSong(liSongs, songIndex):                                     # removes a song from list based on index given
    tempSong = liSongs.pop(songIndex)                                   # stores popped song object to display the next message
    print(f"\"{tempSong.songTitle}\" removed successfully.")

def loadPlaylist():                                                     # the function is used to load data from pickle file to present list
    try:
        with open("playListOOP.txt", "rb") as f:                        # if a file is found, the object given in it is loaded
            playlist = pickle.load(f)
            print("Playlist loaded.")
            return playlist                                             # the loaded object is stored in list and returned as list
    except FileNotFoundError:                                           # if no file exists returns empty list
        print("Playlist not found.")
        return []

# Further functions are created to remove redundant code

def displaySongs(liSongs):                                              # displays song object present in list
    intNum = 1
    for obSong in liSongs:
        print(f"{intNum}.", obSong)
        intNum += 1


def validateRating(rating):                                             # validates the rating to be between 0 and 5
    while True:
        tempRating = rating.replace(".", "", 1)     # checks for valid float value
        if tempRating.isdigit():
            rating = float(rating)
            if rating >= 0 and rating <= 5:                             # if valid, rating is returned as float value
                return rating
            else:
                print("Rating must be between 0 and 5.")                # if invalid numeric value was entered, appropriate message is displayed
        else:
            print("Rating must be between 0 and 5.")                    # if invalid value was entered, appropriate message is displayed
        rating = input("Enter song's rating between 0-5: ").strip()     # again asks for input if wrong input is entered


def validateIndex(liSongs, index):                                      # validates index entered by user for songs playList
    while True:
        if index.isdigit():                                             # if index is a digit
            index = int(index)
            if (index > 0 and index <= len(liSongs)):                   # and the index entered is valid
                return(index - 1)                                       # returns the index of song in list by : position - 1
            else:                                                       # if invalid numeric value was entered, appropriate message is displayed
                print(f"Number entered must be between 1 and {len(liSongs)}\n")
        else:                                                           # if invalid value was entered, appropriate message is displayed
            print("Enter a valid song index from List.\n")
        displaySongs(liSongs)                                           # displays list of songs again and asks for valid input if wrong input is entered
        index = input("Enter song's index to remove from list: ").strip()


# This is the main function of program
def main():
    liSongs = loadPlaylist()                                            # loads list from pickle file to local variable
    print("""
    ******************************
    Welcome to the OOP PlayList!!
    ******************************
    """)

    while True:
        print("""
        Menu:
        1. View songs
        2. Add song
        3. Remove song
        4. Update rating
        5. Exit\n""")

        choice = input("Enter your choice: ")

        if choice == "1":                                                # displays list of songs available in list
            print("Current song Playlist:")
            if not liSongs:                                              # if no song is available, prints appropriate message
                print("No songs to display.\n")
                continue
            displaySongs(liSongs)


        elif choice == "2":                                              # adds new song to list
            print("Add a new song:")
            title = input("Enter song's title: ").strip().title()        # title entered is stripped and formatted to title case
            while True:                                                  # validates year entered to be a 4-digit number
                year = input("Enter song's year: ").strip()
                if year.isdigit() and len(year) == 4:
                    year = int(year)
                    break
                else:
                    print("Year must be four digits.")
            strRating = input("Enter song's rating between 0-5: ").strip()  # validates rating entered
            rating = validateRating(strRating)                           # returned valid rating is stored to use in object
            addSong(liSongs, title, year, rating)                        # appends the song entered to list if not already present


        elif choice == "3":                                              # removes a song from the list
            print("Remove song:")
            if not liSongs:                                              # if list is empty, prints appropriate message
                print("No songs to remove.\n")
                continue
            displaySongs(liSongs)                                        # displays songs available in list
            strIndex = input("Enter song's index to remove from list: ").strip()    # enters position/index of song in list displayed
            index = validateIndex(liSongs, strIndex)                     # validates input entered, index returned is index of song in list from 0 onwards
            removeSong(liSongs, index)                                   # removes song from list


        elif choice == "4":
            print("Update rating:")                                      # to update rating of a song
            if not liSongs:                                              # if list is empty, appropriate message is displayed
                print("No songs to update.\n")
                continue
            displaySongs(liSongs)                                        # else, displays list in numbered format
            strIndex = input("Enter song's index to update from list: ").strip()
            index = validateIndex(liSongs, strIndex)                     # validates index input and stores index of song in actual list from 0
            strRating = input("Enter song's rating between 0-5: ").strip()
            rating = validateRating(strRating)                           # validates rating to be between 0 and 5
            liSongs[index].setRating(rating)                             # uses setter function to update rating of chosen song


        elif choice == "5":                                              # exits program and saves list in pickle
            print("Exiting...\n")
            print("Your final playlist:")
            displaySongs(liSongs)                                        # displays final list of songs

            with open("playListOOP.txt", "wb") as file:                  # writes new updates list to pickle
                    pickle.dump(liSongs, file)
            print("\nPlaylist saved to playlistOOP.txt\n")
            break                                                        # exits while loop / end of program

        else:                                                            # if wrong choice from menu is entered
            print("Invalid choice.\n")


# displays ending message
    print("""
******************************
    Thank you for playing.
******************************
    """)

if __name__ == "__main__":                                               # to enter main function of program
    main()