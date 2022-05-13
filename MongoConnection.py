from pymongo import MongoClient
import urllib.parse

connection = MongoClient('mongodb://root:root@localhost:27017/')
db = connection['test']
col = db['test']

#mydict = { "name": "Jae1", "address": "Highway 37" }
#collectionn.insert_one(mydict)

#item_details = collectionn.find()
#for item in item_details:
#    print(item)

import gridfs
tireInfo = gridfs.GridFS(db)

def saveImage():
    imageLocation = "C:/Users/Jae/Downloads/firsttesttire.jpg"
    #Open the image in read-only format.
    with open(imageLocation, 'rb') as tireImage:
        contents = tireImage.read()
    #Now store/put the image via GridFs object.
    tireInfo.put(contents, filename="image1")


'''
imageLocation = "C:/Users/Jae/Downloads/tiretest.png"
with open(imageLocation, 'rb') as tireImage:
    contents = tireImage.read()
tireInfo.put(contents, filename="image2")
'''

'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread('C:/Users/Jae/Downloads/firsttesttire.jpg')
plt.imshow(image)
plt.show()
'''


'''
importim = Image.open(r"C:/Users/Jae/Downloads/firsttesttire.jpg")
am = im
'''

'''
reading = db.tireInfo.files.find_one({'filename':'image1'})
my_id = data['_id']
'''