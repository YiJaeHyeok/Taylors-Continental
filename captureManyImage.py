import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

def startCamera():
    cam_on, image = cam.read()
    if not cam_on:
        print("No input from sensor")
        
    
    cv2.imshow("test", image)

startCamera()


img_counter = 0

cam_on, image = cam.read()
if not cam_on:
        print("No input from sensor")
        quit()

while True:
    

    cv2.imshow("test", image)

    k = cv2.waitKey(1)
    if k%256 == 27: #if press terminate from UI
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k%256 == 32: #change to when receive serial from Aduino
        # SPACE pressed
        img_name = "opencv_image_{}.png".format(img_counter)
        cv2.imwrite("C:/Users/Jae/Desktop/Mongo/testPic/picTest2%s.png" %img_counter, image)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

