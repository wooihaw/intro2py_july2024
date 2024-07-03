# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:41:20 2024

@author: wooihaw
"""

s1 = set(range(1, 101))  # set of all numbers from 1 to 100
s2 = set(range(5, 101, 5))  # set of all numbers divisible by 5
s3 = set(range(7, 101, 7))  # set of all numbers divisible by 7

print(f"List of the remaining number: {list(s1 - (s2 | s3))}")
