from PIL import Image
import glob
import os

folderDir = 'C:/Users/Jae/Desktop/Mongo/testPic/*'

def returnImageLoc(folderLocation):
    for filename in glob.glob(folderLocation): 
        return filename
        break
    
def loadImageFromFile(imageLocation):
    image = Image.open(imageLocation) 
    return image

def closeImage(image):
    image.close()

def removePicInFolder(imageLocation):
    picDir = glob.glob(imageLocation)
    for pic in picDir:
        os.remove(pic)
        break

#print(returnImageLoc(folderDir))

# order: load -> extract -> save image -> save text (including id from image)

#testimage = loadImageFromFile()
#testimage.show()