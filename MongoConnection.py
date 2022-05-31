from pymongo import MongoClient
import gridfs
from PIL import Image
import io

connection = MongoClient('mongodb://root:root@localhost:27017/')
db = connection.test
fs = gridfs.GridFS(db)

def loadImage(searchFileName):
    data = db.fs.files.find_one({'filename':searchFileName})
    imageID = data['_id']
    loadedImageBytes = fs.get(imageID).read()
    loadedImage = Image.open(io.BytesIO(loadedImageBytes))
    return loadedImage

def saveImage(imageLocation, saveImageNameAs):
    file_data=open(imageLocation,"rb")
    data = file_data.read()
    imageID = fs.put(data, filename=saveImageNameAs)
    return imageID

def saveDocument(document):
    db.insert_one(document)


#saveDocument(post)
'''
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }
'''

#saveImage("C:/Users/Jae/Downloads/firsttesttire.jpg",'finaltest1')

#testImage = loadImage('finaltest1')
#testImage.show()
    #loadedImage.show()

