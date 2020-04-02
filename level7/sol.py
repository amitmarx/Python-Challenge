import cv2

img = cv2.imread('oxygen.png',0)
rows, cols = img.shape
ls=[105, 10, 16, 101, 103, 14, 105, 16, 121]
i=0
for x in range(rows):
    for y in range(cols):
        if(img[x,y]==ls[i]):
            img[x,y]=0
            i= (i+1) % len(ls)
            cv2.imshow('123',img)

cv2.waitKey(0)
