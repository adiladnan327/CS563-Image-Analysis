import cv2
import imageio
import matplotlib.pyplot as plt
import numpy as np



img = cv2.imread('E:\Images/MRI.pgm',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('E:\Images/strechedMRI.png',res)

plt.hist(img.ravel(),256,[0,256])
plt.show()

