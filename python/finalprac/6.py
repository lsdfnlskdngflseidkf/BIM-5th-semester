import tkinter as tk
from tkinter import simpledialog,messagebox
again=tk.Tk()
again.title("multiply two numbers with gui")
again.geometry("500x500")
def mul():
    a=simpledialog.askinteger("Enter","Enter first number")
    b=simpledialog.askinteger("Enter","Enter second number")
    res=a*b
    messagebox.showinfo("Result",f"The product is {res}")
btn=tk.Button(again,text="Click this button",command=mul)
btn.pack()
again.mainloop()
