from itertools import permutations
matrics = '256 134 267 27 16 135 34'.split()
grafs = 'AF FE EC CG GD DB BA FB ED '.split()
print(*range(1, 8))
for i in permutations('AFECGDB'):
    if all(str(i.index(x)+1) in matrics[i.index(y)] for x,y in grafs):
        print(*i)