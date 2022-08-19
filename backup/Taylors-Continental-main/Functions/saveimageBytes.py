from pymongo import MongoClient
import gridfs
from PIL import Image
import io
from datetime import datetime
import cv2
from PIL import Image as im


connection = MongoClient('mongodb://root:root@localhost:27017/')
db = connection.test
col = db['test']

def saveImage(image, saveImageNameAs):
    tireImageBytes = io.BytesIO()
    image.save(tireImageBytes,format='PNG')
    tireImageBytes=tireImageBytes.getvalue()

    #imageID = fs.put(tireImageBytes, filename=saveImageNameAs)
    #return imageID


def createDocument(imageID,TirePattern,TireSize,DOT):
    doc = {"imageID": imageID,
        "Department of Transportation": DOT,
        "Tire Pattern":TirePattern,
        "Tire Size":TireSize,
        "Tire Size and Pattern": "%s %s" %(TireSize,TirePattern),
        "Date captured": datetime.utcnow()
        #"Date captured": datetime.now().strftime("%Y%m%d_%H%M%S")

        }
    return doc

def saveDocument(document):
    col.insert_one(document)


cam = cv2.VideoCapture(0)

while True:
    cam_on, image = cam.read()
    if not cam_on:
        print("No input from sensor")
        quit()
    cv2.imshow("Tire Sidwall Reader",image)

            #1) Take Image
    k = cv2.waitKey(1)

    signal = ''

    if k%256 == 32: #change to when receive serial from Aduino
                   
            #img_counter += 1
            ### Change the name of one field to unique
        tireImage = im.fromarray(image)
        tireImageBytes = io.BytesIO()
        tireImage.save(tireImageBytes,format='PNG')
        tireImageBytes=tireImageBytes.getvalue()
        
        import random
        
        doc = {"imageID": int(100*random.random()),
        "Department of Transportation": int(100*random.random()),
        "Tire Pattern":int(100*random.random()),
        "Tire Size":int(100*random.random()),
        "Date captured": int(100*random.random()),
        "ImageBytes :" : tireImageBytes
        #"Date captured": datetime.now().strftime("%Y%m%d_%H%M%S")
        }
        
        saveDocument(doc)    
        
            #2) Save image into DB and retrieve unique key
    elif k%256 == 27: #if press terminate from UI
     
        # ESC pressed
            print("Escape hit, closing...")
            cv2.destroyWindow("Tire Sidewall Reader")
            quit()     





#saveImage("C:/Users/Jae/Downloads/firsttesttire.jpg",'finaltest1')

#testImage = loadImage('finaltest1')
#testImage.show()
    #loadedImage.show()

