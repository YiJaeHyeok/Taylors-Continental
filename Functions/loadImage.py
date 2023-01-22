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