from tkinter import *
def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result.config(text=str(cm)+"cm")


window =Tk()
window.title("Length Converter App")
window.geometry("400x400")
entry = Entry(window)
entry.pack()

button = Button(window, text= "convert to cm", command=convert)
button.pack()

result = Label(window,text="")
result.pack()

window.mainloop()