# Write a Python script to find the frequency of occurance for each alphabet in a string.
astring = 'A quick brown fox jumps over the lazy dog.'

# Text cleaning and normalization
alist = [c.lower() for c in astring if c.isalpha()]
print(f"{alist = }")

# Use dictionary comprehension
adict = {k: alist.count(k) for k in sorted(set(alist))}
print(f"{adict = }")
