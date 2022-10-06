# . Напишите программу, удаляющую из текста все слова, содержащие "абв".
import csv


text= 'начало сабвук керн укенр мабв бваав в абв сабв конец'
zx= text.split()
print(zx) 
cx=[]

for i in range(len(zx)-1):
         
    if "абв" in zx[i]:
        continue
    else:
        cx.append(zx[i])




print(cx) 