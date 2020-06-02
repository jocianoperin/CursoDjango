import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Python Tkinter Text Box")
window.minsize(200, 200)


def clickMe():
    label.configure(text='Hello ' + name.get())


label = ttk.Label(window, text="Enter Your Name")
label.grid(column=0, row=0)


name = tk.StringVar()
nameEntered = ttk.Entry(window, width=15, textvariable=name)
nameEntered.grid(column=1, row=1)


button = ttk.Button(window, text="Click Me", command=clickMe)
button.grid(column=2, row=2)

window.mainloop()
