import sys

text = sys.stdin.read().splitlines()[1:]

qaly = 0.0

for i in text:
    [q, y] = [float(j) for j in i.split()]
    qaly = qaly + q * y

print('%.3f'%qaly)
