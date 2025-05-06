# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# setup tkinter winidow
root=Tk()
root.geometry("200x200")

# function for displaying warning message
# This will be called once the button is clicked
# messagebox.showwarning("Window name", "Text to be displayed")
def msg():
        messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding button widget to Window
button=Button(root, text="Scan for Virus", command=msg)
button.place(x=40,y=80)

# Entering main event loop
root.mainloop()