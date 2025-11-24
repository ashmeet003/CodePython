# Ashmeet Kaur
# CompB10 Fall2025
# pillow
# open an image - apply filter - save the image

import os
from PIL import Image, ImageFilter, ImageEnhance

# This will look for images in a subdirectory "images"
strImageDir = "./images"

# These variables need to be initialized at the top.
imgFile = None
strFileName = ""

def returnFiles(strDir):
    arTemp = []
    for file in os.listdir(strDir):
        # This will make sure only files are returned.
        if str(file).find(".") > 0 and len(file)>3 :
            name, type = file.split(".")
            # Limit file types to JPG and PNG.
            if str(type).lower() == "jpg" or str(type).lower() == "png":
                arTemp.append(file)
    return arTemp

def filterOne(imgFile):
    # Split the image into channels
    imRed, imGreen, imBlue = imgFile.split()
    # Rotate the red channel 3 degrees
    imRed = imRed.rotate(3)
    # Rotate the green channel 358 degrees
    # This is the same as 2 degrees CCW
    imGreen = imGreen.rotate(358)
    # Blur the blue channel
    imBlue = imBlue.filter(ImageFilter.GaussianBlur(30))
    # These two lines adjust the brightness of the blue channel
    # First, we have to create the enhancer instance
    enhancer = ImageEnhance.Brightness(imBlue)
    # Second, we apply it back to the image.
    imBlue = enhancer.enhance(1.5)
    # Merge the channels into one RGB image
    imgNew = Image.merge("RGB",(imRed, imGreen, imBlue))
    # Enhance brightness for the whole image.
    enhancer = ImageEnhance.Brightness(imgNew)
    imgNew = enhancer.enhance(1.5)
    print("\nThe Filter has Been Applied.\n")
    imgNew.show()
    # return the image object
    return imgNew


def filterTwo(imgFile):
    r,g,b = imgFile.split()
    # filters red:
    r = r.filter(ImageFilter.GaussianBlur(30))
    enhancer = ImageEnhance.Brightness(r)
    r = enhancer.enhance(0.8)
    # filters blue:
    b = b.filter(ImageFilter.EDGE_ENHANCE)
    enhancer = ImageEnhance.Color(b)
    b = enhancer.enhance(0.2)
    # filters green:
    enhancer = ImageEnhance.Contrast(g)
    g = enhancer.enhance(2.0)
    # merges image
    imgNew = Image.merge("RGB",(r,g,b))
    print("\nThe Filter has Been Applied.\n")
    # displays and returns image
    imgNew.show()
    return imgNew

def mainMenu():
    print("-"*80)
    print("||","  InstaPy  ".center(74),"||")
    print("-"*80)
    if strFileName == "":
        print(f"\nFile open: None\n")
    else:
        print(f"\nFile open: {strFileName}\n")
    print("What do you want to do?")
    print("1. Open an Image")
    print("2. Apply Filter One")
    print("3. Apply Filter Two")
    print("4. Save Image")
    print("5. Quit")
    strTmp = input("Enter Choice Here:")
    return strTmp

def pressEnter():
    input("\nPress Enter/Return to continue...")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Main program loop
while True:
    strMenu = mainMenu()
    if strMenu == "1":                      # opens image file and displays it
        arFiles = returnFiles(strImageDir)
        print("Which image file would you like to open?")
        for ind, item in enumerate(arFiles,1):      # loops through each file name
            print(f"{ind}. {item}")
        indFile = int(input("Enter the file number: "))-1
        imgFile = Image.open(strImageDir+"/"+str(arFiles[indFile])) # stores image
        strFileName = str(arFiles[indFile])                         # stores file name
        imgFile.show()
        print(f"The file {strFileName} has been opened.\n")

    elif strMenu == "2":            # applies 1st filter
        if imgFile == None:
            print("You need to open an image first!")
        else:
            imgFile = filterOne(imgFile)

    elif strMenu == "3":            # applies second filter
        if imgFile == None:
            print("You need to open an image first!")
        else:
            imgFile = filterTwo(imgFile)

    elif strMenu == "4": # save image
        if imgFile == None:     # checks if any file was opened yet
            print("You need to open an image first!")
        else:
            while True:                                                 # checks for y/n correct input
                strSave = input("\nDo you want to save the image? (y/n): ").strip().lower()
                if strSave == "y":                                      # if user chooses to save file
                    dotIndex = strFileName.find(".")                    # finds dot before extension
                    if dotIndex != -1:                                  # if dot/extension is found
                        fileName = strFileName[0:dotIndex] + "Copy"     # creates new file name: OG_File_NameCopy.extension
                        fileExtension = strFileName[dotIndex:]          # stores last extension part
                        imgFile.save(strImageDir+"/"+fileName+fileExtension)    # merges everything and saves files with new name
                        print("Image saved successfully!\n")
                    else:                                               # if no extension was found originally
                        print("Image extension not found\n")
                    break
                elif strSave == "n":                                    # if user chooses not to save file
                    print("You chose not to save the image.\n")
                    break
                else:                                                   # if invalid input is entered
                    print("Invalid input.\n")

    elif strMenu == "5":        # exits program
        print("")
        print("*"*60)
        print("Thanks for trying InstaPy!".center(60))
        print("*" * 60)
        break

    else:
        print("Invalid Input. Try again.\n")

    pressEnter()

