import tkinter as tk
class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.entry1 = tk.Entry(self.root)
        self.entry1.bind("<KeyPress>", self.onKeyPress)
        self.entry1.pack()
        self.root.mainloop()
 
    def onKeyPress(self, event):
        print("Key has been Pressed.")
display = Display()