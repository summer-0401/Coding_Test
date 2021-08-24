# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:05:37 2021

@author: USER
"""

n = int(input())

answer=1000001
for i in range(n, n//2, -1):
    numbers = list(map(int, str(i)))
    if i+sum(numbers) == n:
        answer = min(answer, i)
        
if answer<1000001:
    print(answer)
else:
    print(0)
        
        