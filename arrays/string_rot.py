def substring(s1,s2):
    if(s1.find(s2)==-1):
        return(False)
    else:
        return(True)

def rotation(s1,s2):

    if((len(s1)==len(s2)) and len(s1)>0 ):

        new_s1 = s1+s1 

        print(substring(new_s1,s2))


rotation('waterbottl','erbottewat')