# In-class examples for Day 1
#%% Numeric data types
import sys
sys.set_int_max_str_digits(10000)  # set new limit for the number of integer digits
a = 1283748213769871230980519480918238478283764923098090912837498721309803824
b = a ** 100
print(a, b, sep="\n")
print(a.__sizeof__())
print(b.__sizeof__())

c = 1234567890
d = 1_234_567_890
print(c, d, sep="\n")

#%% Binary and hexadecimal numbers
x = 0b10110101
y = 0x12cafe
print(x, y, sep=", ")
print(bin(x), hex(y), sep=", ")

#%% Variables
# 1star = 123  # variable name cannot start with digit

# class = 3  # Using keywords as variable name will cause syntax error

# a = 123
# print(type(a))

# type = 'A'
# print(type(a))  # Built-in functions will be shadowed by variables of the same name

# del type  # This will delete the variable
# print(type(a))

#%%Converting between different data types
a, b, c = 1, 2.3, '456'
print(type(a), type(b), type(c), sep=", ")

d, e, f = float(a), str(b), int(c)
print(type(d), type(e), type(f), sep=", ")

g = '1234'
print(g, type(g), sep=", ")
h = int(g)
print(h, type(h), sep=", ")

x = '123abc'  # This is a string of hexadecimal number
print(x, type(x), sep=", ")
y = int(x, 16)
print(y, hex(y), type(y), sep=", ")

#%% Type hinting
a: int = 123
b: float = 4.5

a = 'abc'
c:str = 2.5
print(a, b, c, sep=", ")

#%% Arithmetic operators
a = 3 ** 2
b = -3 ** 2
c= (-3) ** 2
print(a, b, c, sep=", ")

#%% Comparison operators
a = 10
b = 25
print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(0 <= a < 20)
print(0 <= b < 20)

#%% Raw string
print("You can insert \n as the newline character.")
print(r"You can insert \n as the newline character.")
print("You can insert \\n as the newline character.")

#%% String indexing and slicing
s = "Introduction to Python"
print("First character:", s[0])
print("Last character:", s[-1])
print("First 2 characters:", s[:2])
print("Last 5 characters:", s[-5:])
print("Reverse string:", s[::-1])

#%% String concatenation and repetition
a = '45'
b = '123'
c = a + b
print(a, b, c, sep=", ")

d = 10 * "Ha "
print(d)

#%% String methods
s = "Introduction to Python"
print(s.upper())
print(s.lower())
print(s.title())
print(s.replace('on', 'off'))
print(s)

t = s.upper().replace('N', 'm')  # chaining string methods
print(t)

#%% f-string formating
a = 12.345
b = 0.05
c = 67890

print(f"{a = }, {a = :.0f}, {a = :.1f}, {a = :.2f}")

print(f"Percentage: {b:.2%}")

print(f"Binary: {c:b}, Decimal: {c}, Hex: {c:x}")

print("Decimal     Binary")
for i in range(16):
    print(f"{i:>7}      {i:>04b}")

#%% Getting input from the user
num = input("Enter an integer: ")
print(f"{num = }, {type(num) = }")
print(f"10 times of {num} is {10 * num}")

if num.isdigit():
    print(f"10 times of {num} is {10 * int(num)}")
else:
    print(f"{num} is not an integer!")














