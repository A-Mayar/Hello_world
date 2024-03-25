import cv2

CAMERA = cv2.VideoCapture(0)
cv2.namedWindow("'C' to Capture Image 'X' to close webcame")

NO_OF_IMAGES = 0

while True:
    ret, frame = CAMERA.read()
    
    if not ret:
        print('Failed to grab camera')
        break
    
    cv2.imshow('TESTING FRAME', frame)
    
    if cv2.waitKey(1) == ord('x'):
        print("CLOSING THE CAMERA")
        break
    
    if cv2.waitKey(1) == ord('c'):
        img = cv2.imwrite('src/main/resources/static/CAPTURED_IMAGE.jpg',frame)
        print('Captured an Image!!!')
        CAMERA.release()
        
        NO_OF_IMAGES += 1

    
    
img__ = cv2.imread('src/main/resources/static/CAPTURED_IMAGE.jpg', -1)
cv2.imshow('Captured image....',img__)   
cv2.waitKey(0)
cv2.destroyAllWindows()
        
    
