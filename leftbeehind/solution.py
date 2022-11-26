import sys

lines = sys.stdin.read().splitlines()

for l in lines:
    [x,y] = [int(j) for j in l.split()]
    if x == y:
        if x != 0:
            print("Undecided.")
        else:
            pass
    elif y + x == 13:
        print("Never speak again.")
    elif x > y:
        print("To the convention.")
    else:
        print("Left beehind.")
