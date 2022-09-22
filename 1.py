#По двум заданным числам проверить является ли одно квадратом второго.4

num1=int(input("Введите 1 число "))

num2= int(input("Введите 2 число "))


def sqr_num(a,b):
    res= a*b

    if a == b*b:
        print(f" число,{a}, является квадратом, {b}") 
    else:
        print(f" число,{a}, не является квадратом, {b}")

sqr_num(num1,num2)




#Вывести на экран числа от -N до N.

num = int(input('введите число '))


def printNum (number):
    number=abs(number)
    first = number*-1
    sec = number
    while first <= sec: 
        print(f'{first},',end="")
        first+=1

printNum(num)


#Найти максимальное из пяти чисел.


a= [5,71,9,3,22]

def find_max_number(list):
    maxindex = len(list)-1
    index=0
    max = list[0]
    while index <= maxindex: 
        if a[index]>max:
            max = a[index]
        index+=1
    return max         

print(find_max_number(a))


#Показать первую цифру дробной части числа.


num= float(input('Введите число '))
round_num= int(num) 

res = ((num -round_num)*10)

print(f' первая цифра дробной части {int(res)}')


#
#5. Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30.
#






#Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.


def Days(num):
    week= ['Понедельник', 'Вторник','Среда','Четверг','Пятница','Субота','Воскресенье']
    if num < 1 or num > 7:
        print("Вы ввели некоректное число")
    elif num >= 6:
        print(f"{week[num-1]} это выходной день")
    else:
        print(f"{week[num-1]} это рабочий день")



days =int(input("Введите день недели "))

Days(days)


#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
#  плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x_coord = int(input("введите координату х="))
y_coord = int(input("введите координату у="))


def quarter(x,y):
    if (x>0 and y>0):
        print("первая четверть")
    elif (x<0 and y>0):
        print("вторая четверть") 
    elif (x<0 and y<0):
        print("третья четверть")
    else:
        print("четвертая четверть")


quarter(x_coord,y_coord)