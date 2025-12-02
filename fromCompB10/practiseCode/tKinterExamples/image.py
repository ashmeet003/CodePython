import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.geometry("900x600")

image1 = Image.open("images/beach.jpg")
test = ImageTk.PhotoImage(image1)
label= tkinter.Label(window, text= "image").pack()
label1 = tkinter.Label(
    image=test,
    width = 550,
    height = 350,)
label1.pack()

window.mainloop()