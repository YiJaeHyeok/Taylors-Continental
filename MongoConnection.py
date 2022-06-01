from pymongo import MongoClient
import gridfs
from PIL import Image
import io
import datetime

connection = MongoClient('mongodb://root:root@localhost:27017/')
db = connection.test
col = db['test']
fs = gridfs.GridFS(db)

def loadImage(searchFileName):
    data = db.fs.files.find_one({'filename':searchFileName})
    imageID = data['_id']
    loadedImageBytes = fs.get(imageID).read()
    loadedImage = Image.open(io.BytesIO(loadedImageBytes))
    return loadedImage

def saveImage(imageLocation, saveImageNameAs):
    imgae_data = open(imageLocation,"rb")
    image = imgae_data.read()
    imageID = fs.put(image, filename=saveImageNameAs)
    return imageID

def createDocument(a,b,c,d):
    doc = {"author": a,
        "text": b,
        "tags": [c, d],
        "date": datetime.datetime.utcnow()
        }
    return doc

def saveDocument(document):
    col.insert_one(document)







#saveImage("C:/Users/Jae/Downloads/firsttesttire.jpg",'finaltest1')

#testImage = loadImage('finaltest1')
#testImage.show()
    #loadedImage.show()

