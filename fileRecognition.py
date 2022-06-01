import os.path
from os import path
from time import sleep
import loadSystemImage as lsi

folderDir = 'C:/Users/Jae/Desktop/Mongo/testPic/'

def checkFileExists():
    if len(os.listdir(folderDir)) == 0:
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

