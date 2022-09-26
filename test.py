# Реализуйте функцию filter_string(). Она принимает на вход строку и символ и
#  возвращает новую строку, в которой удалён переданный символ во всех его позициях. 
# Если строка не содержит указанный символ, то она возвращается без изменений.

# Итоговая строка также не должна содержать
#  начальные и концевые пробелы:

# text = 'If I look forward I win'
# filter_string(text, 'i')  # 'f  look forward  wn'
# filter_string(text, 'O')  # 'If I lk frward I win
# На этот раз реализуйте эту функцию с помощью цикла for. Дополнительное условие: регистр исключаемого символа не имеет значения.





def filter_string(strin,char):
     
    for i in strin:
        if i == char.lower():
            i=char.lower()
            res = strin.replace(char.lower(), '')
        elif i== char.upper():
            i= char.upper()
            res = strin.replace(char.upper(), '')
            
        
    return res

text = 'I look back if you are lost'
print(filter_string(text, 'I'))        


# assert filter_string(text, 'w') == 'I look back if you are lost'
# >       assert filter_string(text, 'I') == 'look back f you are lost'
# E       AssertionError: assert ' look back f you are lost' == 'look back f you are lost'
# E         - look back f you are lost
# E         +  look back f you are lost
# E         ? +
