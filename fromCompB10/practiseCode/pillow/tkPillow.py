from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import tkinter as tk
import random

window = tk.Tk()

def changePic():
    global image1, image2, imgDisplay
    intRotate = random.randint(0,359)
    min_x = random.randint(0, 1620)
    max_x = min_x + 300
    min_y = random.randint(0, 973)
    max_y = min_y + 300
    image2 = image1.crop((min_x, min_y, max_x, max_y))
    # image2 = image2.rotate(intRotate)
    imgDisplay = ImageTk.PhotoImage(image2)
    picLabel["image"] = imgDisplay

def filterA():
    global image1, image2, imgDisplay
    red, green, blue = image2.split()
    red = red.rotate(-5).filter(ImageFilter.GaussianBlur(10))
    green = green.rotate(5).filter(ImageFilter.GaussianBlur(5))
    enh = ImageEnhance.Brightness(blue)
    blue = enh.enhance(3)
    image2 = Image.merge("RGB", (red, green, blue))
    imgDisplay = ImageTk.PhotoImage(image2)
    picLabel["image"] = imgDisplay

filename = "images/beach.jpg"
image1 = Image.open(filename)
image2 = image1.crop((450,450,700,700))

imgDisplay = ImageTk.PhotoImage(image2)


picLabel = tk.Label(window, image=imgDisplay)
picLabel.pack()
txtLabel = tk.Label(window,text="Picture!")
txtLabel.pack()
butChangeImg = tk.Button(window,text="Change Image",command=changePic)
butChangeImg.pack()
butFilter = tk.Button(window,text="Filter Image",command=filterA)
butFilter.pack()

window.mainloop()


