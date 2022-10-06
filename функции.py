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




# вызов функции из функции


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

# Функция pow()

# ункция pow() возводит число в степень. Она принимает 
# два параметра: какое число возводить и в какую степень в
# озводить. Если вызывать pow() без параметров, то Python выдаст 
# следующее: "TypeError: pow expected at least 2 arguments, got 0". Интерпретатор сообщает, что функция ожидает два параметра, а вы вызвали ее без них.

# Функция pow() всегда имеет два 
# обязательных параметра, поэтому ее
#  невозможно вызвать с другим количеством параметров.


# Функция round()
# Рассмотрим функцию round(), которая округляет переданное ей число:

result = round(10.25, 0)  # 10.0
# Мы передали в нее два параметра:

# Число, которое нужно округлить
# Точность округления
# 0 означает, что округление будет до целого значения. Чаще всего нужно округлять именно до целого числа, а не до десятых. Поэтому создатели функции round сделали второй параметр необязательным и задали ему внутри функции значение по умолчанию 0. Значит, можно не
#  указывать второй параметр, а результат будет тем же:

result = round(10.25)  # 10.0
# А если нужна другая точность,
#  то можно передать параметр:

# округление до одного знака после запятой
result = round(10.25, 1)  # 10.2
# Если функция в Python принимает необязательные аргументы, то они всегда стоят после обязательных. Их количество может быть любым. Это зависит от самой функции, 
# но они всегда идут рядом и в конце списка аргументов.



def truncate(text, length):
    # BEGIN
    result = f"{text[0:length]}..."
    return result
    # END


    numcard = "1234144423415552341234"
 

def get_hidden_card(card_number, stars_count=4):
    visible_digits = card_number[-4:]
    return f'{"*" * stars_count}{visible_digits}'

print(get_hidden_card(numcard))



def has_upper_case(text):
    return text != text.lower() # проверка на нижний регистр




# удалить символ не зависимо от регистра
    
def filter_string(strin,char):
    res=''
    for i in strin:
        if i == char.lower() or i== char.upper():                       
            strin = strin.replace(char.lower(), '')
            strin = strin.replace(char.upper(), '')
            
        
    return strin


print(filter_string("If I looL forward I win","l"))        


Как работать с модулем time:
```
import time

x = time.time()
print(x)

# получаем число типа float - сколько секунд прошло с 01.01.1970 (начало эпохи Unix)
# 1662783075.0398953
# x =time.time_ns()
# print(x)

# получаем число типа int - наносекунды от 01.01.1970
# 1662783075039899938
# ```


import time
from tkinter import Y
x= time.time_ns()
y= time.time()
print(x,y) 


isinstance(i, float)   #проверяет тип объекта
isinstance(i, int)

if isinstance(i, float):
    
    print('yes')



функция reduce():
Функция reduce(), как можно понять из названия, применяет переданную функцию к итерируемому объекту и возвращает одно значение.


Синтаксис:

reduce(function, iterables)
Здесь функция определяет, какое выражение необходимо применить к итерируемому объекту. Эту функцию необходимо импортировать из модуля functools.

Пример:

from functools import reduce
reduce(lambda a, b: a + b, [23, 21, 45, 98])
Результат:

187

Функция zip
Функция zip() применяется к набору итерируемых
объектов и возвращает итератор с кортежами из
элементов входных данных.
Количество элементов в результате равно минимальному количеству элементов входного набора
zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
 ↓
[(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]


Функция enumerate
Функция enumerate() применяется к итерируемому
объекту и возвращает новый итератор с кортежами
из индекса и элементов входных данных.
enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
 ↓
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
Нельзя пройтись дважды

>>> nums = [1, 2, 3, 4, 5]
>>> odd_squares = [n*n for n in nums if n%2 == 1]
>>> print(odd_squares)
[1, 9, 25]