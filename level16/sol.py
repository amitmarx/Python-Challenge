import imageio
import numpy as np
import cv2
img = imageio.mimread("mozart.gif")[0]
imgNew = imageio.mimread("mozart.gif")[0]
indexes = []
print(img[0,0])
for row in range(480):
    for col in range(640):
        (r,g,b,_) = img[row,col]
        if(r==255 and g==255 and b==255):
            imgNew[row, 0:(640-col)] = img[row, col:]
            imgNew[row, (640-col):] = img[row,0:col]
            continue

# sortedArr = sorted(indexes, key=lambda item: item[1])

# newImage = np.zeros([480,640,4],np.uint8)
# index=0
# for [row,_] in sortedArr:
#  newImage[index] = img[row]
#  index+=1

cv2.imshow('foo', imgNew)
cv2.waitKey(500000000)
