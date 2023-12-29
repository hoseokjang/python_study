# 1. list copy
a1 = [1, 2, 3]
b1= a1
# print(b1 is a1) # return -> True
print(b1)

# 2. [:]
a2 = [1, 2, 3]
b2 = a2[:]
print(b2)

# 3. copy
from copy import copy
a3 = [1, 2, 3]
b3 = copy(a3)
# print(b3 is a3) # return -> False
print(b3)

