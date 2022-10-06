
# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

stroka="4 5 6 7 10 9"

result= stroka.split(" ")
print(result)



def sort(strol):
    res=[]
    for i in range(len(strol)-1):
        if int(strol[i-1])==int(strol[i])-1:
            res.append(strol[i])
        strol=res
    return strol   

zz=map(sort,stroka)

# print(sort(result))
print(list(zz))

