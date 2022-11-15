import sys

tarif = [int(i) for i in sys.stdin.read().splitlines()]

x = tarif[0]
n = tarif[1:]
rest = 0

for j in range(len(n)):
    rest = rest + x - n[j]

print(rest + j)
