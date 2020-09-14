def zer_mat(mat):
    row_mat = [False]*len(mat)
    col_mat = [False] * len(mat[0])
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if(mat[i][j]==0):
                row_mat[i]=True
                col_mat[j]=True
    for i in range(len(mat)):
        if(row_mat[i]):
            for j in range(len(mat[0])):
                mat[i][j] = 0
    for j in range(len(mat[0])):
        if(col_mat[j]):
            for i in range(len(mat)):
                mat[i][j]=0
    return(mat)

print(zer_mat([[1,1,2],[1,2,0]]))    
