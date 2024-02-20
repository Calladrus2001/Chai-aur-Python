arr = [1,2,3,4,-1,-2,-3]
s = "buzz"
# counting postive numbers
pcount = sum(1 for x in arr if x > 0)

# sum of even numbers
esum = sum(x for x in arr if not x & 1)

# table of 3
tableOf3 = [x*3 for x in range(1,11)]

# reverse a string the hard way
s = s[::-1]

# find the first non-repeated char, couldnt code 1 liner for this
d = dict()
for c in s:
  if d.__contains__(c): d.__setitem__(c, d.get(c)+1)
  else: d.__setitem__(c, 1)
for k, v in d.items():
  if v == 1:
    print(k)
    break