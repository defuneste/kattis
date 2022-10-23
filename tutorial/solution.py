#!/usr/bin/env python3

from math import log2
from sys import getrecursionlimit

[m,n,t] = [int(i) for i in input().split()]

accepted = False

def fct(x):
    if x < 1:
        return 1
    elif x > getrecursionlimit():
        return 1000000001
    else:
        return x * fct(x - 1)

if t == 1 and fct(n) <= m:
    accepted = True
if t == 2 and 2 ** n <= m:
    accepted = True
if t == 3 and n ** 4 <= m:
    accepted = True
if t == 4 and n ** 3 <= m:
    accepted = True
if t == 5 and n ** 2 <= m:
    accepted = True
if t == 6 and n * log2(n) <= m:
    accepted = True
if t == 7 and n <= m:
    accepted = True

if accepted:
    print("AC")
else:
    print("TLE")
