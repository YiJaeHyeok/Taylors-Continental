from pymongo import MongoClient
import gridfs
from PIL import Image
import io
from datetime import datetime


connection = MongoClient('mongodb://root:root@localhost:27017/')
db = connection.test
col = db['test']

data = col.find_one()
imageID = data['ImageBytes :']

loadedImage = Image.open(io.BytesIO(imageID))
loadedImage.show()
