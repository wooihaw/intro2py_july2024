# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:26:32 2024

@author: wooihaw
"""

# r + c = 35
# 4r + 2c = 94

for r in range(36): 
    c = 35 - r
    if 4*r + 2*c == 94:
        print(f"There are {c} chickens and {r} rabbits in the farm.")