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




вызов функции из функции


import math

PI= math.pi

def radius():
    n = float(input("диаметр цилиндра в см"))
    n /=2
    return n

def height():
    m= float(input('высота цилиндра в см'))
    return m

def volume():
    r = radius()
    h = height()
    s= PI*r**2
    v = s*h
    return v


#print("обьем цилиндра ", volume()," см3")

def massa (g):
     n= float(input('удельный вес г/см/3 '))
     return g*n/1000

print ("вес цилиндра", massa(volume()))  

Функция pow()

ункция pow() возводит число в степень. Она принимает 
два параметра: какое число возводить и в какую степень в
озводить. Если вызывать pow() без параметров, то Python выдаст 
следующее: "TypeError: pow expected at least 2 arguments, got 0". Интерпретатор сообщает, что функция ожидает два параметра, а вы вызвали ее без них.

Функция pow() всегда имеет два 
обязательных параметра, поэтому ее
 невозможно вызвать с другим количеством параметров.


Функция round()
Рассмотрим функцию round(), которая округляет переданное ей число:

result = round(10.25, 0)  # 10.0
Мы передали в нее два параметра:

Число, которое нужно округлить
Точность округления
0 означает, что округление будет до целого значения. Чаще всего нужно округлять именно до целого числа, а не до десятых. Поэтому создатели функции round сделали второй параметр необязательным и задали ему внутри функции значение по умолчанию 0. Значит, можно не указывать второй параметр, а результат будет тем же:

result = round(10.25)  # 10.0
А если нужна другая точность, то можно передать параметр:

# округление до одного знака после запятой
result = round(10.25, 1)  # 10.2
Если функция в Python принимает необязательные аргументы, то они всегда стоят после обязательных. Их количество может быть любым. Это зависит от самой функции, но они всегда идут рядом и в конце списка аргументов.

