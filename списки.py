#n = list(range(10))
#m = []
#for i in n:
#    if i == 8:
#        continue
#    m += [i]
#else:
#    print[m]


x = [9,8,7,6,5]
x.append(4)  # добавляет элемент в конец списка


x.append(4)  # добавляет элемент в конец списка
x.insert(1, 7)     # вставляет элемент по указанному индексу
print (x.count(7))   # сколько одинаковых элементов 7 списке
x.sort ()  # сортировка по возрастанию
x.reverse() # сортировка  по убыванию
y =x.pop(0) # удалить значение с списка с индексо 0 и присвоить переменной У, без аргументв удалается последний элемент.
x.remove(7) # удалить 1 элемент с конкретным значением если два то второй элемент останется
x.clear() # полностью очищает список
x.extend ({"a","s"})# добавить в конец списка значение с другого списка
h= x.copy() # копировать список
b= n.copy()

#  или b = n[start:stop:step:]
b=n[::]


#m= [1,2,1,3,5,"a",[1,2],["s","f"]]

#print(m[-1][0])


m= [[5,6] ,[1,2], ["s","f"]]

m[0]= 9

#print(len(m[0])) # длина списка 0 =2
#print(len(m)) # длина общего списка 
print (m)
m[0]= m[0]+2
print (m)

m[1], m[2] = m[2], m[1]
print (m)

m = m+[7]
print (m)

n= list("stroka")

print (n)

n = list(range(10))





n = list(range(1,21))
#b=n.copy()
#  или b = n[start:stop:step:]
b=n[::]
m = []
for i in n:
    if i %2 == 0:
        m.append(i)    # добавить
        n.remove(i)    # убрать 
  
else:
    print(m)
    print(n)
    print (b)

    # №##индекс  с индексом  (-1) последний элемент 
    print (m[-1][0])


    def exclusive_itrm(*args, key= False):
    new_list=[]
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key== True:
        new_list.sort()       

    return new_list




z=[9,8,7]
x=[8,8,9,7,6,5]
c=[1,2,3,4,5,6,7,7]
t =exclusive_itrm(z,x,c,key= True)
print(t)