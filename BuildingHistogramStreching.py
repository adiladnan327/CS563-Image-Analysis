import cv2
import matplotlib.pyplot as plt
import numpy as np



img = cv2.imread('E:\Images/building.pgm',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) 
cv2.imwrite('E:\Images/strechedbuilding.png',res)

plt.hist(img.ravel(),256,[0,256])
plt.show()


