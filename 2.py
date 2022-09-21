
import math


num1=int(input("Введите 1 число "))

num2= int(input("Введите 2 число "))


def sqr_num(a,b):
    res= a*b

    if a == b*b:
        print(f" число,{a}, является квадратом, {b}") 
    else:
        print(f" число,{a}, не является квадратом, {b}")

sqr_num(num1,num2)