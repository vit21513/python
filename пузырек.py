array = [3, -4, 1, 3, -1, 8, 2]
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
print(array)
