def compress(array):
    array2 = ''
    new_lis = []
    count = 0
    for i in range(len(array)):
        count+=1
        if((i+1==len(array)) or (array[i]!=array[i+1])):
            new_lis.append(array[i])
            new_lis.append(count)
            count=0
    if(len(new_lis)>len(array)):
        return(array)
    else:
        return(new_lis)

print(compress('aaasssssssssssssssssbbccc'))
            