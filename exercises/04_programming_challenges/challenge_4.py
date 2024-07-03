# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:46:01 2024

@author: wooihaw
"""

def mean(data):
    return sum(data)/len(data)

def median(data):
    sdata = sorted(data)
    n = len(sdata)
    if n % 2:
        return sdata[n // 2]
    else:
        return (sdata[(n // 2) - 1] + sdata[n // 2]) / 2

with open("data/Heathrow.txt", "r") as f:
    raw_data = f.readlines()

# print(raw_data)    
data = [float(t.strip()) for t in raw_data]
# print(data)
print(f"Lowest: {min(data)}\nhighest: {max(data)}")
print(f"Mean: {mean(data)}")
print(f"Median: {median(data)}")
