chai = "Masala chai chai chai"
print(chai.find("chai"))
if (chai.find("Chai") != -1):
  print("found")
else:
  print("not found")

print(f'count of chai is {chai.count("chai")}')
# this is an example of many types of strings in python, one more :

normal = "Masala\nChai"
print(normal) # result separated by newline
raw = r"Masala\nChai"
print(raw) # wihout newline