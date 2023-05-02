# frame = imutils.resize(frame, width=400)

import imutils
from tkinter import filedialog
from tkinter import *
import cv2
import random
import os
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
try:
    folder=folder_selected.split('/')
    os.mkdir(folder[-1]+'_'+'Scale')
except:
    pass

arr = os.listdir(folder_selected)
print("Total number of images in a folder",len(arr))
for i in arr:
    print("Taking Image ",i)
    img=cv2.imread(folder_selected+"/"+i)
    val=random.randrange(-2,1)
    img = imutils.resize(img, width=500,height=500)
    #cv2.imshow("RE", img)
    cv2.imwrite(folder[-1]+'_'+'Scale'+"/"+'Scale_img_'+str(val)+i,img)
    
    print("Image Scaled",i)
    cv2.waitKey(0)
