# переменные
 
num1, num2, num22 = 1, 5, 44
print (num1, num2, num22)


 
num1, num2, num22 = 1, 5, 44
print (num1, num2, num22)
num2,num1 =num1,num2
print (num1, num2, num22)
a= (23, 445, 56, 66, 77)
num2,num1 =num1,num2+num22
print (num1, num2, num22)
 
a,b,c,d,e = (23, 445, 56, 66, 77)
print(a,b,c,d,e)
 
a,b, *c, d= (23, 445, 56, 66, 77)
print(a,b,c,d)
 
#типы данных

a= 5
a= "5"
x = input ('введите число')
print (type (x))


x = float(input ('введите число '))
y = float(input ('введите число '))
# r = int(x) +5   # целое 
# r = float(x)+5    # с плавающей точкой
r = x+y
print ("result =" + str(r))


условия

if True:
    print ('if')
elif True:
    print("elif")
else:
    print ("else")         

if False:
    print ('if')
elif True:
    print("elif")
else:
    print ("else")         

if False:
    print ('if')
elif False:
    print("elif")
else:
    print ("else")         




x=[1,2]

if x==0:
    x=1
    print("x равно 0")
elif type (x) == type(5) or type (x) == type(5.5):  # в скобки вводим любые числа 5 проверка на целое 5.5 проверка на дробное
    print ("x допустимое значение")
else:
    print("х недопустимый тип данных ")
    x=1          
and  и и 
not не





print(100/x)


import http
import os




import os

while True:
    sayt = input("Введите адрес сайта \n")    # \n  перенос строки
    if sayt == "завершить":
        break

    if "https://" in sayt:
        os.system ("start " + sayt)
        print("if")
    elif "www." in sayt:
        sayt= "https://" +sayt
        os.system ("start "+ sayt)
    else:
        sayt= "https://www." + sayt
        os.system("start "+ sayt)
        print ("else")



import time
time.sleep(5) задержка 5 сек 

import os

os.startfile("c://program files/......ink.exe")


while 


while True:
    x = int(input ('введите число '))
    count =0
    y=1
    while count<x:
        count+=1
        y= y*count
  
    else:
        print(y)


 x= ""

while len(x)<5:
    y= input("Ввод данных ")
    if y=="o":
        continue  #возрашает цикл назад  ? прерывает итерацию..
    if y=="1":
        break  # прерывает цикл и не выполняет else
    x += y
else:
    print(x) 

print("программа работает дальше")      




m= "stroka text"
count =0
for i in m:

    if i =="t":
        print("В строке есть t")
        count+=1
    if i == "e":
        break     

else:
    print("цикл завершен. букв т", count)    

print("ПРограмма работает дальше")    




m= "stroka text"
count =0
for i in m:

    if i =="t":
        continue 
        print("В строке есть t")
        count+=1
    print(i)    
               

else:
    print("цикл завершен. букв т", count)    

print("ПРограмма работает дальше")   


from itertools import count


x= "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
y = input("Введите строку:\n")


for i in x:
    count=0
    for r in y:
        if i == r:
            count +=1
    if count >0:        
        print("букв", i, "было", count)        


range

# for x in range(1,10,2):
for x in range(10,-10,-2):

    print(x)


n = list(range(10))
m = []
for i in n:
    if i == 8:
        continue
    m += [i]
else:
    print(m)
