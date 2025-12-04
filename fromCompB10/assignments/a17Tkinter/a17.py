from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import tkinter as tk

def applyFilterOne():
    global image1, imgDisplay
    # Split the image into channels
    imRed, imGreen, imBlue = image1.split()
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
    image1 = Image.merge("RGB",(imRed, imGreen, imBlue))
    # Enhance brightness for the whole image.
    enhancer = ImageEnhance.Brightness(image1)
    image1 = enhancer.enhance(1.5)
    print("\nThe Filter has Been Applied.\n")
    imgDisplay = ImageTk.PhotoImage(image1)
    picLabel["image"] = imgDisplay

def applyFilterTwo():
    global image1, imgDisplay
    r,g,b = image1.split()
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
    image1 = Image.merge("RGB",(r,g,b))
    print("\nThe Filter has Been Applied.\n")
    # displays and returns image
    imgDisplay = ImageTk.PhotoImage(image1)
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

root = tk.Tk()
root.title("Filter Image App")
root.geometry("1000x600")


filename = "images/beach.jpg"
image1 = Image.open(filename)

imgDisplay = ImageTk.PhotoImage(image1)

txtLabel = tk.Label(root,text="Picture!")
txtLabel.pack()
picLabel = tk.Label(root, image=imgDisplay, width=550, height=350)
picLabel.pack()


filter1Button = tk.Button(master = root, text = "Filter 1", command = applyFilterOne)
filter1Button.pack()
filter2Button = tk.Button(master = root, text = "Filter 2", command = applyFilterTwo)
filter2Button.pack()
root.mainloop()