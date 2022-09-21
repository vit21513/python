



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