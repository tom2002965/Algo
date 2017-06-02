# count the number of prime

import numpy as np


def eratosthenes(n):
    n = ( n + 1) >> 1
    print n
    i, j, p = 1, 3, np.ones(n, dtype=np.int8)
    
    while i < n:
        if p[i]:
            p[j * j >> 1::j] = 0
            
        i, j = i + 1, j + 2
    
    return p.sum()

print eratosthenes(100)