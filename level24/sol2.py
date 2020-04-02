import zlib
import pickle

lines = open('rgb.txt').readlines()
reds= [line.split(', ')[-1] for line in lines]
noZeros = [int(x) for x in reds][1::2]
print(noZeros)
data = bytes(noZeros)
f = open("sol.zip",'wb')
f.write(data)
f.close()
f = open("sol.zip","rb")
#output = zlib.decompress(data)
output = pickle.load(f)
print(output)
