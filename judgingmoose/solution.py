[l, r] = [int(i) for i in input().split()]

if l == r and l > 0:
    print(f"Even {l + r}")
elif l != r:
    odd = 2 * max(l, r)
    print(f"Odd {odd}")
else:
    print("Not a moose")
