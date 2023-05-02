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
    os.mkdir(folder[-1]+'_'+'Flip')
except:
    pass

arr = os.listdir(folder_selected)
print("Total number of images in a folder",len(arr))
for i in arr:
    print("Taking Image ",i)
    img=cv2.imread(folder_selected+"/"+i)
    val=random.randrange(-2,1)
    img=cv2.flip(img,val)
    #cv2.imshow("RE", img)
    cv2.imwrite(folder[-1]+'_'+'Flip'+"/"+'flip_img_'+str(val)+i,img)
    
    print("Image flipped",i)
    cv2.waitKey(0)
