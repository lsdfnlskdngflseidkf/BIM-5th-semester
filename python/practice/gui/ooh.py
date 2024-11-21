import tkinter as tk
from tkinter import *
window = tk.Tk()

window.geometry("400x400")
lb = tk.Label(text="This is a label in a window that uses tk interface")
lb.pack()

bt=tk.Button(text="Do NOT click this button")
bt.pack()


en=tk.Entry()
enlab=tk.Label(text="Enter your name")
enlab.pack()
en.pack()
name=en.get()
en.delete(0,5)



window.mainloop()