
def Days(num):
    week= ['Понедельник', 'Вторник','Среда','Четверг','Пятница','Субота','Воскресенье']
    if (num < 1 or num > 7):
        print("Вы ввели некоректное число")
    elif num >= 6:
        print(f"{week[num-1]} это выходной день")
    else:
        print(f"{week[num-1]} это рабочий день")



days =int(input("Введите день недели "))

Days(days)

