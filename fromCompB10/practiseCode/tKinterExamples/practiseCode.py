import tkinter as tk

def updateLabel():
    strText = str(entry.get())
    label1["text"] = "Hello, " + strText

window = tk.Tk()
window.geometry("400x300")

frame1 = tk.Frame()
frame2 = tk.Frame()

label1 = tk.Label(
    master=frame1,
    text="Hello World!",
    bg="white",
    fg="black",
    height=10,
    width=20,
    borderwidth=2,
    relief="raised"
)
label1.pack()


label2 = tk.Label(master=frame2,text="Your Name")
entry = tk.Entry(master=frame2,width=25)

label2.pack()
entry.pack()

button = tk.Button(master=frame2,text="Click ME!", command=updateLabel)
button.pack()

frame2.pack()
frame1.pack()


window.mainloop()