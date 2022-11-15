import sys

lines = sys.stdin.read().splitlines()

for i in lines:
    [a, b] =[int(j) for j in i.split()]
    print(abs(a -b))
