from pymongo import MongoClient
import gridfs

connection = MongoClient('mongodb://root:root@localhost:27017/')
db = connection.test
fs = gridfs.GridFS(db)

def saveDocument(document):
    db.insert_one(document)