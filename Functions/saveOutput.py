from pymongo import MongoClient
import urllib.parse
import datetime #current time for logging time

connection = MongoClient('mongodb://root:root@localhost:27017/')
db = connection['test']

def saveDocument(document):
    posts = db.posts
    posts.insert_one(document)

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }

saveDocument(post)
