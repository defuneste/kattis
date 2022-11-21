[G, S, C] = [int(i) for i in input().split()]

hand = G * 3 + S * 2 + C * 1

if hand >= 8:
    victory = "Province"
elif hand >= 5:
    victory = "Duchy"
elif hand >= 2:
    victory = "Estate"
else:
    victory = None

if hand >= 6:
    treasure = "Gold"
elif hand >= 3:
    treasure = "Silver"
else:
    treasure = "Copper"

if hand <= 1:
    print(treasure)
else:
    print(f"{victory} or {treasure}")
