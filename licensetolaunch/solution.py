import sys

[n, l] = sys.stdin.read().splitlines()

waste = [int(i) for i in l.split()]

index = d = 0
g = waste[0]


for i in waste:
    if i < g:
        index = d
        g = i
    d = d + 1
    if d == int(n):
        break

print(index)
