import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Main Window")
window.geometry("1080x600")

lbl1 = Label(window, text="Welcome to Tkinter", font=("Arial", 50)).pack()

img = ImageTk.PhotoImage(Image.open("pic.jpg"))
imglabel = Label(window, image=img).pack()


window.mainloop()