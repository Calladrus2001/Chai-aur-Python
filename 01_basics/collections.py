myDict = {'abc': 1, 'def': 2}
print(myDict['abc']) # returns 1
# print(myDict['f']) # will give traceback
if (myDict.__contains__('f')):
  print("found key")
else :
  print("did not find key")