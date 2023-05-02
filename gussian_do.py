import cv2
import numpy
import os
try:
    os.mkdir("Class_2_Gussian")
    os.mkdir("Class_3_Gussian")
    os.mkdir("Class_4_Gussian")
except:
    pass
arr = os.listdir('class4')


for i in arr:
    print("Taking Image  .",i)
    img=cv2.imread("class4/"+i)
    img=cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)

    #cv2.imshow('image',img)
    cv2.imwrite('Class_4_Gussian/'+i,img)
    cv2.waitKey(0)
'''
img=cv2.imread("class0/"+arr[0])
img=cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)

cv2.imshow('image',img)
cv2.imwrite("test1.png",img)
cv2.waitKey(0)
'''