import sys

[x, y] = [int(i) for i in sys.stdin.read().splitlines()]

if (x > 0) & (y > 0):
    print(1)
elif (x < 0) & (y > 0):
    print(2)
elif (x < 0)  & (y < 0):
    print(3)
else:
    print(4)
