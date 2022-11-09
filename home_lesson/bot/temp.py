# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
# 1.1 (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)


import datetime
import time
from functools import wraps


def decorator(func):
    def wrapper(*args, **kwargs):
        
        print(f"Кеш функции при  n = {''.join(map(str, args))} составляет = ",end="")
        return func(*args, **kwargs)
        
    return wrapper    


def cacher(func):
    cach = {}
    def wrapper(*args):
        key =''.join(map(str, args))                           #
        if key not in cach:
            cach[key] = func(*args)
        print(cach)
        return cach[key]

    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        print(finish - start)
        return res
    return wrapper    







@decorator
# #timer
@cacher


def seq(n):
    res=[]
    for i in range(n+1):
        res.append((1+i)**i)
    return res
  
def main():
    # print(seq(1))
    # print(seq(2))
    # print(seq(3))
    # print(seq(4))
    # print(seq(3))
    # print(seq(2))
    # print(seq(1))
    seq(1)
    seq(2)
    seq(3)
    seq(4)
    seq(3)
    seq(2)
    seq(1)
    timer(seq(4))




if __name__ == '__main__':
    main()


# c= (1,2,3,4,5,6)

# a=list(c)
# map(str,a)
# print(a)