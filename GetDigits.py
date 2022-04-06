import cv2
import PIL
import pytesseract
import imutils
import os
import numpy as np
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


#read image
image=cv2.imread('img1.jpeg')
#gray scale converion
grayIMG=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow("Gray-scale",grayIMG)
cv2.waitKey(0)


#blur the img(reduce noice)
blurIMG=cv2.bilateralFilter(grayIMG, 11,17,17)
cv2.imshow("Smoothed image",blurIMG)
cv2.waitKey(0)


#edge detection
edgedIMG=cv2.Canny(blurIMG,30,200)
cv2.imshow("Edges",edgedIMG)
cv2.waitKey(0)

#get the countours of whole image
cnts,new=cv2.findContours(edgedIMG.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
copyIMG=image.copy()
cv2.drawContours(copyIMG, cnts, -1, (0,255,0),3)
cv2.imshow("Countors",copyIMG)
cv2.waitKey(0)

#get first 30 countours depending on area from high to low
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:10]
copyIMG1=image.copy()
cv2.drawContours(copyIMG1, cnts, -1, (0,255,0),3)
cv2.imshow("Top 30 countours",copyIMG1)
cv2.waitKey(0)

location=None
for cnt in cnts:
    approx=cv2.approxPolyDP(cnt, 10, True)
    if(len(approx)==4):
        #get the contour
        location=cnt
        break
 
mask = np.zeros(grayIMG.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(image, image, mask=mask)
#crop the number plate

#x,y,w,h=cv2.boundingRect(location)
#cropIMG=grayIMG[y:y+h,x:x+w]

(x,y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropIMG = grayIMG[x1:x2+1, y1:y2+1]

cv2.imshow("Cropped image",cropIMG)
cv2.waitKey(0)


pytesseract.pytesseract.tesseract_cmd=r"C:\Users\ADMIN\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


digits = pytesseract.image_to_string(cropIMG)
print(digits)







