# 1По двум заданным числам проверить является ли одно квадратом второго.4

num1=int(input("Введите 1 число "))

num2= int(input("Введите 2 число "))


def sqr_num(a,b):
    res= a*b

    if a == b*b:
        print(f" число,{a}, является квадратом, {b}") 
    else:
        print(f" число,{a}, не является квадратом, {b}")

sqr_num(num1,num2)




2 #Найти максимальное из пяти чисел.


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




# 3Вывести на экран числа от -N до N.

num = int(input('введите число '))


def printNum (number):
    number=abs(number)
    first = number*-1
    sec = number
    while first <= sec: 
        print(f'{first},',end="")
        first+=1

printNum(num)





4 #Показать первую цифру дробной части числа.


num= float(input('Введите число '))
round_num= int(num) 

res = ((num -round_num)*10)

print(f' первая цифра дробной части {int(res)}')


#
#5. Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30.
#






# 6 Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.


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





8 #Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У.

x_coord = float(input("введите координату х="))
y_coord = float(input("введите координату у="))


def quarter(x,y):
    if (x>0 and y>0):
        print(f"точка с координатами x={x},y={y} находится в первой четверти")
    elif (x<0 and y>0):
        print(f"точка с координатами x={x},y={y} находится в второй четверти") 
    elif (x<0 and y<0):
        print(f"точка с координатами x={x},y={y} находится в третьей четверти")
    else:
        print(f"точка с координатами x={x},y={y}  находится четвертой четверти")


quarter(x_coord,y_coord)
             


#9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти.

num_quarter = int(input("Введите номер четверти "))


def quarter(num):
    if num==1:
        print("первая четверть x>0  y>0")
    elif num==2:
        print("вторая четверть  x<0  y>0") 
    elif num==3:
        print("третья четверть x<0  y<0")
    elif num==4:
        print("четвертая четверть x<0  y<0")

    else:
        print("такой четверти нет")


quarter(num_quarter)
             
                 
#10. Найти расстояние между двумя точками пространства.

x_coord = float(input("введите координату первого числа х="))
y_coord = float(input("введите координату первого числа у="))
x_coord2 = float(input("введите координату второго числа х="))
y_coord2 = float(input("введите координату второго числа у="))


def lens(x1, y1, x2, y2):
    res = round(((x2 - x1) ** 2 + ((y2 - y1)) ** 2) ** 0.5, 2)
    return res


result = lens(x_coord, y_coord, x_coord2, y_coord2)


print(result)

