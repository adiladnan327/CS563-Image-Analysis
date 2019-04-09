import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('E:\Images/building.pgm')

kernel = np.ones((5,5),np.float32)/25
median = cv2.medianBlur(image,5)
dst = cv2.filter2D(image,-1,kernel)

plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Average smoothing')
plt.xticks([]), plt.yticks([])
plt.show()
