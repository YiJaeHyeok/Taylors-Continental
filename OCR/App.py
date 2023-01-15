import MongoConnection as mc
#import Functions.processingAlgorithms as pa
import OCR
import cv2
from PIL import Image as im
import sys

import tkinter
from tkinter import *
from tkinter import Label
import cv2
import PIL.Image, PIL.ImageTk
import time
  
class App:
     def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
 
        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
 
         # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        #def onKeyPress(self, event):
        #    print("Key has been Pressed.")

        #tkinter.Tk().bind("<KeyPress>", self.onKeyPress) 
        


        result = ""
        def show(OCRoutput):
            global result
            result+=OCRoutput
            label_result.config(text=result)
            
        def clear():
            global result
            result = ""
            label_result.config(text=result)

        label_result = tkinter.Label(window,text="result tab \n",font=("aerial",12))
        label_result.pack(side=TOP, expand=True)

         # Button that lets the user take a snapshot
        self.btn_snapshot1=tkinter.Button(window, text="Exit", width=50, command=self.close)
        self.btn_snapshot1.pack(side="left", expand=True)
        
         #k = cv2.waitKey(1)
         #self.btn_snapshot2=tkinter.Button(window, text="testbutton2", width=50, command=self.snapshot)
         #self.btn_snapshot2.pack(side="left", expand=True)

    

         # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
 
        self.window.mainloop()
 
     def snapshot(self):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
             #tireImage = im.fromarray(frame)
             #tireCount = mc.countDoc() +1
             #imageName = 'TireImage_%s' %tireCount
             #imageID = mc.saveImage(tireImage, imageName)
             print("test")

     def update(self):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
 
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
 
        self.window.after(self.delay, self.update)
 
     def close(self):
    #win.destroy()
        self.window.quit()
    
 
class MyVideoCapture:
    def __init__(self, video_source=0):
         # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
 
         # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
 
     # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
 
 # Create a window and pass it to the Application object
App(tkinter.Tk(), "Continental Automation Tire Reading Program")