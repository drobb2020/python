# import tkinter
from tkinter import *
from tkinter import ttk

# tkinter._test()

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked the button!!")
    myLabel.pack()


# Create a simple label widget
# mylabel0 = Label(root, text="             ")
# mylabel1 = Label(root, text="Hellow World!")
# mylabel2 = Label(root, text="My name is David Robb")
# mylabel3 = Label(root, text="                     ")

# Shove it onto the screen
# mylabel0.grid(row=0, column=0)
# mylabel1.grid(row=1, column=0)
# mylabel2.grid(row=2, column=0)
# mylabel3.grid(row=3, column=0)

myButton = Button(root, text="Click Me!", command=myClick, fg="green", bg="yellow")
myButton.pack()


root.mainloop()
