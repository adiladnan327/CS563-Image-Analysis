import cv2
import numpy as np
import matplotlib.pyplot as plt



img = cv2.imread('E:\Images/peppers.pgm',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('E:\Images/Strechedpeppers.png',res)


plt.hist(img.ravel(),256,[0,256])
plt.show()
