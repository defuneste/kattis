
[a, b, c, n] = [int(i) for i in input().split()]

if n < 3 or a == 0 or b == 0 or c== 0:
    print("NO")
elif n > a + b + c:
    print("NO")
else:
    print("YES")
