import sys

l = sys.stdin.read().splitlines()[1:]

for i in l:
    temp = [int(j) for j in i.split()]
    start = temp[1]
    for k in range(2, len(temp)):
        num = temp[k]
        if num != start + 1:
            print(k)
            break
        start = num
