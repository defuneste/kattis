
import sys

n = 0

for line in sys.stdin:
    x = [int(s) for s in line.split()][1:]
    n = n + 1
    mi = min(x)
    ma = max(x)
    rn = ma - mi
    print(f"Case {n}: {mi} {ma} {rn}")
