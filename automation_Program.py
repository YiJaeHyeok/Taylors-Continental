import MongoConnection as mc
#import Functions.processingAlgorithms as pa
import OCR 
import cv2
from PIL import Image as im
import sys
#Requres update whenever image folder change
def runProgram():
    cam = cv2.VideoCapture(0)
    while True:

        tireCount = mc.countDoc() +1
        imageName = 'TireImage_%s' %tireCount
        cam_on, image = cam.read()

        if not cam_on:
            print("No input from sensor")
            quit()
        cv2.imshow("Tire Sidwall Reader",image)

            #1) Take Image 
        k = cv2.waitKey(1)

        signal = ''

        if k%256 == 32: #change to when receive serial from Aduino
                   
            tireImage = im.fromarray(image)
            #tireImage.show() #Show image for testing
        
            #2) Save image into DB and retrieve unique key
            imageID = mc.saveImage(tireImage, imageName)
            
            #4) pre-process image
        
        
            
            #5) Process image
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

        elif k%256 == 27: #if press terminate from UI
        # ESC pressed
            print("Escape hit, closing...")
            cv2.destroyWindow("Tire Sidewall Image")
            sys.exit()   
 
runProgram()

#hello testing
