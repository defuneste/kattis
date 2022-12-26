import sys

def calc_score(x):
    x0 = int(x[0])
    x1 = int(x[1])
    if x == "21":
        return(100)
    elif x0 == x1:
        return 70 + x0
    else:
        return 10 * x0 + x1

for l in sys.stdin.read().splitlines():

    [s0, s1, r0, r1] = [str(i) for i in l.split()]

    if s0 == "0":
        break

    if s0 < s1:
        temp = s0
        s0 = s1
        s1 = temp
    p1 = s0+s1


    if r0 < r1:
        temp = r0
        r0 = r1
        r1 = temp
    p2 = r0+r1

    if calc_score(p1) == calc_score(p2):
        print("Tie.")
    else:
        winner = 1 if calc_score(p1) > calc_score(p2) else 2
        print(f"Player {winner} wins.")
