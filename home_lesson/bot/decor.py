import math


# def my_funv(x, y):
#     print(f'{x=}')
#     print(f'{y=}')
#     return x * y


# def my_func2(x, y, *args):
#     print(f'{x=}')
#     print(f'{y=}')
#     other= args
#     print(other)


# # my_funv(y=8,x=3)


# my_func2(5,4,23,44)


# def my(*args, **kwargs):
#     a = args
#     b = kwargs

#     print(f'{a=}')
#     print(f'{b=}')


# my(1, 2, 3, 4, 5, 6, z=12, v=14, x=55)    

from functools import wraps
from datetime import datetime

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'площадь комнаты {res} m2 ')
        log_msg=f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}'  
        log_msg = f"параметры: {', '.join(map(str, args))}\t"
        witch open('log.file', 'w', encoding= 'utf-8') as fp:
            fp.wr
        print(log_msg)
        return res
    return wrapper 
            

@decorator

def area1(x, y):
    '''возврашает..
    '''

    return x*y



def main():
    print(area1(5,4))
    print(area1.__doc__)  #  убрать декоратор  . с ним не показывавет



if __name__ == '__main__':
    main()    