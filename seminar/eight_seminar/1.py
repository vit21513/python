

import sqlite3

bd= sqlite3.connect("Data_base.db")
cursor = bd.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
    id integer primary key AUTOINCREMENT,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT
)''')


baza=[(1,"Иван","Иванов","главный инженер",50000,10000),
(2,"Игорь","Семенов"," инженер",20000,8000),
(3,"Олег","Петров","завхоз",12000,3000),
(4,"Мария","Максимова","медсестра",15000,4560),
(5,"Клавдия","Рубенштейн","отдел кадров",20000,2500)]

try:
    cursor.executemany('INSERT INTO personal VALUES(?,?,?,?,?,?)',baza)
    bd.commit()
except:
    print('Данные уже есть')




def previev_base():
    print("""
|---База данных сотрудников компании-------|
--------------------------------------------
    """)
    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)
    print("""
--------------------------------------------
    """)    



def add_record():

    try:
        id = input('Введите номер записи:')
        nam = input('Введите имя сотрудника :').capitalize()
        last_na=input('Введите фамилию сотрудника :').capitalize()
        position= input('Введите должность сотрудника :')
        sal= input('Введите размер заработной платы сотрудника :')
        bon= input('Введите размер премии сотрудника :')
        cursor.execute('INSERT INTO personal VALUES(?,?,?,?,?,?)',(id, nam, last_na, position, sal,bon))
        bd.commit()
    except:
        print('Некоректный номер записи либо данные уже есть')

def find_record():
    nam = input('Введите фамилию сотрудника :').capitalize()
    cursor.execute(f'select * from personal WHERE last_name LIKE "{nam}";')
    result= cursor.fetchall()
    if result == []:
        print(f"Сотрудник c фамилией {nam} в базе отсутствует ")
    else:
        for i in result:
            print(*i)
   

def delete_record():
    previev_base()
    nam = input('Введите номер записи которую необходимо удалить :')
    cursor.execute(f'DELETE from personal WHERE id={nam};')
    bd.commit()
    
      


def edit_record():
    
    previev_base()
    try:
        id = input("Выберите id записи:")
        zp = input("Ввведите новый размер зарплаты:")
        premia = input("Ввведите новый размер премии :") 
        cursor.execute(f'UPDATE personal SET salary={zp} WHERE id={id};')
        cursor.execute(f'UPDATE personal SET bonus ={premia} WHERE id={id};')
        bd.commit()
        print("Изменения внесены")
    except:
        print("Вы ввели не коректные значения")
    
   


def input_choice():
    
    while True:

        user_choice= input('''
       _______________________________ 
      |                               | 
      |  1- просмотреть базу          |
      |  2- добавить запись           |
      |  3- удалить запись            | 
      |  4- найти по Ф.И.О:           | 
      |  5- изменить зарплату,премию  |
      |  q- выход                     |
      |_______________________________|
      
      ''')
        if user_choice == "1":
            previev_base()
        elif user_choice == "2":
            add_record()
        elif user_choice == "3":
            delete_record()
        elif user_choice == "4":
            find_record()
        elif user_choice == "5":
            edit_record()    
        elif user_choice.lower() == "q":
            print('Выход')
            break
        else:
            print('Не верно введен режим работы')   

                  

input_choice()