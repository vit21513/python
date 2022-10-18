# . Напишите программу, удаляющую из текста все слова, содержащие "абв".
import csv


text= 'начало самозабвенность текста включает зимбабве  абзац в абв абвер листе '
zx= text.split()
print(zx) 
cx=[]

for i in range(len(zx)):
         
    if "абв" in zx[i]:
        continue
    else:
        cx.append(zx[i])
    res=' '.join(cx)    




print(res) 