def unique(arrays):
    sorted_array = sorted(arrays)

    for i in range(len(sorted_array)-1):
        if(sorted_array[i]==sorted_array[i+1]):
            print(False)
            break

def unique_extra_ds(arrays):

    new_array = [0]*256

    for i in range(len(arrays)):

        ascii_val = ord(arrays[i])
        
        if(new_array[ascii_val]==True):
            print(False)
        
        new_array[ascii_val]=True


unique_extra_ds('shius')


