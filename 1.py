from array import array


a =[3,5,4,2,3,88,4,6,9,10,3]
b=[9,5,12,3,6,48,9,2,1]
c=[8,3,1,58,6,4,89,4]

array = a+b+c





#print(array)



size = len(array)
finish_index = size - 1
index = 0

while finish_index > 0:
  index = 0
  while index < finish_index:
    if array[index] > array[index + 1]:
      temp = array[index]
      array[index] = array[index + 1]
      array[index + 1] = temp
    index += 1
  finish_index -= 1
#print(array)

    
size = len(array)

index = 0
c = []
while index <size-1:
    if array[index] != array[index + 1]:
        c= c+array[index+1]
      
    index += 1
  
print(c)




