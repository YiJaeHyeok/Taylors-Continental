from pymongo import MongoClient
import gridfs
from PIL import Image
import io
from datetime import datetime

connection = MongoClient('mongodb://root:root@localhost:27017/')
db = connection.Continental
col = db['Tire Information']
fscol = db['fs.files']
fs = gridfs.GridFS(db)

def loadImage(searchFileName):
    data = db.fs.files.find_one({'filename':searchFileName})
    imageID = data['_id']
    loadedImageBytes = fs.get(imageID).read()
    loadedImage = Image.open(io.BytesIO(loadedImageBytes))
    return loadedImage

def saveImageFromLocation(imageLocation, saveImageNameAs):
    imgae_data = open(imageLocation,"rb")
    imagebytes = imgae_data.read()
    imageID = fs.put(imagebytes, filename=saveImageNameAs)
    return imageID

def saveImage(image, saveImageNameAs):
    tireImageBytes = io.BytesIO()
    image.save(tireImageBytes,format='PNG')
    tireImageBytes=tireImageBytes.getvalue()

    imageID = fs.put(tireImageBytes, filename=saveImageNameAs)
    return imageID


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

def count():
    tireCount = fscol.count_documents({})
    return tireCount


def saveDocument(document):
    col.insert_one(document)







#saveImage("C:/Users/Jae/Downloads/firsttesttire.jpg",'finaltest1')

#testImage = loadImage('finaltest1')
#testImage.show()
    #loadedImage.show()

