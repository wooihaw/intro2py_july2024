# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:32:06 2024

@author: wooihaw
"""

invest = float(input("Enter the initial investment: "))
rate = float(input("Enter the annual rate (%): "))
years = int(input("Enter the number of years to invest: "))

print(f"Initial investment: RM{invest:.2f}, annual rate: {rate:.2f}%, investment years: {years}")

for y in range(years):
    invest = invest + invest * rate/100
    print(f"Year {y+1:>2}: RM{invest:.2f}")