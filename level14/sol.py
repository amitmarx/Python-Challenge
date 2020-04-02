import cv2
import numpy as np
img = cv2.imread("wire.png",cv2.IMREAD_COLOR)
blank_image = np.zeros((100,100,3), np.uint8)

lengths = [100]

for i in range(99,0,-1):
    lengths.append(i)

currentIndex=0
indexes = [0,99,99,]
for length in length:
    if(iterations%4==0):
        img[0:length] = img[currentIndex:lengths]

    currentIndex+=length


