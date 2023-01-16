from tkinter import Tk, Label
root=Tk()
def key_pressed(event):
 w=Label(root,text="Key Pressed:"+event.char)
 w.place(x=70,y=90)
root.bind("<Key>",key_pressed)
root.mainloop()