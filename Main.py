from warnings import filters
import GetNoPlate as g
import cv2
import Info as info
import Sendsms as sendmsg
import time
import urllib.request
import cv2
import numpy as np
import time

#Capture vehicle
URL = "http://192.168.43.93:8080/shot.jpg"

while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
    
    #Get digits
    rawdigits=g.getNoPlate(img)

    if rawdigits=="":
        print("Technical error : No Detection !!")
    else:
        #Get digits in formatted form
        numberp=''.join(char for char in rawdigits if char.isalnum())
        print(numberp)

        #Get info 
        ownerName,mobileno=info.checkInfo(numberp)

        #check error possibilities
        if(ownerName=="noDB"):
            print("Records are not found")

        elif(ownerName=="noScrap"):
            print("Scrapping not required.")

        else:
            #send sms 
            sendmsg.sms(numberp,ownerName,mobileno)
    time.sleep(10)
    print("Done.......!")
        


    

