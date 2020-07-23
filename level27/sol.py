import imageio

gif = imageio.get_reader('zigzag.gif')
frame = gif.get_data(0)
rows,cols = frame.shape

solution=[[] for i in range(rows+cols-1)]
matrix = frame
for i in range(rows):
    for j in range(cols):
        sum=i+j
        if(sum%2 ==0):

            #add at beginning
            solution[sum].insert(0,matrix[i][j])
        else:

            #add at end of the list
            solution[sum].append(matrix[i][j])


# print the solution as it as
for i in solution:
    for j in i:
        print(j,end=" ")

