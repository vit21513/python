from ast import pattern



import re
pattern1= r'([-+])'
input_str='-12x3 - x2 +5x'
res=''
res1= re.search(pattern1, input_str)
print(res1)

re.compile