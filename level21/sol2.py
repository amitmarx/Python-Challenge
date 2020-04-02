import zlib
import bz2

f = open('/Users/amitm/dev/personal/python-challange/level21/package.pack','rb')

x = f.read()

s=""
while True:
    try:
        try:
            x = zlib.decompress(x)
            s = s+ "z"
        except:
            x = zlib.decompress(x[::-1])
            s = s+"\n"
    except:
        try:
            try:
                x = bz2.decompress(x)
                s = s+" "
            except:
                x = bz2.decompress(x[::-1])
                s = s+"\n"
        except:
            f = open("/Users/amitm/dev/personal/python-challange/level21/result",'wb')
            f.write(x)
            break
        
print(s)
