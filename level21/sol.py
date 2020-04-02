import zlib
import bz2

f = open('/Users/amitm/dev/personal/python-challange/level21/package.pack.zip','rb')
x = f.read()
for i in range(6):
    x = zlib.decompress(x)

f = open("/Users/amitm/dev/personal/python-challange/level21/zlib_out",'wb')
f.write(x)
f = open("/Users/amitm/dev/personal/python-challange/level21/bzoutput","wb")
for i in range(3):
    x = bz2.decompress(x)
f.write(x)

i=0
for i in range(10):
    x = zlib.decompress(x)

f = open("/Users/amitm/dev/personal/python-challange/level21/3time",'wb')
f.write(x)
