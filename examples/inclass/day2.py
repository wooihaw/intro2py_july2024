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



















































