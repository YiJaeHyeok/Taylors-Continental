from pymongo import MongoClient
from PIL import Image
import base64
import json
from json import dumps
#from django.http import HttpResponse

connection = MongoClient('mongodb://root:root@localhost:27017/')
db = connection['test']
posts = db.posts

def insert_image():
    with open("C:/Users/Jae/Downloads/firsttesttire.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    print (encoded_string)
    db.posts.insert_one({"image":encoded_string})
    #return HttpResponse("inserted")
#insert_image()

db.posts.remove()


'''
def retrieve_image():
    data = db.posts.find()
    data1 = json.loads(dumps(data))
    img = data1[0]
    img1 = img['image']
    decode=img1.decode()
    img_tag = '<img alt="sample" src="data:image/png;base64,{0}">'.format(decode)
    #return HttpResponse(img_tag)
    return img_tag

image_saved = retrieve_image()
'''