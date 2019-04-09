import cv2
import imageio
import matplotlib.pyplot as plt

# Gamma encoding 
image = cv2.imread('E:\Images/MRI.pgm')
gamma = 2.2 # Gamma < 1 ~ Dark  ;  Gamma > 1 ~ Bright

gamma_correction = ((image/255) ** (1/gamma)) 
plt.figure(figsize = (5,5))
plt.imshow(gamma_correction)
plt.axis('off');
plt.show()
