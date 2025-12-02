import tkinter as tk

def doCalc():
    label3["text"] = "Average: "+ str((float(entry1.get()) + float(entry2.get()))/2)

window = tk.Tk()
window.geometry("300x300")
label = tk.Label(window, text="Number 1")
label.pack()
entry1 = tk.Entry()
entry1.pack()
label2 = tk.Label(window, text="Number 2")
label2.pack()
entry2 = tk.Entry()
entry2.pack()
btn = tk.Button(window, text="Get Avg", command=doCalc)
btn.pack()
label3 = tk.Label(window, text="Average:")
label3.pack()



window.mainloop()
