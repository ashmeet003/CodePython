import tkinter as tk

def doAvg():
    myAnswer["text"] = "Your Average is:" + str((float(entN1.get()) + float(entN2.get()))/2)

window = tk.Tk()
window.geometry("400x300")

myFrame1 = tk.Frame(window, pady=30, padx=20)
myFrame1.pack()
myFrame2 = tk.Frame(window, pady=10, padx=20)
myFrame2.pack()
myFrame3 = tk.Frame(window, pady=10, padx=20)
myFrame3.pack()
myFrame4 = tk.Frame(window, pady=10, padx=20)
myFrame4.pack()

myLabel = tk.Label(myFrame1, text="Averages")
myLabel.pack()
myAnswer = tk.Label(myFrame1, text="Your Average is: ")
myAnswer.pack()

lblN1 = tk.Label(myFrame2, text="Enter a Number")
lblN1.pack()
entN1 = tk.Entry(myFrame2)
entN1.pack()

lblN2 = tk.Label(myFrame3, text="Enter a Number")
lblN2.pack()
entN2 = tk.Entry(myFrame3)
entN2.pack()

btnClick = tk.Button(myFrame4, text="Click Me", command=doAvg)
btnClick.pack()

window.mainloop()