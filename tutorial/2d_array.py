#2d_array in python

arr = [[1,5], [2,5], [3,4]]

for i in range(len(arr)):
    for j in range (len(arr[i])):
        print(arr[i][j])

#use row
for row in arr:
    for column in row:
        print(column)