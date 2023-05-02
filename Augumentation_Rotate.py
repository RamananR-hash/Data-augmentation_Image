from tkinter import filedialog
from tkinter import *
import cv2
import random
import os
ang=[cv2.ROTATE_90_COUNTERCLOCKWISE,cv2.ROTATE_180,cv2.ROTATE_90_CLOCKWISE]
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
try:
    folder=folder_selected.split('/')
    os.mkdir(folder[-1]+'_'+'Rotoate')
except:
    pass

arr = os.listdir(folder_selected)
print("Total number of images in a folder",len(arr))
for i in arr:
    print("Taking Image ",i)
    img=cv2.imread(folder_selected+"/"+i)
    val=random.randrange(0,3)
    img=cv2.rotate(img,ang[val])
    #cv2.imshow("RE", img)
    cv2.imwrite(folder[-1]+'_'+'Rotoate'+"/"+'Rotated_img_'+str(ang[val])+i,img)
    print("Image Rotated",i)
    cv2.waitKey(0)
