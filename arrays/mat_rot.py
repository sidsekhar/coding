def rot_clock(mat):
    n = len(mat)
    print(len(mat)//2)
    for layer in range(len(mat)//2):
        first = layer
        last = n-1-layer

        for i in range(first,last,1):
            offset = i - first 
            top = mat[first][i]

            mat[first][i] = mat[last-offset][first]

            mat[last-offset][first] = mat[last][last-offset]

            mat[last][last-offset] = mat[i][last]

            mat[i][last] = top
    return(mat)

    
print(rot_clock([[1,2,3,10],[4,5,6,90],[7,8,9,77],[23,22,34,56]]))