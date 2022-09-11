from tkinter import ARC


def count_list(par):
    count =0
    for i in par:
        count+=1
    return count


jj = [9,8,7,6]

h= ["a","v","r"]


print (count_list(jj))



def count_list(par,count=0):
    
    count =0
    for i in par:
        count+=1
    return count


jj = [9,8,7,6]

h= ["a","v","r"]


print (count_list(h))



def count_list(par,par2=False,count=0):

    if par2== True:
        typ= type(par[0])
        for i in par:
            count+=1
        return count,typ    
    for i in par:
        count+=1
    return count


jj = [9,8,7,6]

h= ["a","v","r"]


#print (count_list(h))   #можно так 
print (count_list(h, True, count= -1))  #можно указать прямо

ARC

def name(h,g,*args, key):
    print(h)
    print(g)
    print(args)
    print(key)

name(7,8,9,10,4, key=10)    


