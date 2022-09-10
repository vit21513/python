#m= [1,2,1,3,5,"a",[1,2],["s","f"]]

#print(m[-1][0])


m= [[5,6] ,[1,2], ["s","f"]]

m[0]= 9

#print(len(m[0])) # длина списка 0 =2
#print(len(m)) # длина общего списка 
print (m)
m[0]= m[0]+2
print (m)

m[1], m[2] = m[2], m[1]
print (m)

m = m+[7]
print (m)

n= list("stroka")

print (n)

n = list(range(10))

