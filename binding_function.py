import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Binding Functions")


def hi():
    tk.Label(window, text="Hello "+str(name.get())+" how are you doing?").pack()
    
tk.Label(window, text="Enter your Name").pack()

name = tk.Entry(window, width=30)
name.pack()

tk.Button(window, text="Click Me", command=hi).pack()


window.mainloop()