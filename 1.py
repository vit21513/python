from tracemalloc import start


n = list(range(1,21))
#b=n.copy()
#  или b = n[start:stop:step:]
b=n[::]
m = []
for i in n:
    if i %2 == 0:
        m.append(i)
        n.remove(i)
  
else:
    print(m)
    print(n)
    print (b)