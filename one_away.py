def edit(array1,array2):
    diff = False
    if(len(array1)==len(array2)):
        for i in range(len(array1)):
            if(array1[i]!=array2[i]):
                if(diff):
                    return False
                diff = True
        return True
    elif((len(array2)-1==len(array1))):

        
        
        index1 = 0
        index2= 0 
        while((index1 < len(array1)) and (index2<len(array2))):
            print(index1,index2)
            if(array1[index1]!=array2[index2]):
                if(index1!=index2):
                    return False
                index2+=1
            else:
                index1+=1
                index2+=1
        return True
    elif((len(array1)-1)==len(array2)):
        
        array1,array2=swap(array1,array2)
        print(array1,array2)
        index1 = 0
        index2= 0 
        while((index1 < len(array1)) and (index2<len(array2))):
            if(array1[index1]!=array2[index2]):
                if(index1!=index2):
                    return False
                index2+=1
            else:
                index1+=1
                index2+=1
        return True

def swap(a1,a2):
    t = a1
    a1=a2 
    a2=t  
    return(a1,a2)


print(edit('pale','ple'))
            