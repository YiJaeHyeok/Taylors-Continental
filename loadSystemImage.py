from PIL import Image
import glob
import os

folderDir = 'C:/Users/Jae/Desktop/Mongo/testPic/*'

def returnImageLoc():
    for filename in glob.glob(folderDir): 
        tmp = filename
        break
    return filename

def loadImageFromFile():
    image = Image.open(returnImageLoc()) 
    return image

def removePicInFolder():
    picDir = glob.glob(folderDir)
    for pic in picDir:
        os.remove(pic)
        break

# order: load -> extract -> save image -> save text (including id from image)
removePicInFolder()

#testimage = loadImageFromFile()
#testimage.show()