# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

# Method 1 - Use for loop
total = 1
for n in alist:
    total = total * n
print(total)

# Method 2 - Use list comprehension
p = 1
answer = [p:=p*i for i in alist][-1]
print(answer)

# Method 3 - Use math module
import math
print(math.prod(alist))