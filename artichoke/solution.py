import math
import sys

[p, a, b , c, d, n] = [int(i) for i in input().split()]

def fun_price(k):
    return(p * (math.sin((a * k) + b) + math.cos((c * k) + d) + 2))

start = fun_price(1)
decline = 0.0

for i in range(1, n + 1):
    #print(fun_price(i))
    if fun_price(i) >= start:
        start = fun_price(i)
    temp_decline = start - fun_price(i)
    if temp_decline >= decline:
        decline = temp_decline

if decline == 0:
    print("0.00")
else:
    print(f'{decline:.9f}')
