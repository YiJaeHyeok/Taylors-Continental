# importing OpenCV library
import cv2 
  
def captureImage(folderDir):
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    pic_taken, image = cam.read()
    
    if pic_taken:
        
        route = folderDir + '/tireImage'
        cv2.imshow("Tire Sidewall Image", image)
        cv2.imwrite("C:/Users/Jae/Desktop/Mongo/testPic/picTest2.png", image)

        #cv2.waitKey(0)
        cv2.destroyWindow("Tire Sidewall Image")
        
    else:
        print("No image captured, Please try again")
        

captureImage('C:/Users/Jae/Desktop/Mongo/testPic')

