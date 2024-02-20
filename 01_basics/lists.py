array1 = [1,2,3,4]
for i in array1:
  print(i, end = ' ')

array2 = array1.copy()
array1 = [5]
print(f'array1 is {array1} but array2 is still {array2}')

array2 = [x*2 for x in array2] # List comprehension
print(array2)