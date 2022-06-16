import MongoConnection as mc
import processingAlgorithms as pa
import OCR 
from random import *
import arduino
from time import sleep
import cv2
from datetime import datetime
from PIL import Image as im

#Requres update whenever image folder change

tireCount = mc.count() +1
imageName = 'TireImage_%s' %tireCount

def runSystem():

    cam = cv2.VideoCapture(0)

    while True:
        cam_on, image = cam.read()
        if not cam_on:
            print("No input from sensor")
            quit()
        cv2.imshow("Tire Sidwall Reader",image)

            #1) Take Image
        k = cv2.waitKey(1)
        #if arduino.arduinoCapture():
        if k%256 == 32: #change to when receive serial from Aduino
                   
            #img_counter += 1
            ### Change the name of one field to unique
            tireImage = im.fromarray(image)
            #tireImage.show() Show image for testing
            #sleep(2)
        
            #2) Save image into DB and retrieve unique key
            imageID = mc.saveImage(tireImage, imageName)
            
            #4) pre-process image
            
            #5) Process image
            texts = OCR.tesseractReader(tireImage)
            print (texts)

            #pa.processimage(image)
            b = (randint(1,10))
            c= (randint(1,100))
            d= (randint(1,1000))

            #6) categorize into columns and save as documents in order
            pa.categorize(b,c,d)
            mc.saveDocument(mc.createDocument(imageID,texts,c,d))

        elif k%256 == 27: #if press terminate from UI
        # ESC pressed
            print("Escape hit, closing...")
            cv2.destroyWindow("Tire Sidewall Image")
            break

runSystem()

#showimage = mc.loadImage('tmp')
#showimage.show()


'''

        if len(os.listdir(folderDir)) == 0:
        #no fileg
            print("Waiting")
            sleep(3)
        
        else:
            print("Start main Program")
    
        
            #4) pre-process image
            

            #5) Process image
            texts = OCR.tesseractReader(image)
            print (texts)

            #pa.processimage(image)
            b = (randint(1,10))
            c= (randint(1,100))
            d= (randint(1,1000))

            #6) categorize into columns and save as documents in order
            pa.categorize(b,c,d)
            mc.saveDocument(mc.createDocument(imageID,b,c,d))
        
            lsi.closeImage(image)
            lsi.removePicInFolder(imageLoc)
            print("Done")
            sleep(1)

runSystem()
'''