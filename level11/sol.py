file_size = len(open('evil2.gfx','rb').read())
file = open('evil2.gfx','rb')
file1 = open('1.gfx','wb')
file2 = open('2.gfx','wb')
file3 = open('3.gfx','wb')
file4 = open('4.gfx','wb')
file5 = open('5.gfx','wb')
files = [file1,file2,file3,file4,file5]
for i in range(file_size):
    files[i%5].write(file.read(1))

["disproportional