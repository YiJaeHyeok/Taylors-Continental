from PIL import Image
import glob

def loadImageFromFile(imageLocation):
    image = Image.open(imageLocation) 
    return image


def returnImageLoc(folderLocation):
    for filename in glob.glob(folderLocation): 
        return filename
        break

def closeImage(image):
    image.close()

#Requres update whenever image folder changes
folderDir = 'C:/Users/Jae' #Folder Directory
filesDir = folderDir + '/*'
imageName = 'tmp'

            #1) Load image location
imageLoc = returnImageLoc(filesDir)
        
            #2) Load image from file system
image = loadImageFromFile(imageLoc)


#after preprocessing
image.close()