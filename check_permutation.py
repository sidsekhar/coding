from collections import defaultdict

def perma_check(array1,array2):
    
    len_a = len(array1)
    len_b = len(array2)

    if(len_a!=len_b):
        print(False)
    else:
        sorted_arr_1 = sorted(array1)
        sorted_arr_2 = sorted(array2)

        for i in range(len(array1)):
            if(sorted_arr_1[i]==sorted_arr_2[i]):
                continue
            else:
                print(False)




def perma_check_hash(array1,array2):

    new_dic = {}

    if(len(array1)!=len(array2)):
        print(False)
        return
    
    for i in range(len(array1)):
        if array1[i] in new_dic:
            new_dic[array1[i]]=new_dic[array1[i]]+1
        else:
            new_dic[array1[i]]=1
    
    for i in range(len(array2)):
        if array2[i] in new_dic:

            new_dic[array2[i]] = new_dic[array2[i]]-1
            
            if(new_dic[array2[i]]<0):
                print(False)
                return
        
           
    print(True)
            
        
perma_check_hash('yey','yye')



