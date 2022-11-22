import sys

lines = [str(i) for i in sys.stdin.read().splitlines()][1:]

index = 0

for j in lines:
    [name, post, birth, course] = lines[index].split(" ")
    index = index + 1
    if int(post[0:4]) >= 2010:
        print(f"{name} eligible")
    elif int(birth[0:4]) >= 1991:
        print(f"{name} eligible")
    elif int(course) < 41:
        print(f"{name} coach petitions")
    else:
        print(f"{name} ineligible")
