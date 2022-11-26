import sys

lines = sys.stdin.read().splitlines()[1:]

for i in lines:
    if i == 'P=NP':
        print('skipped')
    else:
       to_add = [int(j) for j in i.split('+')]
       print(sum(to_add))
