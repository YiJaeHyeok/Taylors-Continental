# importing OpenCV library
import cv2 
  
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam_port = 0
cam = cv2.VideoCapture(cam_port)
  
# reading the input using the camera
result, image = cam.read()
  
# If image will detected without any error, 
# show result
if result:
  
    # showing result, it take frame name and image 
    # output
    #cv2.imwrite("GeeksForGeeks.png", image)
    cv2.imwrite("C:/Users/Jae/Desktop/Mongo/testPic/picTest.png", image)

    # If keyboard interrupt occurs, destroy image 
    # window
    cv2.destroyWindow("Tire Sidewall Image")
  
# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")
    