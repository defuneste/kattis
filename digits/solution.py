while True:
    line = input()
    if line == "END":
        break
    x = len(line)
    if line == "0":
        print(2)
        continue
    if x == 1 and line == "1":
        print(1)
        continue
    i = 1
    while x != 1:
        i = i + 1
        x = len(str(x))
    print(i + 1)
