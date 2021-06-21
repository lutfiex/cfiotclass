import cv2
import urllib.request
import numpy as np
##########################

url = 'http://140.118.115.181:1111/cam-lo.jpg'
#cv2.namedWindow('s',cv2.WINDOW_AUTOSIZE)
#print("Before URL")

while True:
    imgResponse=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)
    #print('About to show frame of Video.'
    cv2.imwrite("capture/Capturing.jpg",img)
    #print('Running..')
    break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("Capturing.jpg",img)
        break

cap.release()
cv2.destroyAllWindows()