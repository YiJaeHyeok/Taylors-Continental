from pymongo import MongoClient
import gridfs
from PIL import Image
import io
from datetime import datetime

connection = MongoClient('mongodb://writeonly:writeonly@localhost:27017/?authMechanism=DEFAULT&authSource=Continental')
##connection = MongoClient('mongodb://localhost:27017/')
databaseCon = connection.Continental
tireInfoCollectionCon = databaseCon['TireInformation']
#imageCollectionCon = databaseCon['fs.files']
fs = gridfs.GridFS(databaseCon)

'''
def loadImageFromDB(searchFileName):
    data = databaseCon.fs.files.find_one({'filename':searchFileName})
    imageID = data['_id']
    loadedImageBytes = fs.get(imageID).read()
    loadedImage = Image.open(io.BytesIO(loadedImageBytes))
    return loadedImage
'''

def saveImageFromFile(imageLocation, saveImageNameAs):
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


def createDoc(imageID,TirePattern,TireSize,DOT):
    doc = {"imageID": imageID,
        "Department of Transportation": DOT,
        "Tire Pattern":TirePattern,
        "Tire Size":TireSize,
        "Tire Size and Pattern": "%s %s" %(TireSize,TirePattern),
        "Date captured": datetime.utcnow()
        #"Date captured": datetime.now().strftime("%Y%m%d_%H%M%S")

        }
    return doc

def countDoc():
    tireCount = tireInfoCollectionCon.count_documents({})
    return tireCount


def saveDoc(document):
    tireInfoCollectionCon.insert_one(document)



#saveDoc({"test1":123,"test2":234})



#saveImage("C:/Users/Jae/Downloads/firsttesttire.jpg",'finaltest1')

#testImage = loadImage('finaltest1')
#testImage.show()
    #loadedImage.show()

