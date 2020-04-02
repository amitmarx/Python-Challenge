import zlib
import bz2

f = open('/Users/amitm/dev/personal/python-challange/level21/package.pack','rb')

x = f.read()

zlib = 0
zlibReverse = 0
bz2 = 0
bz2Revers = 0
def update(z=0 , zr=0, bz=0, bzr=0):
    #if(z==1 or zr == 1 or bz == 1 or bzr== 1):
    #    s = "zlib:" if zlib else ("zlibRevers" if zlibReverse else ("bz2" if bz2 else "bz2Revers"))
    #    print(s +"  "+ str(zlib + zlibRev + bz2+ bz2Revers))
    print("foo")
    zlib = z 
    zlibRevers = zr
    bz2 = bz
    bz2Revers = bzr

while True:
    try:
        try:
            x = zlib.decompress(x)
            #update(z = zlib+1)
        except:
            x = zlib.decompress(x[::-1])
            #update(zr = zlibRevers +1)
    except:
        try:
            try:
                x = bz2.decompress(x)
                #update(bz = bz2+1)
            except:
                x = bz2.decompress(x[::-1])
                #update(bzr=bz2Revers+1)
        except:
            f = open("/Users/amitm/dev/personal/python-challange/level21/result",'wb')
            f.write(x)
            break
            
    
