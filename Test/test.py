import tkinter
from tkinter import *

root = Tk()
root.geometry("500x600+100+200")
label_result = Label (root, width=25,height=2,text="",font=("aerial",30))
label_result.pack()

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

label_result = Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(root,text="C", width =5, height = 1, font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(root,text="write", width =5, height = 1, font=("aerial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("/")).place(x=10,y=200)

root.mainloop()