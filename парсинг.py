
import os
import time
spisok =[]
fils =[]
#('D:\\тест', ['1', '2'], ['1.bmp', '2.bmp', 'первй.txt'])

for adres,dirs,files in os.walk ("c:\\"):
   #spisok.append(adres)
   for file in files:
    #spisok.append(os.path.join(adres,file)) # в список все файлы 
    full =os.path.join(adres,file)  
    #if ".txt" in full:               #  в список тоько файлы с тхт
    #    spisok.append(full)
    if time.time() - os.path.getctime(full) <86400: #(86400 сутки)   time.time() - текущее время
        spisok.append(full)

print (spisok)
