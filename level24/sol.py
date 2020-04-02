import cv2
import numpy as np

img = cv2.imread("/Users/amitm/dev/personal/python-challange/level24/maze.png")

xStart = 0
yStart= 639

xEnd = 640
yEnd = 1

def isValidStep(arr):
    return not(all([x==255 for x in arr]))
def isValidCord(x):
    return x<=640 and x>=0
def isNewStep(path, x,y):
    return not((x, y) in path)
def isEmpty(x):
    return x==[]
def last(x):
    item = x.pop()
    x.append(item)
    return item

def solution(x,y,path):
    if(x==xEnd and y==yEnd):
        return path
    if(isValidCord(x+1) and isValidStep(img[x+1][y]) and isNewStep(path, x+1,y)):
        s = solution(x+1,y, path +[(x+1,y)])
        if(s):
            return s
    if(isValidCord(x-1) and isValidStep(img[x-1][y]) and isNewStep(path, x-1,y)):
        s = solution(x-1,y, path + [(x-1,y)])
        if(s):
            return s
    if(isValidCord(y+1) and isValidStep(img[x][y+1]) and isNewStep(path, x,y+1)):
        s = solution(x,y+1, path + [(x,y+1)])
        if(s):
            return s
    if(isValidCord(y-1) and isValidStep(img[x][y-1]) and isNewStep(path, x,y-1)):
        s = solution(x,y-1, path + [(x,y-1)])
        if(s):
            return s

def solution2():
    stack = [[(xStart,yStart)]]
    s = None
    while (not(s) and not(isEmpty(stack))):
        path = stack.pop()
        (x,y) = last(path)
        if(x==xEnd and y==yEnd):
            s = path
        if(isValidCord(y-1) and isValidStep(img[x][y-1]) and isNewStep(path, x,y-1)):
            stack.append(path + [(x,y-1)])
        if(isValidCord(y+1) and isValidStep(img[x][y+1]) and isNewStep(path, x,y+1)):
            stack.append(path + [(x,y+1)])
        if(isValidCord(x-1) and isValidStep(img[x-1][y]) and isNewStep(path, x-1,y)):
            stack.append(path + [(x-1,y)])
        if(isValidCord(x+1) and isValidStep(img[x+1][y]) and isNewStep(path, x+1,y)):
            stack.append(path +[(x+1,y)])

        #if(isValidCord(x+1) and isValidStep(img[x+1][y]) and isNewStep(path, x+1,y)):
        #    stack.append(path +[(x+1,y)])
        #if(isValidCord(x-1) and isValidStep(img[x-1][y]) and isNewStep(path, x-1,y)):
        #    stack.append(path + [(x-1,y)])
        #if(isValidCord(y+1) and isValidStep(img[x][y+1]) and isNewStep(path, x,y+1)):
        #    stack.append(path + [(x,y+1)])
        #if(isValidCord(y-1) and isValidStep(img[x][y-1]) and isNewStep(path, x,y-1)):
        #    stack.append(path + [(x,y-1)])
    return s

print("Start!")
sol = solution2()
sol_img = np.zeros([641,641],dtype=np.uint8)

for point in sol:
    if(not(all([x==0 for x in img[point]]))):
        sol_img[point] = 255
        img[point] = [0,255,0]
    else:
        sol_img[point] = 100
        img[point] = [255,0,0]

f = open("/Users/amitm/dev/personal/python-challange/level24/sol_tran_point.txt","w")
f.write(str(sol))
f.close()

#cv2.imshow("foo", sol_img)
#cv2.imshow("bar", img)
#cv2.waitKey(1000000000)
#cv2.waitKey(0)
cv2.imwrite("/Users/amitm/dev/personal/python-challange/level24/maze_sol_transpose.png",img)
cv2.imwrite("/Users/amitm/dev/personal/python-challange/level24/maze_sol2_transposes.png",sol_img)
