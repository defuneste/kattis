[a, b] = [int(i) for i in input().split()]

ra = str(a)[::-1]
rb = str(b)[::-1]

if int(ra) > int(rb):
    print(ra)
else:
    print(rb)
