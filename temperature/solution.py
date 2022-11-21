
[x, y] = [int(i) for i in input().split()]

if (x == 0) & (y == 1):
    print("ALL GOOD")
elif y == 1:
    print("IMPOSSIBLE")
else:
    res = x / (1 -y)
    if float.is_integer(res):
        print(int(res))
    else:
        print("%.9f"%res)
