myDict = {'a': 1, 'b': 2, 'c': 3}
print(myDict.get('A')) # No error, None returned
# print(myDict['A']) # Error

myDict.__setitem__('a', 4)
print(myDict.get('a'))

myDict.pop('c')
del myDict['b'] # cannot be myDict.get('b')
print(myDict)