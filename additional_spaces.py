def urily(array,arr_len):
    
    sp = 0
    array_lis = list(array)
    
    for i in range(arr_len):
        if(array_lis[i]== ' '):
            sp+=1
    extra = arr_len + sp*2

    for i in range(extra,0,-1):
        if(array_lis[i]== ' '):
            array_lis[i] = '%'
            array_lis[i+1] = '2'
            array_lis[i+2] = '0'
        else:
            array_lis[i] = array_lis[i]

MAX = 100
def replaceSpaces(string): 
      
    # Remove remove leading and trailing spaces 
    string = string.strip() 
  
    i = len(string) 

  
    # count spaces and find current length 
    space_count = string.count(' ') 
  
    # Find new length. 
    new_length = i + space_count * 2
  
    # New length must be smaller than length 
    # of string provided. 
    if new_length > MAX: 
        return -1
  
    # Start filling character from end 
    index = new_length - 1
  
    string = list(string) 
        # Fill string array 
    
    for f in range(i, new_length): 
        string.append('0') 
    

    # Fill rest of the string from end 
    for j in range(i-1, 0, -1): 
        # inserts %20 in place of space 
        if string[j] == ' ': 
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index = index - 3
        else: 
            string[index] = string[j] 
            index -= 1
    
    return ''.join(string) 

print(replaceSpaces('Mr John'))
        