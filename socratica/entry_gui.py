# import tkinter
from tkinter import *
from tkinter import ttk

# tkinter._test()

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", command=myClick, fg="green", bg="yellow")
myButton.pack()


root.mainloop()
