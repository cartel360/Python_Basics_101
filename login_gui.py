import os
import tkinter 
from tkinter import *
from tkinter import messagebox



def log():
    user = "Billy"
    pass_word = "billy"
    if username.get() == user and password.get() == pass_word:
        messagebox.showinfo("Logging In", "Log in Successful")
        login.destroy()
        import main_gui
    else:
        messagebox.showinfo("Logging In", "Log in Unsuccesful!!\nInvalid Credentials")
        
def destroy():
    login_gui.destroy()

login = tkinter.Tk()
login.title("Simple Login")

lbl1 = Label(login, text="Username").grid(row=0, sticky=W, ipady=5, ipadx=5)

username = Entry(login, width=30)
username.grid(row=0, column=1)

lbl2 = Label(login, text="Password").grid(row=1, sticky=W, ipady=5, ipadx=5)

password = Entry(login, width=30, show="*")
password.grid(row=1, column=1)

tkinter.Checkbutton(login, text="Keep Me Logged In").grid(row=2, columnspan=2)

tkinter.Button(login, text="login", command=log).grid(row=3, columnspan=2)



login.mainloop()