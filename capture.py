import urllib.request
import cv2
import numpy as np
import time
flag = 0
URL = "http://192.168.0.103:8080/shot.jpg"
while True:
    flag += 1
    img_arr = np.array(
        bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2.imshow('IPWebcam', img)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
    if flag == 6:
        frame = img
        cv2.imshow("New", frame)
        time.sleep(5)

cv2.destroyAllWindows()
