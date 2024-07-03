# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:03:42 2024

@author: wooihaw
"""

from collections import Counter

data = None
with open("data/alice.txt", "r") as f:
    data = f.read()

if data is not None:
    t = [c.lower() if c.isalpha() else ' ' for c in data]
    # print(t)
    u = ''.join(t)
    w = u.split()
    # print(w)
    c = Counter(w)
    print(f"Number of unique words: {len(c)}")
    print(f"10 most common words: {c.most_common(10)}")
    print(f"The word 'alice' appears {c['alice']} times.")