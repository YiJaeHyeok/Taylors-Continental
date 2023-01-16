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
  
tireCount = 0
x= 0
y= 0

class App:
     def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.geometry('650x650')
        self.window.resizable(False,False)
        self.window.title(window_title)
        self.video_source = video_source
        

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
 
         # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        def combine(event):
            self.snapshot(self)
            tirebrandResult(event)
            Department_of_Transportation(event)
            Tire_Pattern(event)
            Tire_Size(event)

        def tirebrandResult(event):
            global tireCount
            w=Label(window,text="Tire Brand:"+ str(tireCount))
            w.place(x=150,y=490)

        def Department_of_Transportation(event):
            global tireCount
            w=Label(window,text="Department of Transportation:"+ str(tireCount))
            w.place(x=150,y=510)

        def Tire_Pattern(event):
            global tireCount
            w=Label(window,text="Tire Pattern:"+ str(tireCount))
            w.place(x=150,y=530)

        def Tire_Size(event):
            global tireCount
            w=Label(window,text="Tire Size:"+ str(tireCount))
            w.place(x=150,y=550)

        #window.bind("qwe",tirebrandResult)

         # Button that lets the user take a snapshot
        self.btn_snapshot1=tkinter.Button(window, text="Exit", width=50, command=self.close)
        self.btn_snapshot1.place(x=150, y= 600)

        #self.window.bind("qwe", self.snapshot, tirebrandResult) 
        self.window.bind("qwe", combine)  

        self.delay = 15
        self.update()
        self.window.mainloop()
 
     def snapshot(self,event):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        print('pic taken')
 
        if ret:
             global tireCount
             tireCount = mc.countDoc() +1
             imageName = 'TireImage_%s' %tireCount
             print(imageName)

             #tireImage.show() #Show image for testing
             tireImage = im.fromarray(frame)

             #2) Save image into DB and retrieve unique key
             imageID = mc.saveImage(tireImage, imageName)
             
             #3) pre-process image

             #4) Process image
             texts = OCR.tesseractReader(tireImage)
             print (texts)

             # ReadData = Continental UT100 DOT12345 1258754 250/45

            #pa.processimage(image)
             b = 1
             c= 2
             d= 3

            #6) categorize into columns and save as documents in order

            #categorize()
                #categorized = [Brand:'Continental', DOT: **** , Size = 250/45 ............]
                #return categorized

             #pa.categorize(b,c,d)
             mc.saveDoc(mc.createDoc(imageID,texts,c,d))
             global output1
             output1=tireCount
        

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