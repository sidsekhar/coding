def check(array):
    table = [0]*256
    count=0
    for i in array:
        table[ord(i)]+=1
    
    for i in range(len(table)):
        if(table[i]%2==1):
            count+=1
    print(count<=1)


check('alayalam')