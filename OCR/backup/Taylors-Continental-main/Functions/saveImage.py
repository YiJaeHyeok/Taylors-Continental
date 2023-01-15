from pymongo import MongoClient
import gridfs
connection = MongoClient('mongodb://root:root@localhost:27017/')
db = connection.test
fs = gridfs.GridFS(db)

def saveImage(imageLocation, saveImageNameAs):
    file_data=open(imageLocation,"rb")
    data = file_data.read()
    imageID = fs.put(data, filename=saveImageNameAs)
    return imageID