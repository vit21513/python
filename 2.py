
num = int(input('введите число '))


def printNum (number):
    number=abs(number)
    first = number*-1
    sec = number
    while first <= sec: 
        print(f'{first},',end="")
        first+=1

printNum(num)