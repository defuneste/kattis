import sys

x = [int(i) for i in sys.stdin.read().splitlines()][1:]

for j in x:
    if j % 2 == 0:
        print(f"{j} is even")
    else:
        print(f"{j} is odd")
