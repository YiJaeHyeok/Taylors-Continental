import MongoConnection as mc
import loadSystemImage as lsi
import processingAlgorithms as pa
import OCR 
from random import *
import os.path
from time import sleep

#Requres update whenever image folder changes
folderDir = 'C:/Users/Jae/Desktop/Mongo/testPic'
filesDir = folderDir + '/*'
imageName = 'tmp'

def runSystem():
    while True:
        if len(os.listdir(folderDir)) == 0:
        #no fileg
            print("Waiting")
            sleep(3)
        
        else:
            print("Start main Program")
        
            #1) Load image location
            imageLoc = lsi.returnImageLoc(filesDir)

            #2) Save image into DB and retrieve unique key
            imageID = mc.saveImage(imageLoc, imageName)
            
        
            #3) Load image from file system
            image = lsi.loadImageFromFile(imageLoc)
        
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