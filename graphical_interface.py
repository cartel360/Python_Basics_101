import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

def clicked():
    messagebox.showinfo("Clicked", "Button Clicked")

window = tk.Tk()
window.title("Tkinter Basics")
window.geometry("500x300")

# top_frame = Frame(window).pack()
# bottom_frame = Frame(window).pack(side="bottom")

# lbl1 = tk.Label(top_frame, text="Intro to Tkinter").pack()
# bt1 = tk.Button(bottom_frame, text="Click Me", fg="blue", bg="red").pack(side="left")

lbl1 = tk.Label(window, text="Intro to Tkinter")
lbl1.grid(row=0, column=0)

btn1 = tk.Button(window, text="Click Me", fg="blue", bg="red", command=clicked)
btn1.grid(row=1, column=0, columnspan=2)

txt1 = tk.Entry(window, width=30)
txt1.grid(row=2, column=0)

combo = ttk.Combobox(window)
combo["values"]=("Select", 1,2,3,4,5, "One", "Two")
combo.current(0)
combo.grid(row=3, sticky=W)

lbl2 = Label(window, text="Check Button").grid(row=4, sticky=W)
var1 = IntVar()
chk = Checkbutton(window, text="Male", variable=var1).grid(row=5, sticky=W)
var2 = IntVar()
chk = Checkbutton(window, text="Female", variable=var2).grid(row=6, sticky=W)

lbl3 = Label(window, text="Radio Button").grid(row=7, sticky=W)
rad1 = Radiobutton(window, text="Python", value=1).grid(row=8, sticky=W)
rad2 = Radiobutton(window, text="JavaScript", value=2).grid(row=9, sticky=W)
rad3 = Radiobutton(window, text="Java", value=3).grid(row=10, sticky=W)

lbl4 = Label(window, text="Spinbox").grid(row=11, sticky=W)
spin = Spinbox(window, from_=0, to=10, width=10).grid(row=12,sticky=W)

window.mainloop()
