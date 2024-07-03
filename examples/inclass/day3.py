# In-class examples for Day 3
# Use pickle to store a dictionary to a file
import pickle

d = {'Ali': 23, 'Baba':34, 'Cloud':45}

with open("nameage.pkl", "wb") as f:
    pickle.dump(d, f)

#%% Use pickle to retrieve the dictionary from file
import pickle

with open("nameage.pkl", "rb") as f:
    e = pickle.load(f)

print(f"{e = }")

#%% Exception handling
while True:
    try:
        num = int(input("Enter an integer: "))
    except Exception as e:
        print("Error:", e)
    else:
        print(f"You have entered {num}")
        break

print("You have successfully break out from the loop")

#%% Function and return value
def fun1(x, y):
    print(x + y)

def fun2(x: int|float, y: int|float) -> int|float:
    '''This is a function to add 2 arguments.'''
    return x + y

a = fun1(12, 34)
b = fun2(56, 78)

print(f"{a = }, {b = }")

#%% Function that returns multiple values
def fun3(x: int|float, y:int|float, z:int|float) -> int|float:
    '''This is a function which returns 3 values.'''
    return 2*x, 3*y, 4*z

ans = fun3(12, 34, 56)
print(f"{ans = }, {type(ans) = }")

ans1, ans2, ans3 = fun3(12, 34, 56)
print(f"{ans1 = }, {ans2 = }, {ans3 = }")

#%% Functions are objects
def fun_1(x: int|float) -> int|float:
    return x + 1

def fun_2(y: int|float) -> int|float:
    return y * 2

def fun_3(z: int|float) -> int|float:
    return z - 3

alist = [4, 5, 6]
for i in alist:
    for fun in (fun_1, fun_2, fun_3):
        print(f"{fun}{i} = {fun(i)}")
        
#%% Lambda function example 1
alist = [(1, 2, 3), (11, 4, 2), (7, 9, 1)]
blist = sorted(alist)
print(f"{alist = }\n{blist = }")

# To sort according to the 3rd element of each tuple in descending order
clist = sorted(alist, key=lambda x: x[2], reverse=True)
print(f"{clist = }")

#%% Lambda function example 2
# Sort the list based on the ID numbers
IDs = ['ID21', 'ID7', 'ID55', 'ID101', 'ID3', 'ID83', 'ID11', 'ID234', 'ID57']
sorted_IDs = sorted(IDs)
print(f"{sorted_IDs = }")

new_sorted_IDs = sorted(IDs, key=lambda x: int(x[2:]))
print(f"{new_sorted_IDs = }")


print(f"ID of the oldest member: {min(IDs, key=lambda x: int(x[2:]))}")
print(f"ID of the youngest member: {max(IDs, key=lambda x: int(x[2:]))}")

#%% Lambda function example 3
alist = ['A', 'quick', 'blue', 'fox']
print(f"{sorted(alist) = }")

# Sort according to the number of characters in the strings
print(f"{sorted(alist, key=lambda x:len(x)) = }")

#%% Example of map() function
# Revese each string in a list
words = ['apple', 'bell', 'cat', 'door', 'eggs']

# Method 1 - Use for loop
r1 = []
for w in words:
    r1.append(w[::-1])
print(f"{r1 = }")

# Method 2 - Use list comprehension
r2 = [w[::-1] for w in words]
print(f"{r2 = }")

# Method 3 - Use map() function
r3 = list(map(lambda x: x[::-1], words))
print(f"{r3 = }")

#%% Exampel of filter() function
# Select only the words which are palindrome
words = ['ant', 'boy', 'dad', 'fish', 'mom', 'madam']

# Method 1 - Use for loop
p1 = []
for w in words:
    if w == w[::-1]:
        p1.append(w)
print(f"{p1 = }")

# Method 2 - Use list comprehension
p2 = [w for w in words if w == w[::-1]]
print(f"{p2 = }")

# Method 3 - Use filter() function
p3 = list(filter(lambda w: w == w[::-1], words))
print(f"{p3 = }")

#%% OOP example
class Rectangle:
    desc = "This is a rectangle"
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __str__(self):
        return f"A {self.length} x {self.width} rectangle"
    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"
    def __eq__(self, other):
        return self.area() == other.area()
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2*self.width + 2*self.length
    
r1 = Rectangle(2, 3)
r2 = Rectangle(3, 2)
r3 = Rectangle(4, 5)

print(r1)
print(f"{r1 = }, {r1.area() = }, {r1.perimeter() = }")

for r in (r1, r2, r3):
    print(r)
    
if r1 == r3:
    print("They are equal")
else:
    print("They are not equal")
    
# Child class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def __str__(self):
        return f"A {self.length} x {self.width} square"
        
s1 = Square(3)

print(s1)
print(f"{s1.area() = }, {s1.perimeter() = }")


    















