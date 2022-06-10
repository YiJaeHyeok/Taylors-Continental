import os.path
from time import sleep
import loadSystemImage as lsi

#folderDir = 'C:/Users/Jae/Desktop/Mongo/testPic/'

def checkFileExists(imageLocation):
    if len(os.listdir(imageLocation)) == 0:
        #no file
        print("Waiting")
        sleep(5)
    else:
        print("Start main Program")
        lsi.removePicInFolder()
        sleep(3)
        print("Done")
        
while True:
    checkFileExists()


#print(os.listdir(folderDir)[0])

