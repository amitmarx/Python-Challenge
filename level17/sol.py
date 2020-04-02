import difflib
import numpy as np
import cv2
s = open('sFile').readlines()
f = open('fFile').readlines()

f1 = open("f1.png", "wb")
f2 = open("f2.png", "wb")
def removeChars(x):
    return x.replace('\n','').replace('+','').replace('-','')

def removeChar(s,x):
    return s.replace(x,'')

s = list(map(lambda x: removeChars(x), s))
f = list(map(lambda x: removeChars(x), f))
print(type(s[0]))

diff = difflib.ndiff(f, s)
diffList = []
for i in diff:
    if(('-' in i)):
        removeExtraChars = removeChars(i[2:])
        if(removeExtraChars != ''):
            bs = bytes([int(o, 16) for o in removeExtraChars.strip().split(" ") if o])
            f1.write(bs)

def show_img(list1, idx1):
    img = np.zeros([len(list1), 18], dtype=np.uint8)
    idx = 0
    for line in list1:
        split_line = [np.int8(int(val, 16)) for val in line.split(' ')]
        if len(split_line) < 18:
            continue
        img[idx, :] = np.array(split_line)
        idx += 1

    cv2.imshow('ds{0}'.format(idx1), img.transpose())

print(diffList)
show_img(diffList,1)

cv2.waitKey(0)
