# In-class examples for Day 2

#%% List join, append and extend
alist = [1, 2, 3]
print(f"{alist = }")

alist = alist + [4]
print(f"{alist = }")

alist += [5]  # alist = alist + [5]
print(f"{alist = }")

alist.append(6)
print(f"{alist = }")

alist.extend([7, 8])
print(f"{alist = }")

alist.append([9, 10])
print(f"{alist = }")

print(f"{len(alist) = }")

#%% Sorting list
blist = [3, 1, 4, 2, 6, 5, 0]
clist = sorted(blist)  # ascending order
dlist = sorted(blist, reverse=True)  # descending order
print(f"{blist = }\n{clist = }\n{dlist = }")

elist = blist.sort(reverse=True)  # inplace sorting in descending order
print(f"{blist = }\n{elist = }")

#%% List methods
alist = [1, 2, 3.4, 'abc', [5, 6.78], 'yz', 1, 'a']

print(f"{alist.count(1) = }")
print(f"{alist.count('a') = }")
print(f"{alist.index(1) = }")  # only return the index of the first item that matches the value

alist.remove(1)  # only remove the first item that matches the value
print(f"{alist = }")

alist.insert(2, 5)  # insert 5 into the position with index 2
print(f"{alist = }")

r = alist.pop(1)  # remove and return the item at index 1
print(f"{alist = }, {r = }")

#%% Tuple packing and unpacking
atuple = 1, 2.3, 4.5, 6, 7, 9  # tuple packing
print(f"{atuple = }, {type(atuple) = }")

a, b, c, d, e, f = atuple  # tuple unpacking
print(f"{a = }, {b = }, {c = }, {d = }, {e = }, {f = }")

first, *intermediate, last = atuple
print(f"{first = }, {intermediate = }, {last = }")

#%% Dictionary creation and modification
adict = dict(a=1, b=2.5, c='abc')
print(f"{adict = }")
print(f"{adict['c'] = }")

# print(f"{adict['d'] = }")  # KeyError is raised as the key 'd' is not found in adict

# Use get() method to return the default value if the key is not found
print(f"{adict.get('d', 'No found') = }")
print(f"{adict = }")

# Use setdefault() method to insert the key and default value if the key is not found
print(f"{adict.setdefault('d', 0) = }")
print(f"{adict = }")

#%% Joining 2 dictionaries
d1 = {'a':1, 'b':2, 'c':3}
d2 = dict(x=4, y=5, z=6)
print(f"{d1 = }, {d2 = }")

# Method 1
d3 = d1.copy()
d3.update(d2)
print(f"{d3 = }")

# Method 2
d4 = d1 | d2
print(f"{d4 = }")

#%% Set methods
alist = [1, 2, 1, 3, 4, 5, 2, 1, 6]
aset = set(alist)
print(f"{alist = }\n{aset = }")

name1 = ['Ali', 'Baba', 'Cloud', 'Data', 'Engineer']
name2 = ['John', 'Donald', 'Engineer', 'Peter', 'Ali', 'Chan']

# Names appear in both lists
common_names = set(name1) & set(name2)
print(f"{common_names = }")

# Names appear in only one of the lists
uncommon_names = set(name1).symmetric_difference(set(name2))
print(f"{uncommon_names = }")

# All names in both lists
all_names = sorted(set(name1) | set(name2))
print(f"{all_names = }")

#%% Conditional statement
mark = 75
if mark >= 50:
    print("Passed the test")
    print("Well done")
    print("Good job")
else:
    print("Failed the test")
    print("Work harder")
    print("Good luck in your next attempt")
print("Good bye!")

#%% Ternary expression
num = int(input("Enter an interger: "))

# Use if-else statement
if num % 2:
    print("This is an odd number")
else:
    print("This is an even number")

# Use ternary expression
print(f"This is an {'odd' if num % 2 else 'even'} number")

#%% For loop examples
names = ['ali', 'baba', 'cloud']
ages = [13, 37, 46, 51]
blood_types = ['a', 'o', 'b', 'ab', 'o']

# Use index to loop through multiple lists
for i in range(len(names)):
    print(f"{i+1}. {names[i]} is {ages[i]} years old with blood type {blood_types[i]}.")

# Use zip() to combine multiple lists
for i, j, k in zip(names, ages, blood_types):
    print(f"{i} is {j} years old with blood type {j}.")

# Use enumerate to automatically add an index to each iteration
for h, (i, j, k) in enumerate(zip(names, ages, blood_types), start=1):
    print(f"{h}. {i.capitalize()} is {j} years old with blood type {k.upper()}.")

#%% While loop example
while True:
    name = input("Enter your name: ")    
    print(f"Hi {name}, welcome to Hello World")
    ...
    ans = input("Do you want to play again?([y]/n) ") or 'y'
    if ans in ('y', 'Y'):
        continue
    elif ans in ('n', 'N'):
        print("Good bye and see you next time!")
    else:
        print("Invalid choice! Exiting ...")
    break

#%% List comprehension example 1
# Select the words that start with vowels
words = ('ant', 'boy', 'eggs', 'cake', 'door', 'house', 'owl')

# Method 1 - Use for loop
vowel_words1 = []
for w in words:
    if w[0] in 'aeiou':
        vowel_words1.append(w)
print(f"{vowel_words1 = }")

# Method 2 - Use list comprehension
vowel_words2 = [w for w in words if w[0] in 'aeiou']
print(f"{vowel_words2 = }")

#%% List comprehension example 2
# Calculate the number of odd numbers in a list
from random import randint
numbers = [randint(1, 100) for _ in range(100)]  # populate the list with 100 random integers

# Method 1 - Use for loop
count = 0
for n in numbers:
    if n % 2:
        count += 1
print(f"There are {count} odd numbers in the list.")        

# Method - Use list comprehension
count2 = sum([n%2 for n in numbers])
print(f"There are {count2} odd numbers in the list.")        

#%% Dictionary comprehension
# Create a new dictionary for discounted price (after 10% discount)

prices = dict(apple=1.5, orange=3, durian=30, mango=12)

# Method 1 - Use for loop
new_prices = {}
for k in prices:
    new_prices[k] = 0.9 * prices[k]
print(f"{new_prices = }")

# Method 2 - Use dictionary comprehension
new_prices2 = {k: 0.9 * prices[k] for k in prices}
print(f"{new_prices2 = }")

#%% Use any() and all() function
# Check whether any words in the list starts with a vowel
alist = ['bees', 'cats', 'eggs', 'boy']

# Method 1 - Use for loop
ans = False
for w in alist:
    if w[0] in 'aeiou':
        ans = True
        break
if ans:
    print("There is at least one word that starts with a vowel.")
else:
    print("There is no word that starts with a vowel.")

# Method 2 - Use any() and list comprehension
if any([True if w[0] in 'aeiou' else False for w in alist]):
    print("There is at least one word that starts with a vowel.")
else:
    print("There is no word that starts with a vowel.")    

# Check whether all words in a list starts with a vowel
blist = ['apple', 'egg', 'ice', 'owl', 'umbrella']
if all([True if w[0] in 'aeiou' else False for w in blist]):
    print("All words start with a vowel.")
else:
    print("Not all words start with a vowel.")
    











































