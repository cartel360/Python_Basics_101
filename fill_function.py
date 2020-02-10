import tkinter as tk

window = tk.Tk()
window.title("Tkinter Frames")

tk.Label(window, text="Normal Width", bg="red", fg="white").pack()

tk.Label(window, text="Taking all Available X Width", bg="blue", fg="white").pack(fill="x")

tk.Label(window, text="Taking all Available Y Width", bg="green", fg="white").pack(side="left", fill="y")



window.mainloop()