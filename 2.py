

s1= 'привет страна далекая'
s2=',ehfnbyj'
a=s1+s2
b= list(a)
print(b)

print(''.join([s1, s2]))
l=''.join([s1, s2])
print(l)

def join_strs_better(strs):

    return ''.join(strs)


fin = join_strs_better(b) 
print(fin)    