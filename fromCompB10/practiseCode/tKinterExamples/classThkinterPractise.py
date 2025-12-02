import tkinter as tk



def doCalc():
    if(strEntryW.get().isnumeric() and strEntryL.get().isnumeric()):
        intW = int(strEntryW.get())
        intH=int(strEntryL.get())
        intArea=intW*intH
        label2["text"]=f"The result is: {intArea}"
    else:
        print("Enter valid num")

root = tk.Tk()
root.title("Basic Window")
root.geometry("600x300")

label1  = tk.Label(master=root, text="Rectangle area calculator:").pack()

strEntryW=tk.StringVar()
entryW=tk.Entry(master=root, textvariable=strEntryW).pack()

strEntryL=tk.StringVar()
entryL=tk.Entry(master=root, textvariable=strEntryL).pack()

button1=tk.Button(master=root, text="Calculate", command=doCalc).pack()
label2=tk.Label(master=root, text="")
label2.pack()

root.mainloop()