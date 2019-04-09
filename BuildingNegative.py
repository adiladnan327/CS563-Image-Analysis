import cv2
import imageio
import matplotlib.pyplot as plt

import matplotlib.cbook


 

image = cv2.imread('E:\Images/Building.pgm')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
negative = 255 - image 

plt.figure(figsize = (6,6))
plt.imshow(negative);
plt.axis('off')
plt.show()





