import gif2numpy
import numpy as np
import cv2
np_frame,extenstions, image_spec = gif2numpy.convert("white.gif")
#for fram in np_frame:
s=""
l=""
board = np.zeros(shape=(100,100,3))
x=50
y=50
i=0
boards = []
for frame in np_frame:
    out = False
    for row, r in zip(frame, range(len(frame))):
        for col, c in zip(row, range(len(row))):
            if(not(out) and all(x == 8 for x in col)):
                if(r==100 and c==100):
                    i+=1
                    boards.append(board)
                    board = np.zeros(shape=(100,100,3))
                    x=50
                    y=50
                    out = True
                if(r==100 and c==102):
                    x+=1
                if(r==102 and c==100):
                    y+=1
                if(r==102 and c==102):
                    x+=1
                    y+=1
                if(r==98 and c==100):
                    y-=1
                if(r==98 and c==102):
                    y-=1
                    x+=1
                if(r==98 and c==98):
                    y-=1
                    x-=1
                if(r==100 and c==98):
                    x-=1
                if(r==102 and c==98):
                    x-=1
                    y+=1
                board[y][x] = [255,255,255]

boards.append(board)

for board, i in zip(boards, range(len(boards))):
    cv2.imshow(str(i), board)

cv2.waitKey(1000000000)

